from .getter import Getter
import re
from typing import Union, List
import logging
from os import environ
import json

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("LOGGING_LEVEL", "INFO"))

__all__ = ["Formatter"]


class Formatter:
    _full_replacement = r"{{\s*" + Getter.full_regex() + r"\s*}}"
    _replacement_pattern = re.compile(_full_replacement)
    MISSING = object()

    logger.debug(f"Full Replacement: {_full_replacement}")

    def __init__(self, spec: str, fallback: any = None):
        self.fallback = fallback
        self.failed = False
        self.spec = spec

    def single(self, item: Union[list, dict]) -> Union[str, any]:
        return self._replace(self.spec, item)

    def many(self, items: List[Union[list, dict]]) -> List[Union[str, any]]:
        return [self.single(item) for item in items]

    def _replace(self, spec: str, item: Union[list, dict]) -> str:
        logger.debug(f"starting with {spec}")
        updated = self._replacement_pattern.sub(lambda match: self._replacer(match, item), spec)
        logger.debug(f"after replacement {updated}")

        if self.failed:
            return self.fallback
        else:
            if updated != spec:  # we changed stuff
                return self._replace(updated, item)
            else:
                return updated

    def _replacer(self, match, item: Union[list, dict]) -> str:
        groups = match.groups()
        field = groups[0]
        if groups[2]:
            field += groups[2]

        result = Getter(field, fallback=self.MISSING).single(item)
        logger.debug(f"field: {field}, got: {result}")
        if result is self.MISSING:
            self.failed = True
            return ""
        else:
            if isinstance(result, (list, dict)):
                return json.dumps(result)
            else:
                return str(result)


if __name__ == "__main__":
    test = {"env": {"VERSION": "1.0.0"}}
    print(Formatter("build/{{env.VERSION}}").single(test))
