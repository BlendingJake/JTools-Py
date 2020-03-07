# Generated from jtools/grammar/JQL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u009a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5")
        buf.write("\bY\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\6\24r\n\24\r\24\16\24s\3\25\6\25w\n\25\r\25\16\25")
        buf.write("x\3\26\3\26\3\26\3\26\7\26\177\n\26\f\26\16\26\u0082\13")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\7\26\u0089\n\26\f\26\16\26")
        buf.write("\u008c\13\26\3\26\5\26\u008f\n\26\3\27\3\27\3\30\3\30")
        buf.write("\5\30\u0095\n\30\3\31\3\31\3\32\3\32\2\2\33\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\3\2\n\3\2\62;\4\2C\\c|\3\2$$\3\2))\3\2\"\"\4\2\13")
        buf.write("\f\16\17\4\2**\60\60\3\2\f\f\2\u00a3\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\3\65\3\2\2\2\5:\3\2\2\2\7@\3\2\2\2")
        buf.write("\tE\3\2\2\2\13G\3\2\2\2\rI\3\2\2\2\17X\3\2\2\2\21Z\3\2")
        buf.write("\2\2\23\\\3\2\2\2\25^\3\2\2\2\27`\3\2\2\2\31b\3\2\2\2")
        buf.write("\33d\3\2\2\2\35f\3\2\2\2\37h\3\2\2\2!j\3\2\2\2#l\3\2\2")
        buf.write("\2%n\3\2\2\2\'q\3\2\2\2)v\3\2\2\2+\u008e\3\2\2\2-\u0090")
        buf.write("\3\2\2\2/\u0094\3\2\2\2\61\u0096\3\2\2\2\63\u0098\3\2")
        buf.write("\2\2\65\66\7v\2\2\66\67\7t\2\2\678\7w\2\289\7g\2\29\4")
        buf.write("\3\2\2\2:;\7h\2\2;<\7c\2\2<=\7n\2\2=>\7u\2\2>?\7g\2\2")
        buf.write("?\6\3\2\2\2@A\7p\2\2AB\7w\2\2BC\7n\2\2CD\7n\2\2D\b\3\2")
        buf.write("\2\2EF\7/\2\2F\n\3\2\2\2GH\7-\2\2H\f\3\2\2\2IJ\7a\2\2")
        buf.write("J\16\3\2\2\2KL\7v\2\2LM\7t\2\2MN\7w\2\2NY\7g\2\2OP\7h")
        buf.write("\2\2PQ\7c\2\2QR\7n\2\2RS\7u\2\2SY\7g\2\2TU\7p\2\2UV\7")
        buf.write("w\2\2VW\7n\2\2WY\7n\2\2XK\3\2\2\2XO\3\2\2\2XT\3\2\2\2")
        buf.write("Y\20\3\2\2\2Z[\7*\2\2[\22\3\2\2\2\\]\7+\2\2]\24\3\2\2")
        buf.write("\2^_\7\60\2\2_\26\3\2\2\2`a\7]\2\2a\30\3\2\2\2bc\7_\2")
        buf.write("\2c\32\3\2\2\2de\7.\2\2e\34\3\2\2\2fg\7}\2\2g\36\3\2\2")
        buf.write("\2hi\7\177\2\2i \3\2\2\2jk\7<\2\2k\"\3\2\2\2lm\7B\2\2")
        buf.write("m$\3\2\2\2no\7&\2\2o&\3\2\2\2pr\t\2\2\2qp\3\2\2\2rs\3")
        buf.write("\2\2\2sq\3\2\2\2st\3\2\2\2t(\3\2\2\2uw\t\3\2\2vu\3\2\2")
        buf.write("\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2y*\3\2\2\2z\u0080\7$\2")
        buf.write("\2{|\7^\2\2|\177\7$\2\2}\177\n\4\2\2~{\3\2\2\2~}\3\2\2")
        buf.write("\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2")
        buf.write("\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u008f")
        buf.write("\7$\2\2\u0084\u008a\7)\2\2\u0085\u0086\7^\2\2\u0086\u0089")
        buf.write("\7)\2\2\u0087\u0089\n\5\2\2\u0088\u0085\3\2\2\2\u0088")
        buf.write("\u0087\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2")
        buf.write("\u008a\u008b\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u008a\3")
        buf.write("\2\2\2\u008d\u008f\7)\2\2\u008ez\3\2\2\2\u008e\u0084\3")
        buf.write("\2\2\2\u008f,\3\2\2\2\u0090\u0091\t\6\2\2\u0091.\3\2\2")
        buf.write("\2\u0092\u0095\5-\27\2\u0093\u0095\t\7\2\2\u0094\u0092")
        buf.write("\3\2\2\2\u0094\u0093\3\2\2\2\u0095\60\3\2\2\2\u0096\u0097")
        buf.write("\n\b\2\2\u0097\62\3\2\2\2\u0098\u0099\n\t\2\2\u0099\64")
        buf.write("\3\2\2\2\f\2Xsx~\u0080\u0088\u008a\u008e\u0094\2")
        return buf.getvalue()


class JQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    PRIMITIVE = 7
    LPAREN = 8
    RPAREN = 9
    DOT = 10
    LBRACKET = 11
    RBRACKET = 12
    COMMA = 13
    LBRACE = 14
    RBRACE = 15
    SEMI = 16
    AT = 17
    DOLLAR = 18
    DIGITS = 19
    LETTERS = 20
    STRING = 21
    SPACE = 22
    WS = 23
    IDENTIFIER = 24
    LAST = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'null'", "'-'", "'+'", "'_'", "'('", "')'", 
            "'.'", "'['", "']'", "','", "'{'", "'}'", "':'", "'@'", "'$'" ]

    symbolicNames = [ "<INVALID>",
            "PRIMITIVE", "LPAREN", "RPAREN", "DOT", "LBRACKET", "RBRACKET", 
            "COMMA", "LBRACE", "RBRACE", "SEMI", "AT", "DOLLAR", "DIGITS", 
            "LETTERS", "STRING", "SPACE", "WS", "IDENTIFIER", "LAST" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "PRIMITIVE", 
                  "LPAREN", "RPAREN", "DOT", "LBRACKET", "RBRACKET", "COMMA", 
                  "LBRACE", "RBRACE", "SEMI", "AT", "DOLLAR", "DIGITS", 
                  "LETTERS", "STRING", "SPACE", "WS", "IDENTIFIER", "LAST" ]

    grammarFileName = "JQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


