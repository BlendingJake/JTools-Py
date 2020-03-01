from typing import List, Type
from antlr4 import *
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import InputMismatchException

from QUERYLexer import QUERYLexer
from QUERYParser import QUERYParser
from QUERYListener import QUERYListener
import logging
from os import environ

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("JTOOLS:GRAMMAR:QUERY:LOGGING_LEVEL", "INFO"))

__all__ = ['QueryBuilder', 'QueryParseError']


class Part:
    pass


class Value:
    def __init__(self):
        self.parent = None
        self.value = None

    def __repr__(self):
        return f"<Value: value={self.value} type={type(self.value)}>"

    def add_value(self, value):
        pass

    def get_value(self):
        return self.value


class ListValue(Value):
    def __init__(self):
        super().__init__()
        self.value = []

    def __repr__(self):
        return f"<List values={self.value}>"

    def add_value(self, value):
        self.value.append(value)

    def get_value(self):
        return [value.get_value() for value in self.value]


class SetValue(Value):
    def __init__(self):
        super().__init__()
        self.value = set()

    def __repr__(self):
        return f"<Set values={self.value}>"

    def add_value(self, value):
        self.value.add(value)

    def get_value(self):
        return {value.get_value() for value in self.value}


class DictValue(Value):
    def __init__(self):
        super().__init__()
        self.value = {}
        self.key = None

    def __repr__(self):
        return f"<Dict values={self.value}>"

    def add_key(self, key):
        self.key = key

    def add_value(self, value):
        self.value[self.key] = value

    def get_value(self):
        return {key: value.get_value() for key, value in self.value.items()}


class Field(Part):
    def __init__(self):
        logger.debug("creating field...")
        self.field = None

    def __repr__(self):
        return f"<Field '{self.field}'>"

    def set_field(self, field: str):
        logger.debug(f"field is: {field}")
        self.field = field


class Special(Part):
    def __init__(self):
        logger.debug("creating special...")
        self.special = None
        self.arguments = []

        self.value = None

    def __repr__(self):
        return f"<Special '{self.special}' args={self.arguments}>"

    def set_special(self, special: str):
        logger.debug(f"special is: {special}")
        self.special = special

    def add_argument(self, argument):
        logger.debug(f"adding argument: {argument}")
        self.arguments.append(argument)


class Query:
    def __init__(self):
        logger.debug("creating query...")
        self.parent = None
        self.parts: List[Part] = []

    def __repr__(self):
        return f"<Query parts={self.parts}>"

    def add(self, part: Part):
        logger.debug(f"adding part: {part}")
        self.parts.append(part)

    def last(self):
        return self.parts[-1]


class QueryListener(QUERYListener):
    def __init__(self):
        self.root = None
        self.current = self.root

    def enterQuery(self, ctx: QUERYParser.QueryContext):
        if self.root is None:
            self.root = Query()
            self.current = self.root
        else:
            self.current = Query()
            self.current.parent = self.root
            self.root.last().add_argument(self.current)

    def exitQuery(self, ctx: QUERYParser.QueryContext):
        logger.debug(f"exiting query: {self.current}")
        if self.current.parent is not None:
            self.current = self.current.parent

    def exitQuery_field(self, ctx: QUERYParser.Query_fieldContext):
        f = Field()
        f.set_field(ctx.getText())
        self.current.add(f)

    def enterSpecial(self, ctx: QUERYParser.SpecialContext):
        self.current.add(Special())

    def exitSpecial_name(self, ctx: QUERYParser.Special_nameContext):
        self.current.last().set_special(ctx.getText())

    def enterList_value(self, ctx: QUERYParser.List_valueContext):
        self.enter_value(ListValue)

    def enterSet_value(self, ctx: QUERYParser.Set_valueContext):
        self.enter_value(SetValue)

    def enterObject_value(self, ctx: QUERYParser.Object_valueContext):
        self.enter_value(DictValue)

    def exitKey(self, ctx: QUERYParser.KeyContext):
        self.last_value().add_key(self.parse_primitive(ctx.getText()))

    def exitValue(self, ctx: QUERYParser.ValueContext):
        text = ctx.getText()
        if text[0] not in ("[", "{"):
            value = Value()
            value.value = self.parse_primitive(text)

            if self.last_value() is None:
                self.last().add_argument(value)
            else:
                self.last_value().add_value(value)
        else:
            logger.debug(f"exiting with value: {self.last_value().get_value()}")
            if self.last_value().parent is None:
                self.last().add_argument(self.last_value())
                self.last().value = None
            else:
                self.last().value = self.last_value().parent

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

    def last(self):
        return self.current.last()

    def last_value(self):
        return self.last().value

    def enter_value(self, cls: Type[Value]):
        if self.current.last().value is None:
            self.current.last().value = cls()
        else:
            v = cls()
            v.parent = self.current.last().value

            self.current.last().value.add_value(v)
            self.current.last().value = v


class QueryParseError(Exception):
    def __init__(self, e):
        super().__init__(e)


class ParserErrorStrategy(DefaultErrorStrategy):
    def reportError(self, recognizer: Parser, e: RecognitionException):
        if isinstance(e, InputMismatchException):
            raise QueryParseError(str(e))
            return
        else:
            super().reportError(recognizer, e)


class QueryBuilder:
    def __init__(self, query: str, convert_ints=True):
        self.convert_ints = convert_ints
        self.query = query
        self.input_stream = InputStream(self.query)
        self.lexer = QUERYLexer(self.input_stream)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = QUERYParser(self.stream)
        self.parser._errHandler = ParserErrorStrategy()
        self.tree = self.parser.query()

        self.printer = QueryListener()
        self.walker = ParseTreeWalker()
        self.walker.walk(self.printer, self.tree)

        self.parsed_query = self.simplify_query(self.printer.root)

    def get_build_query(self) -> dict:
        return self.parsed_query

    def simplify_query(self, query: Query) -> dict:
        data = {
            "type": "query",
            "parts": []
        }

        for part in query.parts:
            if isinstance(part, Field):
                field = part.field

                if self.convert_ints:
                    try:
                        fi = int(field)
                        field = fi
                    except ValueError:
                        pass

                data["parts"].append({
                    "type": "field",
                    "field": field
                })
            elif isinstance(part, Special):
                data["parts"].append(self.simplify_special(part))

        return data

    def simplify_special(self, special: Special) -> dict:
        data = {
            "type": "special",
            "special": special.special,
            "arguments": []
        }

        for arg in special.arguments:
            if isinstance(arg, Query):
                data["arguments"].append(self.simplify_query(arg))
            else:
                data["arguments"].append({
                    "type": "value",
                    "value": arg.get_value()
                })

        return data
