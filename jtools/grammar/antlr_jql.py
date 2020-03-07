from typing import Type
from antlr4 import *
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.error.Errors import InputMismatchException
from .JQLLexer import JQLLexer
from .JQLParser import JQLParser
from .JQLListener import JQLListener
from .jql import *
import logging
from os import environ

logging.basicConfig(format='%(levelname)s:%(module)s:%(funcName)s:%(lineno)d}: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(environ.get("JTOOLS:GRAMMAR:QUERY:LOGGING_LEVEL", "INFO"))

__all__ = ['JQLQueryBuilder', 'JQLParseError', 'JQLMultiQueryBuilder']


class JQLQueryListener(JQLListener):
    def __init__(self, convert_ints=True):
        self.stack = []
        self.convert_ints = convert_ints
        self.root = None

    def enterQuery(self, ctx: JQLParser.QueryContext):
        q = JQLQuery()
        if self.stack:  # have stuff on the stack, so this must be a value or argument
            self.stack[-1].add(q)
        else:
            self.root = q

        self.stack.append(q)
        logger.debug(self.stack)

    def exitQuery(self, ctx: JQLParser.QueryContext):
        self.stack.pop()
        logger.debug(self.stack)

    def exitQuery_field(self, ctx: JQLParser.Query_fieldContext):
        f = JQLField()
        f.set_field(ctx.getText())

        if self.convert_ints:
            try:
                fi = int(f.field)
                f.set_field(fi)
            except ValueError:
                pass

        self.stack[-1].add(f)
        logger.debug(self.stack)

    def enterSpecial(self, ctx: JQLParser.SpecialContext):
        s = JQLSpecial()
        self.stack[-1].add(s)
        self.stack.append(s)
        logger.debug(self.stack)

    def exitSpecial(self, ctx: JQLParser.SpecialContext):
        self.stack.pop()
        logger.debug(self.stack)

    def exitSpecial_name(self, ctx: JQLParser.Special_nameContext):
        self.stack[-1].set_special(ctx.getText())
        logger.debug(self.stack)

    def enterList_value(self, ctx: JQLParser.List_valueContext):
        self.enter_value(JQLList)

    def enterSet_value(self, ctx: JQLParser.Set_valueContext):
        self.enter_value(JQLSet)

    def enterObject_value(self, ctx: JQLParser.Object_valueContext):
        self.enter_value(JQLDict)

    def exitKey(self, ctx: JQLParser.KeyContext):
        txt = ctx.getText()
        if txt[0] != '@':  # query will add itself
            v = JQLValue()
            v.value = self.parse_primitive(ctx.getText())
            self.stack[-1].add(v)
        logger.debug(self.stack)

    def exitValue(self, ctx: JQLParser.ValueContext):
        # 2 types of values we can have - primitive or already parsed value
        text = ctx.getText()
        if text[0] in ("[", "{"):
            self.stack.pop()
        elif text[0] != "@":  # query will pop itself on exitQuery
            val = JQLValue()
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

    def enter_value(self, cls: Type[JQLValue]):
        v = cls()
        self.stack[-1].add(v)
        self.stack.append(v)
        logger.debug(self.stack)


class JQLMultiQueryListener(JQLQueryListener):
    def __init__(self, convert_ints=True):
        super().__init__(convert_ints)

    def enterJql_multi_query(self, ctx: JQLParser.Jql_multi_queryContext):
        self.root = JQLMultiQuery()
        self.stack.append(self.root)

    def exitJql_multi_query(self, ctx: JQLParser.Jql_multi_queryContext):
        self.stack.pop()

    def exitRaw_text(self, ctx: JQLParser.Raw_textContext):
        raw = JQLRawInput()
        raw.set_text(ctx.getText())
        self.stack[-1].add(raw)


class JQLParseError(Exception):
    def __init__(self, e):
        super().__init__(e)


class JQLErrorStrategy(DefaultErrorStrategy):
    def reportError(self, recognizer: Parser, e: RecognitionException):
        if isinstance(e, InputMismatchException):
            raise JQLParseError(str(e))
        else:
            super().reportError(recognizer, e)


class Builder:
    def __init__(self, text: str, convert_ints=True):
        self.convert_ints = convert_ints
        self.text = text

        self.input_stream = InputStream(self.text)
        self.lexer = JQLLexer(self.input_stream)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = JQLParser(self.stream)
        self.parser._errHandler = JQLErrorStrategy()


class JQLQueryBuilder(Builder):
    def __init__(self, text: str, convert_ints=True):
        super().__init__(text, convert_ints)

        self.tree = self.parser.jql_query()
        self.printer = JQLQueryListener(convert_ints=self.convert_ints)
        self.walker = ParseTreeWalker()
        self.walker.walk(self.printer, self.tree)

        logger.debug(self.printer.root)

    def get_built_query(self) -> JQLQuery:
        return self.printer.root


class JQLMultiQueryBuilder(Builder):
    def __init__(self, text: str, convert_ints=True):
        super().__init__(text, convert_ints)

        self.tree = self.parser.jql_multi_query()
        self.printer = JQLMultiQueryListener(convert_ints=self.convert_ints)
        self.walker = ParseTreeWalker()
        self.walker.walk(self.printer, self.tree)

        logger.debug(self.printer.root)

    def get_built_query(self) -> JQLMultiQuery:
        return self.printer.root


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG)

    JQLQueryBuilder("tests")
    JQLQueryBuilder("tests.test")
    JQLQueryBuilder("tests.$wrap")
    JQLQueryBuilder("$wrap")
    JQLQueryBuilder("$wrap.text")
    JQLQueryBuilder("$wrap(5)")
    JQLQueryBuilder("$wrap('5')")
    JQLQueryBuilder('$wrap("5")')
    JQLQueryBuilder('$wrap(-4.5)')
    JQLQueryBuilder('$wrap([], {}, {:}, true, false, null, "true")')
    JQLQueryBuilder('$wrap([1, 2], {3, "4"}, {4: 5, "true": false})')
    JQLQueryBuilder('$wrap(@prefix, [5, @prefix])')
    JQLQueryBuilder('$wrap(@prefix, [5, @prefix.$sum, @prefix.$join(", ")])')
    JQLQueryBuilder('$wrap({@prefix: "john", @prefix: @prefix, "john": @prefix})')

    JQLMultiQueryBuilder("@tests.test something else @tests.$wrap")
