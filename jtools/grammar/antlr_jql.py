from typing import Type
from antlr4 import *
from antlr4.IntervalSet import IntervalSet
from antlr4.Token import CommonToken
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
            except (ValueError, TypeError):
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

    def enterArgument(self, ctx: JQLParser.ArgumentContext):
        arg = JQLArgument()
        self.stack[-1].add(arg)
        self.stack.append(arg)

    def exitArgument(self, ctx: JQLParser.ArgumentContext):
        self.stack.pop()

    def enterKeyword_argument(self, ctx: JQLParser.Keyword_argumentContext):
        arg = JQLKeywordArgument()
        self.stack[-1].add(arg)
        self.stack.append(arg)

    def exitKeyword_argument(self, ctx: JQLParser.Keyword_argumentContext):
        self.stack.pop()

    def enterName(self, ctx: JQLParser.NameContext):
        if isinstance(self.stack[-1], JQLKeywordArgument):
            self.stack[-1].set_name(ctx.getText())

    # EXPRESSIONS
    def enterArith_expr(self, ctx: JQLParser.Arith_exprContext):
        self.enter_expr()

    def exitArith_expr(self, ctx: JQLParser.Arith_exprContext):
        self.stack.pop()

    def enterFactor_expr(self, ctx: JQLParser.Factor_exprContext):
        self.enter_expr()

    def exitFactor_expr(self, ctx: JQLParser.Factor_exprContext):
        self.stack.pop()

    def enterPower_expr(self, ctx: JQLParser.Power_exprContext):
        self.enter_expr()

    def exitPower_expr(self, ctx: JQLParser.Power_exprContext):
        self.stack.pop()

    # EXPRESSION OPERATORS
    def enterArith_operator(self, ctx: JQLParser.Arith_operatorContext):
        self.stack[-1].set_operator(ctx.getText())

    def enterFactor_operator(self, ctx: JQLParser.Factor_operatorContext):
        self.stack[-1].set_operator(ctx.getText())

    def enterPower_operator(self, ctx: JQLParser.Power_operatorContext):
        self.stack[-1].set_operator(ctx.getText())

    def enterNumber(self, ctx: JQLParser.NumberContext):
        if isinstance(self.stack[-1], JQLExpression):
            v = JQLValue()
            v.value = self.parse_primitive(ctx.getText())
            self.stack[-1].add(v)

    def enterList_value(self, ctx: JQLParser.List_valueContext):
        self.enter_value(JQLList)

    def exitList_value(self, ctx: JQLParser.List_valueContext):
        self.stack.pop()

    def enterSet_value(self, ctx: JQLParser.Set_valueContext):
        self.enter_value(JQLSet)

    def exitSet_value(self, ctx: JQLParser.Set_valueContext):
        self.stack.pop()

    def enterObject_value(self, ctx: JQLParser.Object_valueContext):
        self.enter_value(JQLDict)

    def exitObject_value(self, ctx: JQLParser.Object_valueContext):
        self.stack.pop()

    def exitKey(self, ctx: JQLParser.KeyContext):
        txt = ctx.getText()
        if txt[0] != '@':  # query will add itself
            v = JQLValue()
            v.value = self.parse_primitive(ctx.getText())
            self.stack[-1].add(v)
        logger.debug(self.stack)

    def exitPrimitive_value(self, ctx: JQLParser.Primitive_valueContext):
        text = ctx.getText()
        val = JQLValue()
        val.value = self.parse_primitive(text)
        self.stack[-1].add(val)

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

    def enter_expr(self):
        expr = JQLExpression()
        self.stack[-1].add(expr)
        self.stack.append(expr)


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
    def __init__(self, got: CommonToken, expected: str):
        super().__init__(f"JQL Parse Error. Got '{got.text}', expected {expected}")


class JQLErrorStrategy(DefaultErrorStrategy):
    def __init__(self, lexer: JQLLexer):
        super().__init__()
        self.lexer = lexer

    def reportError(self, recognizer: Parser, e: RecognitionException):
        if isinstance(e, InputMismatchException):
            raise JQLParseError(
                e.offendingToken,
                e.getExpectedTokens().toString(self.lexer.literalNames, self.lexer.symbolicNames)
            )
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
        self.parser._errHandler = JQLErrorStrategy(self.lexer)


class JQLQueryBuilder(Builder):
    def __init__(self, text: str, convert_ints=True):
        super().__init__(text, convert_ints)

        self.tree = self.parser.jql_query()
        self.printer = JQLQueryListener(convert_ints=self.convert_ints)
        self.walker = ParseTreeWalker()
        self.walker.walk(self.printer, self.tree)

        logger.debug(self.printer.root)

    def __repr__(self):
        return repr(self.printer.root)

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

    JQLQueryBuilder("meta.timestamp.$special(4 * 5)")
