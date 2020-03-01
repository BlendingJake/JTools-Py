from .query import Query
from .grammar import QueryParseError, MultiQueryBuilder, MultiQuery, Query as QueryPart
from typing import Union, List
import logging
from os import environ

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("LOGGING_LEVEL", "INFO"))

__all__ = ["Formatter"]


class Formatter:
    MISSING = object()

    def __init__(self, spec: str, fallback: any = None, convert_ints: bool = True):
        self.fallback = fallback
        self.convert_ints = convert_ints
        self.spec = spec
        self.multi_query = None

        try:
            mq = MultiQueryBuilder(self.spec, convert_ints).get_built_query()
            self.multi_query = mq
        except QueryParseError:
            pass

    def single(self, item: Union[list, dict]) -> Union[str, any]:
        return self._format(self.multi_query, item)

    def many(self, items: List[Union[list, dict]]) -> List[Union[str, any]]:
        return [self.single(item) for item in items]

    def _format(self, mq: MultiQuery, item):
        if mq is None:
            return self.fallback
        else:
            output = []
            for part in mq.queries:
                if isinstance(part, QueryPart):
                    v = Query(part, self.convert_ints, self.MISSING).single(item)
                else:
                    v = part.text

                if v is self.MISSING:
                    return self.fallback
                else:
                    output.append(v)

            return "".join(str(p) for p in output)


if __name__ == "__main__":
    test = {"env": {"VERSION": "1.0.0"}}
    print(Formatter("build/{{env.VERSION}}").single(test))
