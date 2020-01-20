from typing import Union, List, Dict, Any
from getter import Getter
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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

    def and_(self, other):
        return self & other

    def __or__(self, other):
        temp = []
        for l in (self, other):
            if len(l.output) == 1:
                if "or" in l.output[0]:
                    temp.extend(l.output[0]["or"])
                else:
                    temp.append(l.output[0])
            else:
                temp.append(l.output)

        self.output = [{"or": temp}]
        return self

    def or_(self, other):
        return self | other

    def filters(self) -> List[dict]:
        return self.output


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

    def in_(self, other):
        return Condition(self.field, "in", other)

    def nin(self, other):
        return Condition(self.field, "!in", other)

    def contains(self, other):
        return Condition(self.field, "contains", other)

    def not_contains(self, other):
        return Condition(self.field, "!contains", other)

    def startswith(self, other):
        return Condition(self.field, "startswith", other)

    def endswith(self, other):
        return Condition(self.field, "endswith", other)

    def none(self, other):
        return Condition(self.field, "null", other)

    def not_none(self, other):
        return Condition(self.field, "!null", other)


class Filter:
    _filters = {
        ">": lambda field, value: field > value,
        "<": lambda field, value: field < value,
        ">=": lambda field, value: field >= value,
        "<=": lambda field, value: field <= value,
        "==": lambda field, value: field == value,
        "!=": lambda field, value: field != value,

        "in": lambda field, value: field in value,
        "!in": lambda field, value: field not in value,
        "contains": lambda field, value: value in field,
        "!contains": lambda field, value: value not in field,

        "startswith": lambda field, value: field.startswith(value),
        "endswith": lambda field, value: field.endswith(value),

        "null": lambda field, _: field is None,
        "!null": lambda field, _: field is not None
    }

    def __init__(self, filters: Union[Condition, List[dict]], convert_ints=True):
        if isinstance(filters, Condition):
            self.filters = filters.filters()
        else:
            self.filters = filters

        logger.debug(filters)
        self.getters = self._preprocess(self.filters, convert_ints)
        logger.debug(self.getters)

    def _preprocess(self, filters, convert_ints=True) -> Dict[str, Getter]:
        out = {}
        for f in filters:
            if isinstance(f, list):
                out.update(self._preprocess(f, convert_ints))
            elif "or" in f:
                out.update(self._preprocess(f["or"], convert_ints))
            elif f["field"] not in out:
                out[f["field"]] = Getter(f["field"], convert_ints=convert_ints)

        return out

    def _filter(self, item: Union[dict, list], filters=None, oring=False) -> bool:
        if filters is None:
            filters = self.filters

        overall = None
        for f in filters:
            if isinstance(f, list):
                c = self._filter(item, f)
            else:
                if "or" not in f:
                    c = self._filters[f["operator"]](self.getters[f["field"]].get(item), f["value"])
                else:
                    c = self._filter(item, f["or"], True)

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

        return False if overall is None else overall

    def filter(self, items: List[Union[dict, list]]) -> List[Union[dict, list]]:
        """
        Take a list of items and only return the ones that meet the filter conditions
        """
        return [
            item for item in items if self._filter(item)
        ]

    def filter_single(self, item: Union[dict, list]) -> bool:
        return self._filter(item)


if __name__ == "__main__":
    pass
