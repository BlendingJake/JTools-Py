from .getter import Getter
import re
from typing import Union
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

    logger.debug(f"Full Replacement: {_full_replacement}")

    def __init__(self, spec: str):
        self.spec = spec

    def format(self, item: Union[list, dict]) -> str:
        return self._replace(self.spec, item)

    def _replace(self, spec: str, item: Union[list, dict]) -> str:
        updated = self._replacement_pattern.sub(lambda match: self._replacer(match, item), spec)

        if updated != spec:  # we changed stuff
            return self._replace(updated, item)
        else:
            return updated

    @classmethod
    def _replacer(cls, match, item: Union[list, dict]) -> str:
        """
        field[:t][|fallback]
        """
        groups = match.groups()
        field = groups[0]
        if groups[1]:
            field += groups[1]

        result = Getter(field).get(item)
        logger.debug(f"field: {field}, got: {result}")
        if isinstance(result, (list, dict)):
            return json.dumps(result)
        else:
            return str(result)


if __name__ == "__main__":
    item = {"email": "john_doe@gmail.com"}

    print(Formatter("Balance: ${{balance.$subtract({{pending_charges}})}}").format({"balance": 1000, "pending_charges": 250}))
