from field_getter import FieldGetter
import re
from typing import Union, Dict, Callable
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

__all__ = ["FieldFormatter"]


class FieldFormatter:
    _full_replacement = r"(?!\\){\s*" + FieldGetter.full_regex() + r"\s*(?<!\\)}"
    _replacement_pattern = re.compile(_full_replacement)

    logger.debug(f"Full Replacement: {_full_replacement}")

    _transformers: Dict[str, Callable] = {

    }

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

        return str(FieldGetter(field).get(item))


if __name__ == "__main__":
    import json

    # mock data from https://www.sitepoint.com/test-data-json-example/
    with open("./test_data.json") as file:
        test = json.loads(file.read())

    single = {
        "a": {
            "Process Error": "Ralph",
            "Micro Error": "Barb"
        },
        "b": [4, 6],
        "c": 3
    }

    FieldGetter.register_special("adder", lambda value, *args: value + sum(args))
    print(FieldFormatter('{a.$items.$map("join", ": \\n\\t").$join("\\n")}').format(single))
