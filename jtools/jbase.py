from typing import Callable, Dict, List, Union, Optional
from .getter import Getter
from .setter import Setter
from uuid import uuid4

__all__ = ["JBase"]
MISSING = object()


class Hook:
    def __init__(self, callback: Callable, priority: int = 100):
        self.callback = callback
        self.priority = priority
        self.id = str(uuid4())

    def __lt__(self, other):
        return isinstance(other, Hook) and self.priority < other.priority

    def call(self, instance):
        self.callback(instance)


class JBase:
    def __init__(self, meta: dict = None):
        if meta is None:
            self.meta = {}
        else:
            self.meta = meta

        self.hooks: Dict[str, Hook] = {}
        self.ordered_hooks: List[Hook] = []

    def _sort_hooks(self):
        self.ordered_hooks = sorted(self.hooks.values())

    def hook(self, callback: Callable, priority: int = 100) -> str:
        """
        Hook a function to updates to this base object. The new instance of the object
        will be passed as the sole argument to the function.
        :param callback:
        :param priority:
        :return The ID of the new hook instance
        """
        h = Hook(callback, priority)
        self.hooks[h.id] = h
        self._sort_hooks()

        return h.id

    def unhook(self, hook_id: str):
        if hook_id in self.hooks:
            del self.hooks[hook_id]
            self._sort_hooks()

    def propagate(self, instance):
        for h in self.ordered_hooks:
            h.call(instance)

    def prop(self, field: Union[str, Getter, Setter], value=MISSING) -> Optional:
        """
        Get or set a meta property.
        :param field: `str` or `Getter` if getting, otherwise `str` or `Setter`
        :param value: The new value for the property
        :return:
        """
        if value is MISSING:
            if isinstance(field, str):
                return Getter(field).single(self.meta)
            elif isinstance(field, Getter):
                return field.single(self.meta)
        else:
            if isinstance(field, str):
                Setter(field).set(self.meta, value)
            elif isinstance(field, Setter):
                field.set(self.meta, value)
