from typing import Union, Any, Dict, Callable, List, Optional
from .grammar import *
import logging
from datetime import datetime, timezone
import math
from os import environ
from dateutil.parser import parse

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("JTOOLS_LOGGING_LEVEL", "WARNING"))

__all__ = ["Query", "SpecialNotFoundError"]


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


def print_return(value, *, _):
    print(value)
    return value


def index(value, i, fallback=None):
    try:
        return value[i]
    except IndexError:
        return fallback


def store_as(value, name, *, context):
    context[name] = value
    return value


def group_by(value, key="", count=False, *, context) -> Dict[any, Union[List[any], int]]:
    """
    Group the incoming values
    :param value: Incoming list
    :param key: The key to use in grouping the items. If no key, then the value will be used. Any valid JQL query
    :param count: Whether to just count the items or create a list with them
    :param context: context
    """
    query = Query(key)
    out = {}
    for v in value:
        part = query.single(v)

        if part in out:
            if count:
                out[part] += 1
            else:
                out[part].append(v)
        else:
            if count:
                out[part] = 1
            else:
                out[part] = [v]

    return out


def sort(value, key="", reverse=False, *, context) -> list:
    """
    Sort the value by the specified key
    :param value:
    :param key: The key to sort by, any valid JQL query, or "", to just sort based on the top-level values
    :param reverse: Whether to reverse the sorting or not
    :param context:
    :return:
    """
    if key is None:
        return sorted(value, reverse=reverse)
    else:
        query = Query(key)
        return sorted(value, key=query.single, reverse=reverse)


class Query:
    SPECIALS: Dict[str, Callable] = {
        # general
        "length": lambda value, *, context: len(value),
        "lookup": lambda value, mp, fallback=None, *, context: mp.get(value, fallback),
        "inject": lambda _, value, *, context: value,
        "print": print_return,
        "store_as": store_as,
        "group_by": group_by,

        # dict
        "keys": lambda value, *, context: list(value.keys()),
        "values": lambda value, *, context: list(value.values()),
        "items": lambda value, *, context: list(value.items()),
        "wildcard": lambda value, nxt, just_field=True, *, context: wildcard(value, nxt, just_field),

        # type conversions
        "set": lambda value, *, context: set(value),
        "float": lambda value, *, context: float(value),
        "string": lambda value, *, context: str(value),
        "dict": lambda value, context: dict(value),
        "int": lambda value, *, context: int(value),
        "not": lambda value, *, context: not value,
        "fallback": lambda value, fallback, *, context: value if value else fallback,
        "ternary": lambda value, if_true, if_false, strict=False, *, context: if_true if (not strict and value) or (
                strict and value is True) else if_false,

        # datetime
        "parse_timestamp": lambda value, *, context: datetime.utcfromtimestamp(value),
        "strptime": lambda value, fmt=None, *, context: parse_dt_string(value, fmt),
        "timestamp": lambda value, *, context: value.replace(tzinfo=timezone.utc).timestamp(),
        "strftime": lambda value, fmt="%Y-%m-%dT%H:%M:%SZ", *, context: value.strftime(fmt),

        # math / numeric
        "add": lambda value, num, *, context: value + num,
        "subtract": lambda value, num, *, context: value - num,
        "multiply": lambda value, num, *, context: value * num,
        "divide": lambda value, num, *, context: value / num,
        "pow": lambda value, num, *, context: value ** num,
        "abs": lambda value, *, context: abs(value),
        "distance": lambda value, other, *, context: math.sqrt(sum((a-b)**2 for a, b in zip(value, other))),
        "math": lambda value, attr, *, context: getattr(math, attr)(value),
        "round": lambda value, n=2, *, context: round(float(value), n),

        # string
        "prefix": lambda value, prefix, *, context: f"{prefix}{value}",
        "suffix": lambda value, suffix, *, context: f"{value}{suffix}",
        "wrap": lambda value, prefix, suffix, *, context: f"{prefix}{value}{suffix}",
        "strip": lambda value, *, context: value.strip(),
        "replace": lambda value, old, new, *, context: value.replace(old, new),
        "trim": lambda value, length=50, suffix="...", *, context: value[:length-len(suffix)]+(
            suffix if len(value) > length-len(suffix) else ""
        ),
        "split": lambda value, on=" ", *, context: value.split(on),

        # list
        "sum": lambda value, *, context: sum(value),
        "join": lambda value, sep=", ", *, context: sep.join(str(i) for i in value),
        "join_arg": lambda _, arg, sep=', ', *, context: sep.join(str(i) for i in arg),
        "index": lambda value, i, fallback=None, *, context: index(value, i, fallback),
        "range": lambda value, start, end=None, *, context: value[start: end if end is not None else len(value)],
        "remove_nulls": lambda value, *, context: [v for v in value if v is not None],
        "sort": sort,

        # attribute accessing
        "call": lambda value, func, *args, context: getattr(value, func)(*args),
        "attr": lambda value, attr, *, context: getattr(value, attr)
    }

    SPECIALS["map"] = lambda value, special, *args, context: [
        Query.SPECIALS[special](v, *args, context=context) for v in value
    ]

    def __init__(self,
                 query: Union[str, List[str], JQLQuery, List[JQLQuery]], convert_ints: bool = True,
                 fallback: any = None):
        """
        Create a query object from a JQL query string, or list of JQL query strings.
        :param query: The JQL query string(s)
        :param convert_ints: Whether to treat digit-only field values as integers or strings
        :param fallback: A fallback value that will be used if a field cannot be found
        """
        self.multiple: bool = not (isinstance(query, str) or isinstance(query, JQLQuery))
        self.fields: Union[List[str], List[JQLQuery]] = query if self.multiple else [query]
        self.fallback = fallback
        self.convert_ints = convert_ints

        self.parts: List[Optional[JQLQuery]] = []
        for f in self.fields:
            if isinstance(f, JQLQuery):
                self.parts.append(f)
            else:
                try:
                    if f == "":
                        p = JQLQuery()
                    else:
                        p = JQLQueryBuilder(f, convert_ints=self.convert_ints).get_built_query()
                    self.parts.append(p)
                except JQLParseError:
                    self.parts.append(None)

        logger.debug(f"got parts: {self.parts}")

    def __repr__(self):
        return f"Query: {self.parts}"

    def _query(self, value, query: JQLQuery, context: dict):
        original = value
        for i, part in enumerate(query.parts):
            if isinstance(part, JQLField):
                if value != self.fallback:
                    try:
                        value = value[part.field]
                    except Exception:
                        # if this is the base part of a query, then check the current context
                        if i == 0 and part.field in context:
                            value = context[part.field]
                        else:
                            value = self.fallback
            elif isinstance(part, JQLSpecial):
                arguments = []
                arguments_safe = True

                for arg in part.arguments:
                    v = self._value(original, arg, context)
                    if v != self.fallback:
                        arguments.append(v)
                    else:
                        value = self.fallback
                        arguments_safe = False

                if arguments_safe:
                    if part.special in self.SPECIALS:
                        value = self.SPECIALS[part.special](value, *arguments, context=context)
                    else:
                        raise SpecialNotFoundError(part.special)

        return value

    def _value(self, value, q_or_v: Union[JQLQuery, JQLValue], context: dict):
        if isinstance(q_or_v, JQLQuery):
            return self._query(value, q_or_v, context)
        elif isinstance(q_or_v, JQLList):
            return [self._value(value, part, context) for part in q_or_v.value]
        elif isinstance(q_or_v, JQLDict):
            return {
                self._value(value, k, context): self._value(value, v, context)
                for k, v in q_or_v.value.items()
            }
        elif isinstance(q_or_v, JQLSet):
            return {self._value(value, part, context) for part in q_or_v.value}
        else:
            return q_or_v.value

    def single(self, item: Union[list, dict]) -> Union[Any, List[Any]]:
        """
        Query the item
        :param item: The item to query
        :return: A value, or list of values, depending on whether one or multiple queries are present
        """
        values = []
        for query in self.parts:
            if query is not None:
                values.append(self._query(item, query, {}))
            else:
                values.append(self.fallback)

        return values if self.multiple else values[0]

    def many(self, items: List[Union[list, dict]]) -> Union[List[Any], List[List[Any]]]:
        """
        Query the items
        :param items: The items to query
        :return: A list of values or a list of lists of values, depending on whether one or multiple queries are present
        """
        return [self.single(item) for item in items]

    @classmethod
    def register_special(cls, name: str, func: Callable) -> bool:
        """
        Register a new special that can be accessed with $<name>.
        The function should take at least one argument, which will be the current value in query.
        :param name: The name of the special - must only contain these characters: [-a-zA-Z0-9_]
        :param func: The function that will be applied to the value
        :return Whether or not the special could be registered
        """
        if name not in cls.SPECIALS:
            cls.SPECIALS[name] = func
            return True
        else:
            logger.warning(f"{name} is already registered as a special value")
            return False


class SpecialNotFoundError(Exception):
    def __init__(self, special):
        super().__init__(f"'{special}' is not a valid special. Valid options are {list(Query.SPECIALS.keys())}")


if __name__ == "__main__":
    print(Query("found.missing", fallback="N/A").single({"found": {}}))
