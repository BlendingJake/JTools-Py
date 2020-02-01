from .jbase import JBase
from typing import Union

__all__ = ["JElement"]


class JElement(JBase):
    def __init__(self, data: Union[list, dict], meta=None):
        super().__init__(meta)
        self.data = data
