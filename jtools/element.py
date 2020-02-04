from .base import Base
from typing import Union

__all__ = ["Element"]


class Element(JBase):
    def __init__(self, data: Union[list, dict], meta=None):
        super().__init__(meta)
        self.data = data
