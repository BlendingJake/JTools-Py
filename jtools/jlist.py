from .jbase import JBase
from .jelement import JElement
from typing import List, Union, Optional

__all__ = ["JList"]


class JList(JBase):
    def __init__(self, meta: dict = None):
        super().__init__(meta)
        self._elements: Union[List[JList], List[JElement]] = []

    def __iter__(self):
        for e in self.elements():
            yield e

    def elements(self, new: list = None, axis: int = 0) -> Optional[list]:
        if axis == 0:
            if new is None:
                return self._elements
            else:
                self._elements = new
        else:
            results = []
            for e in self._elements:
                if isinstance(e, JList):
                    result = e.elements(new, axis-1)

                    if new is not None:
                        results.extend(result)

            return results
