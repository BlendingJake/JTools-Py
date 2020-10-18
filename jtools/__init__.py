from typing import Dict
from .query import Query, SpecialNotFoundError
from .filter import Key, Condition, Filter
from .formatter import Formatter

FILTER_CACHE: Dict[str, Filter] = {}
__all__ = [
    "Query", "Key", "Condition", "Filter", "Formatter", "SpecialNotFoundError",
    "__version__"
]
__version__ = "2.0.0"


def filter_special(value, *args, single=True, context):
    if len(args) == 3:
        f = [{"field": args[0], "operator": args[1], "value": args[2]}]
    elif isinstance(args[0], dict):
        f = [args[0]]
    else:
        f = args[0]

    key = str(f)
    if key in FILTER_CACHE:
        filterer = FILTER_CACHE[key]
    else:
        filterer = Filter(f)
        FILTER_CACHE[key] = filterer

    if single:
        return filterer.single(value, context=context)
    else:
        return filterer.many(value, context=context)


if "filter" not in Query.SPECIALS:
    Query.register_special("filter", filter_special)
