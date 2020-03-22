from typing import Union, List, Dict, Any
from .query import Query
import logging
from os import environ

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("JTOOLS_LOGGING_LEVEL", "WARNING"))

__all__ = ["Condition", "Key", "Filter"]


class Condition:
    """
    Key conditions AND and OR can be performed with this class.
    """
    def __init__(self, field: str, operator: str, value: Any):
        self.output: List[dict] = [{"field": field, "operator": operator, "value": value}]

    def __repr__(self):
        return str(self.output)

    def __and__(self, other):
        self.output.extend(other.output)
        return self

    def and_(self, *args):
        val = self
        for a in args:
            val = val & a

        return val

    def __or__(self, other):
        t = []
        for l in (self, other):
            if len(l.output) == 1:
                if "or" in l.output[0]:
                    t.extend(l.output[0]["or"])
                else:
                    t.append(l.output[0])
            else:
                t.append(l.output)

        self.output = [{"or": t}]
        return self

    def or_(self, *args):
        val = self
        for a in args:
            val = val | a

        return val

    def __invert__(self):
        self.output = [{"not": self.output}]
        return self

    def not_(self):
        return ~self

    def filters(self) -> List[dict]:
        return self.output


class ValueLessCondition:
    def __init__(self, field: str, op: str):
        self.field = field
        self.op = op

    def value(self, value: any) -> Condition:
        return Condition(self.field, self.op, value)


class Key:
    def __init__(self, field: str):
        self.field = field

    def __gt__(self, other):
        return Condition(self.field, ">", other)

    def gt(self, other):
        return self > other

    def __lt__(self, other):
        return Condition(self.field, "<", other)

    def lt(self, other):
        return self < other

    def __ge__(self, other):
        return Condition(self.field, ">=", other)

    def gte(self, other):
        return self >= other

    def __le__(self, other):
        return Condition(self.field, "<=", other)

    def lte(self, other):
        return self <= other

    def __eq__(self, other):
        return Condition(self.field, "==", other)

    def eq(self, other):
        return self == other

    def __ne__(self, other):
        return Condition(self.field, "!=", other)

    def ne(self, other):
        return self != other

    def seq(self, other):
        return Condition(self.field, "===", other)

    def sne(self, other):
        return Condition(self.field, "!==", other)

    def in_(self, other):
        return Condition(self.field, "in", other)

    def nin(self, other):
        return Condition(self.field, "!in", other)

    def contains(self, other):
        return Condition(self.field, "contains", other)

    def not_contains(self, other):
        return Condition(self.field, "!contains", other)

    def interval(self, other):
        return Condition(self.field, "interval", other)

    def not_interval(self, other):
        return Condition(self.field, "!interval", other)

    def startswith(self, other):
        return Condition(self.field, "startswith", other)

    def endswith(self, other):
        return Condition(self.field, "endswith", other)

    def present(self):
        return Condition(self.field, "present", None)

    def not_present(self):
        return Condition(self.field, "!present", None)

    def operator(self, op: str) -> ValueLessCondition:
        return ValueLessCondition(self.field, op)


class Filter:
    MISSING = object()

    _filters = {
        ">": lambda field, value: field > value,
        "<": lambda field, value: field < value,
        ">=": lambda field, value: field >= value,
        "<=": lambda field, value: field <= value,
        "==": lambda field, value: field == value,
        "!=": lambda field, value: field != value,
        "===": lambda field, value: field == value,
        "!==": lambda field, value: field != value,

        "in": lambda field, value: field in value,
        "!in": lambda field, value: field not in value,
        "contains": lambda field, value: value in field,
        "!contains": lambda field, value: value not in field,

        "interval": lambda field, value: value[0] <= field <= value[1],
        "!interval": lambda field, value: field < value[0] or value[1] < field,

        "startswith": lambda field, value: field.startswith(value),
        "endswith": lambda field, value: field.endswith(value),

        "present": lambda field, _: field is not Filter.MISSING,
        "!present": lambda field, _: field is Filter.MISSING,
    }

    def __init__(self, filters: Union[Condition, List[dict]], convert_ints: bool = True,
                 empty_filters_response: bool = True, missing_field_response: bool = False):
        """
        Prepare a filter object from a list of filters, or from a condition object
        :param filters: The filters
        :param convert_ints: Whether to convert digit-only strings to integers or not
        :param empty_filters_response: What is returned if there are no filters. Makes the difference between
            returning all items for empty filters, or returning none.
        :param missing_field_response: What is returned for a filter if the field was not present.
        """
        self.empty_filters_response = empty_filters_response
        self.missing_field_response = missing_field_response

        if isinstance(filters, Condition):
            self.filters = filters.filters()
        else:
            self.filters = filters

        logger.debug(filters)
        self.queries = self._preprocess(self.filters, convert_ints)
        logger.debug(self.queries)

    def _preprocess(self, filters, convert_ints=True) -> Dict[str, Query]:
        out = {}
        for f in filters:
            if isinstance(f, list):
                out.update(self._preprocess(f, convert_ints))
            elif "or" in f:
                out.update(self._preprocess(f["or"], convert_ints))
            elif "not" in f:
                out.update(self._preprocess(f["not"], convert_ints))
            elif f["field"] not in out:
                out[f["field"]] = Query(f["field"], fallback=self.MISSING, convert_ints=convert_ints)

        return out

    def _filter(self, item: Union[dict, list], filters=None, oring=False) -> bool:
        if filters is None:
            filters = self.filters

        overall = None
        for f in filters:
            if isinstance(f, list):
                c = self._filter(item, f)
            elif "or" in f:
                c = self._filter(item, f["or"], True)
            elif "not" in f:
                c = not self._filter(item, f["not"])
            else:
                query_result = self.queries[f["field"]].single(item)
                if query_result is self.MISSING and f["operator"] not in ("present", "!present"):
                    c = self.missing_field_response
                else:
                    c = self._filters[f["operator"]](query_result, f["value"])

            if overall is None:
                overall = c
            elif "or" in f or oring:
                overall = c or overall

                if overall:  # shortcut or
                    return True
            else:
                overall = c and overall

                if not overall:  # shortcut and
                    return False

        return self.empty_filters_response if overall is None else overall

    def single(self, item) -> bool:
        """
        Filter a single item
        :param item: The item to filter
        :return: Whether or not the item meets the filter
        """
        return self._filter(item)

    def many(self, items: List[any]) -> List[any]:
        """
        Filter the list of items
        :param items: The items to filter
        :return: Only the items that satisfy the filter
        """
        return [
            item for item in items if self._filter(item)
        ]


if __name__ == "__main__":
    pass
