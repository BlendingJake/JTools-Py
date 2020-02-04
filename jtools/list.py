from .base import Base
from .element import Element
from .filter import Filter, Condition
from typing import List as OGList, Union, Optional

__all__ = ["List"]


class List(Base):
    def __init__(self, meta: dict = None):
        super().__init__(meta)
        self._elements: Union[OGList[List], OGList[Element]] = []

    def __iter__(self):
        for e in self.elements():
            yield e

    def _propagate(self, propagate=True):
        if propagate:
            super().propagate(self._elements)

    def elements(self, new: list = None, axis: int = 0, propagate: bool = True) -> Optional[list]:
        if axis == 0:
            if new is None:
                return self._elements
            else:
                self._elements = new
                self._propagate(propagate)
        else:
            results = []
            for e in self._elements:
                if isinstance(e, List):
                    result = e.elements(new, axis-1)

                    if new is not None:
                        results.extend(result)

            return results

    def filter(self, filters: Union[list, Condition, Filter], axis: int = 0, propagate: bool = True):
        pass
