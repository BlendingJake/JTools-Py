from .query import Query
from .grammar import JQLParseError, JQLMultiQueryBuilder, JQLMultiQuery, JQLQuery
from typing import List, Optional
import logging
from os import environ

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("JTOOLS_LOGGING_LEVEL", "WARNING"))

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
    def __init__(self, spec: str, fallback: str = "<missing>", convert_ints: bool = True):
        """
        Create a new Formatter for a spec string which can contain multiple JQL queries, prefixed with '@',
        which will be used to format the output string(s).
        :param spec: The specification string
        :param fallback: The value that will replace any query that could not be performed
        :param convert_ints: Whether to convert any digit-only strings to integers or not
        """
        self.fallback: str = fallback
        self.convert_ints: bool = convert_ints
        self.spec: str = spec
        self.multi_query: Optional[JQLMultiQuery] = None

        try:
            mq = JQLMultiQueryBuilder(self.spec, convert_ints).get_built_query()
            self.multi_query = mq
        except JQLParseError:
            self.multi_query = None

    def _format(self, mq: JQLMultiQuery, item, context: dict) -> str:
        if mq is None:
            return self.fallback
        else:
            output = []
            for part in mq.queries:
                if isinstance(part, JQLQuery):
                    v = Query(part, convert_ints=self.convert_ints, fallback=Query.MISSING).single(item, context)
                else:
                    v = part.text.replace("@@", "@")

                if v is Query.MISSING:
                    output.append(self.fallback)
                else:
                    output.append(v)

            return "".join(str(p) for p in output)

    def single(self, item: any, context: dict = None) -> str:
        """
        Format a single item
        :param item: The item to format
        :param context: An additional namespace that will be searched if a top-level field name cannot
            be found on the item
        :return: The formatted string
        """
        return self._format(self.multi_query, item, context)

    def many(self, items: List[any], context: dict = None) -> List[str]:
        """
        Format a list of items
        :param items: The items to format
        :param context: An additional namespace that will be searched if a top-level field name cannot
            be found on the item
        :return: A list of formatted strings
        """
        return [self.single(item, context) for item in items]


if __name__ == "__main__":
    test = {"env": {"VERSION": "1.0.0"}}
    print(Formatter("build/@env.VERSION").single(test))
