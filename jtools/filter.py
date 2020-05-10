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

    @staticmethod
    def ander(cond1, cond2, *conditions):
        return cond1.clone().and_(cond2, *conditions)

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

    @staticmethod
    def orer(cond1, cond2, *conditions):
        return cond1.clone().or_(cond2, *conditions)

    def __invert__(self):
        self.output = [{"not": self.output}]
        return self

    def not_(self):
        return ~self

    def to_list(self) -> list:
        return self.output

    @staticmethod
    def from_list(conditions):
        condition = Condition("", "", "")
        condition.output = conditions
        return condition

    def clone(self, deep=False):
        condition = Condition("", "", "")
        if deep:
            pass
        else:
            condition.output = [*self.output]

        return condition

    @classmethod
    def _deep_clone(cls, conditions: List[dict]):
        output = []
        for cond in conditions:
            if isinstance(cond, list):
                item = cls._deep_clone(cond)
            elif "or" in cond:
                item = {"or": cls._deep_clone(cond["or"])}
            elif "not" in cond:
                item = {"or": cls._deep_clone(cond["not"])}
            else:
                item = {**cond}

            output.append(item)
        return output

    def traverse(self, callback: callable, on_duplicate=False):
        """
        Traverse/visit every filter in the condition, either on the current condition, or on a deep copy.
        The condition used will be returned, which is either this one, or a duplicate.
        Note, a filter here is of the form { field: ..., operator: ..., value: ... }, ignoring "and", "not", and "or"
        conditions
        :param callback: A function that will be called and passed the current filter in the traversal
        :param on_duplicate:
        """
        condition = self.clone(True) if on_duplicate else self
        filters = [*condition.output]

        i = 0
        while i < len(filters):
            f = filters[i]
            if isinstance(f, list):
                filters.extend(f)
            elif "or" in f:
                filters.extend(f["or"])
            elif "not" in f:
                filters.extend(f["not"])
            else:
                callback(f)

            i += 1
        return filters


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

    def interval(self, *values):
        return Condition(self.field, "interval", values[0] if len(values) == 1 else values)

    def not_interval(self, *values):
        return Condition(self.field, "!interval", values[0] if len(values) == 1 else values)

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
            self.filters = filters.to_list()
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

    def _filter(self, item: Union[dict, list], filters=None, oring=False, context: dict = None) -> bool:
        if filters is None:
            filters = self.filters

        overall = None
        for f in filters:
            if isinstance(f, list):
                c = self._filter(item, f, oring, context)
            elif "or" in f:
                c = self._filter(item, f["or"], True, context)
            elif "not" in f:
                c = not self._filter(item, f["not"], oring, context)
            else:
                query_result = self.queries[f["field"]].single(item, context)
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

    def single(self, item, context: dict = None) -> bool:
        """
        Filter a single item
        :param item: The item to filter
        :param context: An additional namespace that will be searched if a top-level field name cannot
            be found on the item
        :return: Whether or not the item meets the filter
        """
        return self._filter(item, None, False, {} if context is None else context)

    def many(self, items: List[any], context: dict = None) -> List[any]:
        """
        Filter the list of items. Adds 'INDEX' to the query space which is the 0-base index of the item being filtered
        :param items: The items to filter
        :param context: An additional namespace that will be searched if a top-level field name cannot
            be found on the item
        :return: Only the items that satisfy the filter
        """
        return [
            item for index, item in enumerate(items)
            if self._filter(item, None, False, {"INDEX": index, **({} if context is None else context)})
        ]


if __name__ == "__main__":
    pass
