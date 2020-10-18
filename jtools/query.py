from typing import Union, Any, Dict, Callable, List, Optional, Tuple
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


def group_by(value, key: Union[str, int] = "", count=False, *, context) -> Dict[any, Union[List[any], int]]:
    """
    Group the incoming values
    :param value: Incoming list
    :param key: The key to use in grouping the items. If no key, then the value will be used. Any valid JQL query
    :param count: Whether to just count the items or create a list with them
    :param context: context
    """
    if isinstance(key, int):
        get_value = lambda x: x[key]
    else:
        if key in QUERY_CACHE:
            query = QUERY_CACHE[key]
        else:
            query = Query(key)
            QUERY_CACHE[key] = query

        get_value = lambda x: query.single(x)

    out = {}
    for v in value:
        part = get_value(v)

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


def index_special(value, key: Union[int, str, List[Union[str, int]]], fallback=None, extended=False, *, context):
    multiple = isinstance(key, list)

    if extended:
        query_key = str(key) + str(fallback)
        if query_key in QUERY_CACHE:
            query = QUERY_CACHE[query_key]
        else:
            query = Query(
                [str(x) for x in key] if multiple else str(key),
                fallback=fallback
            )
            QUERY_CACHE[query_key] = query

        return query.single(value, context=context)
    else:
        out = []
        for x in (key if multiple else [key]):
            try:
                out.append(value[x])
            except (IndexError, KeyError, TypeError):
                try:
                    out.append(context[x])
                except (IndexError, KeyError, TypeError):
                    out.append(fallback)

        return out if multiple else out[0]


def key_of_max_value(value, just_key=True, *, context):
    key = None
    for k, v in value.items():
        if key is None or v > value[key]:
            key = k

    if just_key:
        return key
    else:
        return key, value[key]


def key_of_min_value(value, just_key=True, *, context):
    key = None
    for k, v in value.items():
        if key is None or v < value[key]:
            key = k

    if just_key:
        return key
    else:
        return key, value[key]


def parse_dt_string(value, fmt=None):
    if fmt is None:
        return parse(value)
    else:
        return datetime.strptime(value, fmt)


def print_return(value, *, context):
    print(value)
    return value


def special_pipeline(
        value,
        pipeline,
        *, context):
    """
    Take a value and map it through multiple specials
    :param value: The value to pipe through the specials
    :param pipeline: The specials to execute on the value. Each entry can be:
        str - The name of the special
        [str, *args] - The name of the special, followed by positional arguments
        [str, dict] - The name of the special, followed by a dict of keyword arguments
        [str, *args, dict] - The name of the special, followed by positional and then a dict of keyword arguments
    :param context: The current context expanding the local query namespace
    """
    local_value = value
    for stage in pipeline:
        if isinstance(stage, str):
            local_value = Query.SPECIALS[stage](local_value, context=context)
        elif isinstance(stage[-1], dict):
            local_value = Query.SPECIALS[stage[0]](local_value, *stage[1:-1], **stage[-1], context=context)
        else:
            local_value = Query.SPECIALS[stage[0]](local_value, *stage[1:], context=context)

    return local_value


def sort(value, key: Union[str, int] = "", reverse=False, *, context) -> list:
    """
    Sort the value by the specified key
    :param value:
    :param key: The key to sort by, any valid JQL query, or "", to just sort based on the top-level values
    :param reverse: Whether to reverse the sorting or not
    :param context:
    :return:
    """
    if isinstance(key, int):
        return sorted(value, key=lambda x: x[key], reverse=reverse)
    else:
        if key in QUERY_CACHE:
            query = QUERY_CACHE[key]
        else:
            query = Query(key)
            QUERY_CACHE[key] = query

        return sorted(value, key=query.single, reverse=reverse)


def store_as(value, name, *, context):
    context[name] = value
    return value


def time_part(value: datetime, part, *, context):
    if part == "millisecond":
        return int(value.microsecond / 1000)
    elif part == "second":
        return value.second
    elif part == "minute":
        return value.minute
    elif part == "hour":
        return value.hour
    elif part == "day":
        return value.day
    elif part == "month":
        return value.month
    elif part == "year":
        return value.year
    elif part == "dayOfWeek":
        return value.weekday()
    elif part == "dayOfYear":
        return value.timetuple().tm_yday


def wildcard(value: dict, nxt: Union[str, int], just_field=True, *, context):
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


def value_map(value, special: str, *args, duplicate=True, context, **kwargs):
    real_value = {**value} if duplicate else value

    for key in real_value:
        real_value[key] = Query.SPECIALS[special](value[key], *args, **kwargs, context=context)

    return real_value


class Query:
    MISSING = object()

    MATH_OPERATIONS: Dict[str, Callable[[Union[int, float], Union[int, float]], Union[int, float]]] = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "//": lambda a, b: a // b,
        "**": lambda a, b: a ** b,
        "%": lambda a, b: a % b
    }

    SPECIALS: Dict[str, Callable] = {
        # general
        "length": lambda value, *, context: len(value),
        "lookup": lambda value, lookup, fallback=None, *, context: lookup.get(value, fallback),
        "inject": lambda _, value, *, context: value,
        "print": print_return,
        "store_as": store_as,
        "group_by": group_by,
        "pipeline": special_pipeline,

        # dict
        "keys": lambda value, *, context: list(value.keys()),
        "values": lambda value, *, context: list(value.values()),
        "items": lambda value, *, context: list(value.items()),
        "wildcard": wildcard,
        "value_map": value_map,
        "key_of_min_value": key_of_min_value,
        "key_of_max_value": key_of_max_value,

        # type conversions
        "set": lambda value, *, context: set(value),
        "float": lambda value, *, context: float(value),
        "string": lambda value, *, context: str(value),
        "dict": lambda value, context: dict(value),
        "int": lambda value, *, context: int(value),
        "not": lambda value, *, context: not value,
        "fallback": lambda value, fallback, *, context: value if value and value is not Query.MISSING else fallback,
        "ternary": lambda value, if_true, if_false, strict=False, *, context: if_true if (not strict and value) or (
                strict and value is True) else if_false,

        # datetime
        "parse_timestamp": lambda value, *, context: datetime.utcfromtimestamp(value),
        "strptime": lambda value, fmt=None, *, context: parse_dt_string(value, fmt),
        "timestamp": lambda value, *, context: value.replace(tzinfo=timezone.utc).timestamp(),
        "strftime": lambda value, fmt="%Y-%m-%dT%H:%M:%SZ", *, context: value.strftime(fmt),
        "time_part": time_part,

        # math / numeric
        "add": lambda value, num, *, context: value + num,
        "subtract": lambda value, num, *, context: value - num,
        "multiply": lambda value, num, *, context: value * num,
        "divide": lambda value, num, *, context: value / num,
        "pow": lambda value, num, *, context: value ** num,
        "abs": lambda value, *, context: abs(value),
        "distance": lambda value, other, *, context: math.sqrt(sum((a-b)**2 for a, b in zip(value, other))),
        "math": lambda value, attr, *args, context: getattr(math, attr)(value, *args),
        "round": lambda value, n=2, *, context: round(float(value), n),
        "arith": lambda value, op, arg_value, *, context: Query.MATH_OPERATIONS[op](value, arg_value),

        # string
        "lowercase": lambda value, context: value.lower(),
        "uppercase": lambda value, context: value.upper(),
        "titlecase": lambda value, context: value.title(),
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
        "min": lambda value, *, context: min(value),
        "max": lambda value, *, context: max(value),
        "sum": lambda value, *, context: sum(value),
        "join": lambda value, sep=", ", *, context: sep.join(str(i) for i in value),
        "join_arg": lambda _, arg, sep=', ', *, context: sep.join(str(i) for i in arg),
        "index": index_special,
        "range": lambda value, start, end=None, *, context: value[start: end if end is not None else len(value)],
        "remove_nulls": lambda value, *, context: [v for v in value if v is not None],
        "sort": sort,

        # attribute accessing
        "call": lambda value, func, *args, context, **kwargs: getattr(value, func)(*args, **kwargs),
        "attr": lambda value, attr, *, context: getattr(value, attr),
    }

    SPECIALS["map"] = lambda value, special, *args, context, **kwargs: [
        Query.SPECIALS[special](v, *args, **kwargs, context=context) for v in value
    ]

    def __init__(self,
                 query: Union[str, List[str], JQLQuery, List[JQLQuery]], fallback: any = None,
                 convert_ints: bool = True):
        """
        Create a query object from a JQL query string, or list of JQL query strings.
        :param query: The JQL query string(s)
        :param fallback: A fallback value that will be used if a field cannot be found
        :param convert_ints: Whether to treat digit-only field values as integers or strings
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
                    elif '$' not in f:
                        # if there are no specials, then manually parse
                        p = self._manually_parse(f)
                    else:
                        p = JQLQueryBuilder(f, convert_ints=self.convert_ints).get_built_query()

                    self.parts.append(p)
                except JQLParseError as e:
                    logger.error(e)
                    self.parts.append(None)

        logger.debug(f"got parts: {self.parts}")

    def __repr__(self):
        return f"Query: {self.parts}"

    def _manually_parse(self, query_string: str) -> JQLQuery:
        query = JQLQuery()
        for part in query_string.split('.'):
            field = JQLField()
            field.set_field(part)

            if self.convert_ints:
                try:
                    f = int(part)
                    field.set_field(f)
                except (ValueError, TypeError):
                    pass

            query.add(field)

        return query

    def _query(self, value, query: JQLQuery, context: dict):
        original = value
        for i, part in enumerate(query.parts):
            if isinstance(part, JQLField):
                if value != self.fallback:
                    try:
                        value = value[part.field]
                    except (ValueError, IndexError, TypeError, KeyError):
                        # if this is the base part of a query, then check the current context
                        if i == 0 and part.field in context:
                            value = context[part.field]
                        else:
                            value = self.fallback
            elif isinstance(part, JQLSpecial):
                if part.special in self.SPECIALS:
                    args, kwargs = self._arguments(part.arguments, original, context)
                    value = self.SPECIALS[part.special](
                        value, *args, **kwargs, context=context
                    )
                else:
                    raise SpecialNotFoundError(part.special)

        return value

    def _arguments(self, arguments: List[JQLArgument], value, context: dict) -> Tuple[list, dict]:
        args = []
        kwargs = {}
        for arg in arguments:
            if isinstance(arg, JQLKeywordArgument):
                kwargs[arg.name] = self._value(value, arg.value, context)
            else:
                args.append(self._value(value, arg.value, context))

        return args, kwargs

    def _value(self, value, qve: Union[JQLQuery, JQLValue, JQLExpression], context: dict):
        if isinstance(qve, JQLQuery):
            return self._query(value, qve, context)
        elif isinstance(qve, JQLExpression):
            if qve.second is None:
                return self._value(value, qve.first, context)
            else:
                return self.MATH_OPERATIONS[qve.operator](
                    self._value(value, qve.first, context),
                    self._value(value, qve.second, context)
                )
        elif isinstance(qve, JQLList):
            return [self._value(value, part, context) for part in qve.value]
        elif isinstance(qve, JQLDict):
            return {
                self._value(value, k, context): self._value(value, v, context)
                for k, v in qve.value.items()
            }
        elif isinstance(qve, JQLSet):
            return {self._value(value, part, context) for part in qve.value}
        else:
            return qve.value

    def single(self, item: Any, context: dict = None) -> Union[Any, List[Any]]:
        """
        Query the item
        :param item: The item to query
        :param context: An additional namespace that will be searched if a top-level field name cannot
            be found on the item
        :return: A value, or list of values, depending on whether one or multiple queries are present
        """
        values = []
        for query in self.parts:
            if query is not None:
                values.append(self._query(item, query, {} if context is None else context))
            else:
                values.append(self.fallback)

        return values if self.multiple else values[0]

    def many(self, items: List[Any], context: dict = None) -> Union[List[Any], List[List[Any]]]:
        """
        Query the items
        :param items: The items to query
        :param context: An additional namespace that will be searched if a top-level field name cannot
            be found on an item
        :return: A list of values or a list of lists of values, depending on whether one or multiple queries are present
        """
        return [self.single(item, context) for item in items]

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


QUERY_CACHE: Dict[str, Query] = {}


if __name__ == "__main__":
    print(Query("found.missing", fallback="N/A").single({"found": {}}))
