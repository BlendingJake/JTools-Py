from typing import Union, Any, Dict, Callable, List
import re
import logging
from datetime import datetime, timezone
import math
import json
from os import environ
from dateutil.parser import parse

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("LOGGING_LEVEL", "INFO"))

__all__ = ["Getter"]


def parse_dt_string(value, fmt=None):
    if fmt is None:
        return parse(value)
    else:
        return datetime.strptime(value, fmt)


class Getter:
    """
    FieldGetter provides a powerful way to access that attributes of JSON-like data and perform
    manipulations on them. The `field` notation is listed below by the constructor.
    """
    _arguments = r"""((?:(?!{{)(?:(?:"(?!{{)[^"]*")|[^\)]))*)"""
    _func_def = r"(?:\$[a-z]+[_]*[a-z]+(?:\(" + _arguments + r"\))?)"
    _field = r"[-_a-zA-Z0-9]+"
    _part = r"(?:\.(" + _func_def + "|" + _field + "))"

    _part_pattern = re.compile(_part)
    _full_field = "(" + _field + ")(" + _part + "*)"
    _full_pattern = re.compile(_full_field)

    logger.debug(f"Function Def: {_func_def}")
    logger.debug(f"Part Def: {_part}")
    logger.debug(f"Full Def: {_full_field}")

    _specials: Dict[str, Callable] = {
        # general
        "length": lambda value: len(value),

        # dict
        "keys": lambda value: list(value.keys()),
        "values": lambda value: list(value.values()),
        "items": lambda value: list(value.items()),

        # type conversions
        "set": lambda value: set(value),
        "float": lambda value: float(value),
        "string": lambda value: str(value),
        "int": lambda value: int(value),
        "not": lambda value: not value,
        "fallback": lambda value, fallback: value if value else fallback,
        "ternary": lambda value, if_true, if_false, strict=False: if_true if (not strict and value) or (
                strict and value is True) else if_false,

        # datetime
        "parse_timestamp": lambda value: datetime.utcfromtimestamp(value),
        "datetime": lambda value, attr: getattr(value, attr),
        "strptime": lambda value, fmt=None: parse_dt_string(value, fmt),
        "timestamp": lambda value: value.replace(tzinfo=timezone.utc).timestamp(),
        "strftime": lambda value, fmt="%Y-%m-%dT%H:%M:%SZ": value.strftime(fmt),

        # math / numeric
        "add": lambda value, num: value + num,
        "subtract": lambda value, num: value - num,
        "multiply": lambda value, num: value * num,
        "divide": lambda value, num: value / num,
        "pow": lambda value, num: value ** num,
        "abs": lambda value: abs(value),
        "distance": lambda value, other: math.sqrt(sum((a-b)**2 for a, b in zip(value, other))),
        "math": lambda value, attr: getattr(math, attr)(value),
        "round": lambda value, n=2: round(float(value), n),

        # string
        "prefix": lambda value, prefix: f"{prefix}{value}",
        "suffix": lambda value, suffix: f"{value}{suffix}",
        "strip": lambda value: value.strip(),
        "replace": lambda value, old, new: value.replace(old, new),
        "trim": lambda value, length=50, suffix="...": value[:length-len(suffix)]+(
            suffix if len(value) > length-len(suffix) else ""
        ),
        "split": lambda value, on=" ": value.split(on),

        # list
        "sum": lambda value: sum(value),
        "join": lambda value, sep=", ": sep.join(str(i) for i in value),
        "index": lambda value, index: value[index],
        "range": lambda value, start, end=None: value[start: end if end is not None else len(value)],
    }

    _specials["map"] = lambda value, special, *args: [Getter._specials[special](v, *args) for v in value]

    def __init__(self, field: Union[str, List[str]], convert_ints=True, fallback=None):
        """
        Create a FieldGetter for a specific field query string.
        :param field: The field query string (or strings),
                formatted <field>[.<field>|.$<special>[(<arg>[, <arg>]*)]],
            where:
                field: An exact field name or index value to get from the items provided later with `.single` or `.many`
                special: Any name in the `_specials` map above
                arg: Any JSON-formatted value. Note: JSON requires strings to be double-quoted

            Examples:
                friends.$length
                friends.$index(-1)  # get last friend
                age.$subtract(2020).$abs  # basic age calculation
                coordinate.$distance([0, 0])  # distance from origin in 2-D
        :param convert_ints: Whether to convert <field> values that are digits to be ints to allow array indexing, or
            whether to leave them as strings.
        :param fallback: A fallback value that will be used a field cannot be found on a given object
        """
        self.multiple = isinstance(field, (list, tuple))
        self.fields: List[str] = field if self.multiple else [field]
        self.fallback = fallback
        self.convert_ints = convert_ints

        self.parts: List[list] = [self._process_field(f) for f in self.fields]

    def __repr__(self):
        return f"Getter: {self.parts}"

    def _process_field(self, field):
        # splits into anchor field and then the rest of the parts
        parts = []
        match = self._full_pattern.match(field)
        if match is not None:
            full_groups = match.groups()
            parts.append(full_groups[0])  # anchor

            if full_groups[1]:
                for part in self._part_pattern.findall(full_groups[1]):
                    if part[0][0] == "$":  # is a special
                        if "(" in part[0]:
                            special = part[0][1:part[0].index("(")]
                        else:  # no args
                            special = part[0][1:]

                        if part[1]:
                            logger.debug(f"going to load: [{part[1]}]")
                            args = json.loads(f"[{part[1]}]")
                        else:
                            args = []

                        parts.append({
                            "special": special,
                            "args": args
                        })
                    else:  # regular field
                        if self.convert_ints:
                            try:
                                p = int(part[0])
                                parts.append(p)
                            except ValueError:
                                parts.append(part[0])
                        else:
                            parts.append(part[0])
        return parts

    @classmethod
    def full_regex(cls):
        return cls._full_field

    @classmethod
    def register_special(cls, name: str, func: Callable):
        """
        Register a new special that can be accessed with $<name>.
        The function should take at least one argument, <value>.
        :param name: The name of the special
        :param func: The function that will be applied to the value
        """
        if name not in cls._specials:
            cls._specials[name] = func
        else:
            raise NameError(f"{name} is already registered as a special value")

    def single(self, item: Union[list, dict]) -> Union[Any, List[Any]]:
        """
        Get the field from the specified item
        """
        values = []
        if not self.parts:
            return self.fallback
        else:
            for field in self.parts:
                value = item
                for part in field:
                    if value != self.fallback:
                        if isinstance(part, dict):
                            value = self._specials[part["special"]](value, *part["args"])
                        else:
                            if isinstance(value, list):
                                if part < len(value):
                                    value = value[part]
                                else:
                                    logger.warning(f"Could not find field '{part}'")
                                    value = self.fallback
                            else:
                                if part in value:
                                    value = value[part]
                                else:
                                    logger.warning(f"Could not find field '{part}'")
                                    value = self.fallback
                values.append(value)

        return values if self.multiple else values[0]

    def many(self, items: List[Union[list, dict]]) -> Union[List[Any], List[List[Any]]]:
        return [self.single(item) for item in items]


if __name__ == "__main__":
    print(Getter("a"))
