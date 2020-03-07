from .query import Query
from .grammar import JQLParseError, JQLMultiQueryBuilder, JQLMultiQuery, JQLQuery
from typing import Union, List
import logging
from os import environ

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("LOGGING_LEVEL", "INFO"))

__all__ = ["Formatter"]


class Formatter:
    """
    Formatter allows the advanced query capabilities of Query to be interpolated right into string
    outputs. A format query string supports multiple query strings that will be replaced.
    Each query string should be prefixed with '@' like is required for nesting queries.

    Example:
    data = {
        "name": "John Smith",
        "DOB": "11/25/1987"
    }
    Formatter("Name: @name and DOB: @DOB").single(data)  # 'Name: John Smith and DOB: 11/25/198'
    """
    MISSING = object()

    def __init__(self, spec: str, fallback: any = None, convert_ints: bool = True):
        self.fallback = fallback
        self.convert_ints = convert_ints
        self.spec = spec
        self.multi_query = None

        try:
            mq = JQLMultiQueryBuilder(self.spec, convert_ints).get_built_query()
            self.multi_query = mq
        except JQLParseError:
            pass

    def single(self, item: Union[list, dict]) -> Union[str, any]:
        return self._format(self.multi_query, item)

    def many(self, items: List[Union[list, dict]]) -> List[Union[str, any]]:
        return [self.single(item) for item in items]

    def _format(self, mq: JQLMultiQuery, item):
        if mq is None:
            return self.fallback
        else:
            output = []
            for part in mq.queries:
                if isinstance(part, JQLQuery):
                    v = Query(part, self.convert_ints, self.MISSING).single(item)
                else:
                    v = part.text.replace("@@", "@")

                if v is self.MISSING:
                    return self.fallback
                else:
                    output.append(v)

            return "".join(str(p) for p in output)


if __name__ == "__main__":
    test = {"env": {"VERSION": "1.0.0"}}
    print(Formatter("build/{{env.VERSION}}").single(test))
