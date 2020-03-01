from typing import List, Type, Union
from antlr4 import *
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import InputMismatchException
from .QUERYLexer import QUERYLexer
from .QUERYParser import QUERYParser
from .QUERYListener import QUERYListener
import logging
from os import environ

logging.basicConfig(format='%(levelname)s:%(module)s:%(funcName)s:%(lineno)d}: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("JTOOLS:GRAMMAR:QUERY:LOGGING_LEVEL", "INFO"))

__all__ = ['QueryBuilder', 'QueryParseError', 'MultiQueryBuilder', "MultiQuery", "RawInput",
           "Query", "Field", "Special", "ListValue", "SetValue", "DictValue", "Value"]


class Value:
    def __init__(self):
        self.parent = None
        self.value = None

    def __repr__(self):
        return f"<Value: value={repr(self.value)}>"

    def add(self, value):
        pass

    def get_value(self):
        return self.value


class ListValue(Value):
    def __init__(self):
        super().__init__()
        self.value = []

    def __repr__(self):
        return f"<List values={self.value}>"

    def add(self, value):
        self.value.append(value)

    def get_value(self):
        return [value.get_value() for value in self.value]


class SetValue(Value):
    def __init__(self):
        super().__init__()
        self.value = set()

    def __repr__(self):
        return f"<Set values={self.value}>"

    def add(self, value):
        self.value.add(value)

    def get_value(self):
        return {value.get_value() for value in self.value}


class DictValue(Value):
    MISSING = object()

    def __init__(self):
        super().__init__()
        self.value = {}
        self.key = self.MISSING

    def __repr__(self):
        return f"<Dict values={self.value}>"

    def add(self, value):
        if self.key is self.MISSING:
            self.key = value
        else:
            self.value[self.key] = value
            self.key = self.MISSING

    def get_value(self):
        return {key: value.get_value() for key, value in self.value.items()}


class Part:
    def get_value(self):
        pass


class Field(Part):
    def __init__(self):
        self.field = None

    def __repr__(self):
        return f"<Field '{self.field}'>"

    def set_field(self, field: Union[str, int]):
        self.field = field

    def get_value(self):
        return self.field


class Special(Part):
    def __init__(self):
        self.special = None
        self.arguments = []

    def __repr__(self):
        return f"<Special '{self.special}' args={self.arguments}>"

    def set_special(self, special: str):
        self.special = special

    def add(self, argument):
        self.arguments.append(argument)

    def get_value(self):
        return {
            "special": self.special,
            "arguments": [arg.get_value() for arg in self.arguments]
        }


class Query:
    def __init__(self):
        self.parent = None
        self.parts: List[Part] = []

    def __repr__(self):
        return f"<Query parts={self.parts}>"

    def add(self, part: Part):
        self.parts.append(part)

    def last(self):
        return self.parts[-1]

    def get_value(self):
        return [part.get_value() for part in self.parts]


class RawInput:
    def __init__(self):
        self.text = None

    def set_text(self, text: str):
        self.text = text


class MultiQuery:
    def __init__(self):
        self.queries: List[Union[Query, RawInput]] = []

    def add(self, query):
        self.queries.append(query)


class QueryListener(QUERYListener):
    def __init__(self, convert_ints=True):
        self.stack = []
        self.convert_ints = convert_ints
        self.root = None

    def enterQuery(self, ctx: QUERYParser.QueryContext):
        q = Query()
        if self.stack:  # have stuff on the stack, so this must be a value or argument
            self.stack[-1].add(q)
        else:
            self.root = q

        self.stack.append(q)
        logger.debug(self.stack)

    def exitQuery(self, ctx: QUERYParser.QueryContext):
        self.stack.pop()
        logger.debug(self.stack)

    def exitQuery_field(self, ctx: QUERYParser.Query_fieldContext):
        f = Field()
        f.set_field(ctx.getText())

        if self.convert_ints:
            try:
                fi = int(f.field)
                f.set_field(fi)
            except ValueError:
                pass

        self.stack[-1].add(f)
        logger.debug(self.stack)

    def enterSpecial(self, ctx: QUERYParser.SpecialContext):
        s = Special()
        self.stack[-1].add(s)
        self.stack.append(s)
        logger.debug(self.stack)

    def exitSpecial(self, ctx: QUERYParser.SpecialContext):
        self.stack.pop()
        logger.debug(self.stack)

    def exitSpecial_name(self, ctx: QUERYParser.Special_nameContext):
        self.stack[-1].set_special(ctx.getText())
        logger.debug(self.stack)

    def enterList_value(self, ctx: QUERYParser.List_valueContext):
        self.enter_value(ListValue)

    def enterSet_value(self, ctx: QUERYParser.Set_valueContext):
        self.enter_value(SetValue)

    def enterObject_value(self, ctx: QUERYParser.Object_valueContext):
        self.enter_value(DictValue)

    def exitKey(self, ctx: QUERYParser.KeyContext):
        txt = ctx.getText()
        if txt[0] != '@':  # query will add itself
            v = Value()
            v.value = self.parse_primitive(ctx.getText())
            self.stack[-1].add(v)
        logger.debug(self.stack)

    def exitValue(self, ctx: QUERYParser.ValueContext):
        # 2 types of values we can have - primitive or already parsed value
        text = ctx.getText()
        if text[0] in ("[", "{"):
            self.stack.pop()
        elif text[0] != "@":  # query will pop itself on exitQuery
            val = Value()
            val.value = self.parse_primitive(text)
            self.stack[-1].add(val)
        logger.debug(self.stack)

    # helpers
    @classmethod
    def parse_primitive(cls, text):
        if text[0] == '"' or text[0] == "'":
            value = text[1:-1]
        elif text == "true":
            value = True
        elif text == "false":
            value = False
        elif text == "null":
            value = None
        elif "." in text:
            value = float(text)
        else:
            value = int(text)

        return value

    def enter_value(self, cls: Type[Value]):
        v = cls()
        self.stack[-1].add(v)
        self.stack.append(v)
        logger.debug(self.stack)


class MultiQueryListener(QueryListener):
    def __init__(self, convert_ints=True):
        super().__init__(convert_ints)

    def enterMulti_query(self, ctx: QUERYParser.Multi_queryContext):
        self.root = MultiQuery()
        self.stack.append(self.root)

    def exitMulti_query(self, ctx: QUERYParser.Multi_queryContext):
        self.stack.pop()

    def exitRaw_text(self, ctx: QUERYParser.Raw_textContext):
        raw = RawInput()
        raw.set_text(ctx.getText())
        self.stack[-1].add(raw)


class QueryParseError(Exception):
    def __init__(self, e):
        super().__init__(e)


class ParserErrorStrategy(DefaultErrorStrategy):
    def reportError(self, recognizer: Parser, e: RecognitionException):
        if isinstance(e, InputMismatchException):
            raise QueryParseError(str(e))
        else:
            super().reportError(recognizer, e)


class Builder:
    def __init__(self, text: str, convert_ints=True):
        self.convert_ints = convert_ints
        self.text = text

        self.input_stream = InputStream(self.text)
        self.lexer = QUERYLexer(self.input_stream)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = QUERYParser(self.stream)
        self.parser._errHandler = ParserErrorStrategy()


class QueryBuilder(Builder):
    def __init__(self, text: str, convert_ints=True):
        super().__init__(text, convert_ints)

        self.tree = self.parser.query()
        self.printer = QueryListener(convert_ints=self.convert_ints)
        self.walker = ParseTreeWalker()
        self.walker.walk(self.printer, self.tree)

        logger.debug(self.printer.root)

    def get_built_query(self) -> Query:
        return self.printer.root


class MultiQueryBuilder(Builder):
    def __init__(self, text: str, convert_ints=True):
        super().__init__(text, convert_ints)

        self.tree = self.parser.multi_query()
        self.printer = MultiQueryListener(convert_ints=self.convert_ints)
        self.walker = ParseTreeWalker()
        self.walker.walk(self.printer, self.tree)

        logger.debug(self.printer.root)

    def get_built_query(self) -> MultiQuery:
        return self.printer.root


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)

    QueryBuilder("tests")
    QueryBuilder("tests.test")
    QueryBuilder("tests.$wrap")
    QueryBuilder("$wrap")
    QueryBuilder("$wrap.text")
    QueryBuilder("$wrap(5)")
    QueryBuilder("$wrap('5')")
    QueryBuilder('$wrap("5")')
    QueryBuilder('$wrap(-4.5)')
    QueryBuilder('$wrap([], {}, {:}, true, false, null, "true")')
    QueryBuilder('$wrap([1, 2], {3, "4"}, {4: 5, "true": false})')
    QueryBuilder('$wrap(@prefix, [5, @prefix])')
    QueryBuilder('$wrap(@prefix, [5, @prefix.$sum, @prefix.$join(", ")])')
    QueryBuilder('$wrap({@prefix: "john", @prefix: @prefix, "john": @prefix})')

    MultiQueryBuilder("@tests.test something else @tests.$wrap")
