from typing import Union, Any, Dict, Callable, List, Optional
from .grammar import (
    QueryBuilder, QueryParseError, Query as QueryPart, Special, Field, ListValue, DictValue, SetValue, Value
)
import logging
from datetime import datetime, timezone
import math
from os import environ
from dateutil.parser import parse

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("LOGGING_LEVEL", "INFO"))

__all__ = ["Query"]


def parse_dt_string(value, fmt=None):
    if fmt is None:
        return parse(value)
    else:
        return datetime.strptime(value, fmt)


def wildcard(value: dict, nxt: Union[str, int], just_field=True):
    out = []
    for v in value.values():
        if (isinstance(v, dict) and nxt in v) or (
                # check if this object has the ability to get a specific index
                not isinstance(v, dict) and isinstance(nxt, int) and getattr(
                v, "__getitem__", None) is not None and 0 <= nxt < len(v)
        ):
            if just_field:
                out.append(v[nxt])
            else:
                out.append(v)

    return out


class Query:
    """
    FieldGetter provides a powerful way to access that attributes of JSON-like data and perform
    manipulations on them.
    """

    _specials: Dict[str, Callable] = {
        # general
        "length": lambda value: len(value),
        "lookup": lambda value, mp, fallback=None: mp.get(value, fallback),

        # dict
        "keys": lambda value: list(value.keys()),
        "values": lambda value: list(value.values()),
        "items": lambda value: list(value.items()),
        "wildcard": lambda value, nxt, just_field=True: wildcard(value, nxt, just_field),

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
        "wrap": lambda value, prefix, suffix: f"{prefix}{value}{suffix}",
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
        "remove_nulls": lambda value: [v for v in value if v is not None],

        # attribute accessing
        "call": lambda value, func, *args: getattr(value, func)(*args),
        "attr": lambda value, attr: getattr(value, attr)
    }

    _specials["map"] = lambda value, special, *args: [Query._specials[special](v, *args) for v in value]

    def __init__(self,
                 field: Union[str, List[str], QueryPart, List[QueryPart]], convert_ints: bool = True,
                 fallback: any = None):
        """
        Create an object for a specific field query string or strings.
        :param field: The field query string (or strings) or the query parts.
        :param convert_ints: Whether to convert <field> values that are digits to be ints to allow array indexing, or
            whether to leave them as strings.
        :param fallback: A fallback value that will be used a field cannot be found on a given object
        """
        self.multiple: bool = not (isinstance(field, str) or isinstance(field, QueryPart))
        self.fields: Union[List[str], List[QueryPart]] = field if self.multiple else [field]
        self.fallback = fallback
        self.convert_ints = convert_ints

        self.parts: List[Optional[QueryPart]] = []
        for f in self.fields:
            if isinstance(f, QueryPart):
                self.parts.append(f)
            else:
                try:
                    p = QueryBuilder(f, convert_ints=self.convert_ints).get_built_query()
                    self.parts.append(p)
                except QueryParseError:
                    self.parts.append(None)

        logger.debug(f"got parts: {self.parts}")

    def __repr__(self):
        return f"Getter: {self.parts}"

    @classmethod
    def full_regex(cls):
        return ""

    @classmethod
    def register_special(cls, name: str, func: Callable) -> bool:
        """
        Register a new special that can be accessed with $<name>.
        The function should take at least one argument, <value>.
        :param name: The name of the special
        :param func: The function that will be applied to the value
        """
        if name not in cls._specials:
            cls._specials[name] = func
            return True
        else:
            logger.warning(f"{name} is already registered as a special value")
            return False

    def single(self, item: Union[list, dict]) -> Union[Any, List[Any]]:
        """
        Get the field from the specified item
        """
        values = []
        for query in self.parts:
            if query is not None:
                values.append(self._query(item, query))
            else:
                values.append(self.fallback)

        return values if self.multiple else values[0]

    def _query(self, value, query: QueryPart):
        original = value
        for part in query.parts:
            if value != self.fallback:
                if isinstance(part, Field):
                    if isinstance(value, list):
                        if isinstance(part.field, int) and 0 <= part.field < len(value):
                            value = value[part.field]
                        else:
                            value = self.fallback
                    else:
                        if part.field in value:
                            value = value[part.field]
                        else:
                            value = self.fallback
                elif isinstance(part, Special):
                    arguments = []
                    arguments_safe = True

                    for arg in part.arguments:
                        v = self._value(original, arg)
                        if v != self.fallback:
                            arguments.append(v)
                        else:
                            value = self.fallback
                            arguments_safe = False

                    if arguments_safe:
                        value = self._specials[part.special](value, *arguments)

        return value

    def _value(self, value, q_or_v: Union[QueryPart, Value]):
        if isinstance(q_or_v, QueryPart):
            return self._query(value, q_or_v)
        elif isinstance(q_or_v, ListValue):
            return [self._value(value, part) for part in q_or_v.value]
        elif isinstance(q_or_v, DictValue):
            return {self._value(value, k): self._value(value, v) for k, v in q_or_v.value.items()}
        elif isinstance(q_or_v, SetValue):
            return {self._value(value, part) for part in q_or_v.value}
        else:
            return q_or_v.value

    def many(self, items: List[Union[list, dict]]) -> Union[List[Any], List[List[Any]]]:
        return [self.single(item) for item in items]


if __name__ == "__main__":
    print(Query("found.missing", fallback="N/A").single({"found": {}}))
