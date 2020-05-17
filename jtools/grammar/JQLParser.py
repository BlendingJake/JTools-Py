# Generated from jtools/grammar/JQL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("\u0204\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\3\2\3\2\7\2:\n\2\f\2\16")
        buf.write("\2=\13\2\3\3\7\3@\n\3\f\3\16\3C\13\3\3\3\5\3F\n\3\3\3")
        buf.write("\7\3I\n\3\f\3\16\3L\13\3\3\3\3\3\3\4\3\4\7\4R\n\4\f\4")
        buf.write("\16\4U\13\4\3\4\3\4\7\4Y\n\4\f\4\16\4\\\13\4\3\5\6\5_")
        buf.write("\n\5\r\5\16\5`\3\5\3\5\3\5\6\5f\n\5\r\5\16\5g\3\6\3\6")
        buf.write("\5\6l\n\6\3\7\3\7\3\b\3\b\3\b\5\bs\n\b\3\t\3\t\3\n\3\n")
        buf.write("\7\ny\n\n\f\n\16\n|\13\n\3\n\3\n\7\n\u0080\n\n\f\n\16")
        buf.write("\n\u0083\13\n\3\n\3\n\7\n\u0087\n\n\f\n\16\n\u008a\13")
        buf.write("\n\3\n\7\n\u008d\n\n\f\n\16\n\u0090\13\n\3\n\7\n\u0093")
        buf.write("\n\n\f\n\16\n\u0096\13\n\3\n\3\n\7\n\u009a\n\n\f\n\16")
        buf.write("\n\u009d\13\n\3\n\7\n\u00a0\n\n\f\n\16\n\u00a3\13\n\3")
        buf.write("\n\7\n\u00a6\n\n\f\n\16\n\u00a9\13\n\3\n\3\n\3\n\3\n\7")
        buf.write("\n\u00af\n\n\f\n\16\n\u00b2\13\n\3\n\3\n\7\n\u00b6\n\n")
        buf.write("\f\n\16\n\u00b9\13\n\3\n\3\n\7\n\u00bd\n\n\f\n\16\n\u00c0")
        buf.write("\13\n\3\n\7\n\u00c3\n\n\f\n\16\n\u00c6\13\n\3\n\3\n\3")
        buf.write("\n\3\n\7\n\u00cc\n\n\f\n\16\n\u00cf\13\n\3\n\5\n\u00d2")
        buf.write("\n\n\3\13\3\13\7\13\u00d6\n\13\f\13\16\13\u00d9\13\13")
        buf.write("\3\13\3\13\7\13\u00dd\n\13\f\13\16\13\u00e0\13\13\3\13")
        buf.write("\3\13\5\13\u00e4\n\13\3\f\3\f\5\f\u00e8\n\f\3\r\3\r\7")
        buf.write("\r\u00ec\n\r\f\r\16\r\u00ef\13\r\3\r\3\r\7\r\u00f3\n\r")
        buf.write("\f\r\16\r\u00f6\13\r\3\r\3\r\7\r\u00fa\n\r\f\r\16\r\u00fd")
        buf.write("\13\r\3\16\3\16\3\17\3\17\7\17\u0103\n\17\f\17\16\17\u0106")
        buf.write("\13\17\3\17\3\17\7\17\u010a\n\17\f\17\16\17\u010d\13\17")
        buf.write("\3\17\3\17\7\17\u0111\n\17\f\17\16\17\u0114\13\17\3\20")
        buf.write("\3\20\3\21\3\21\7\21\u011a\n\21\f\21\16\21\u011d\13\21")
        buf.write("\3\21\3\21\7\21\u0121\n\21\f\21\16\21\u0124\13\21\3\21")
        buf.write("\3\21\7\21\u0128\n\21\f\21\16\21\u012b\13\21\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\7\23\u0134\n\23\f\23\16\23\u0137")
        buf.write("\13\23\3\23\3\23\7\23\u013b\n\23\f\23\16\23\u013e\13\23")
        buf.write("\3\23\3\23\5\23\u0142\n\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u014c\n\24\3\25\3\25\7\25\u0150\n\25")
        buf.write("\f\25\16\25\u0153\13\25\3\25\3\25\7\25\u0157\n\25\f\25")
        buf.write("\16\25\u015a\13\25\3\25\3\25\7\25\u015e\n\25\f\25\16\25")
        buf.write("\u0161\13\25\3\25\7\25\u0164\n\25\f\25\16\25\u0167\13")
        buf.write("\25\3\25\7\25\u016a\n\25\f\25\16\25\u016d\13\25\3\25\3")
        buf.write("\25\3\25\3\25\7\25\u0173\n\25\f\25\16\25\u0176\13\25\3")
        buf.write("\25\5\25\u0179\n\25\3\26\3\26\7\26\u017d\n\26\f\26\16")
        buf.write("\26\u0180\13\26\3\26\3\26\7\26\u0184\n\26\f\26\16\26\u0187")
        buf.write("\13\26\3\26\3\26\7\26\u018b\n\26\f\26\16\26\u018e\13\26")
        buf.write("\3\26\7\26\u0191\n\26\f\26\16\26\u0194\13\26\3\26\7\26")
        buf.write("\u0197\n\26\f\26\16\26\u019a\13\26\3\26\3\26\3\26\3\26")
        buf.write("\7\26\u01a0\n\26\f\26\16\26\u01a3\13\26\3\26\5\26\u01a6")
        buf.write("\n\26\3\27\3\27\7\27\u01aa\n\27\f\27\16\27\u01ad\13\27")
        buf.write("\3\27\3\27\7\27\u01b1\n\27\f\27\16\27\u01b4\13\27\3\27")
        buf.write("\3\27\7\27\u01b8\n\27\f\27\16\27\u01bb\13\27\3\27\7\27")
        buf.write("\u01be\n\27\f\27\16\27\u01c1\13\27\3\27\7\27\u01c4\n\27")
        buf.write("\f\27\16\27\u01c7\13\27\3\27\3\27\3\27\3\27\7\27\u01cd")
        buf.write("\n\27\f\27\16\27\u01d0\13\27\3\27\3\27\7\27\u01d4\n\27")
        buf.write("\f\27\16\27\u01d7\13\27\3\27\5\27\u01da\n\27\3\30\3\30")
        buf.write("\7\30\u01de\n\30\f\30\16\30\u01e1\13\30\3\30\3\30\7\30")
        buf.write("\u01e5\n\30\f\30\16\30\u01e8\13\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u01f1\n\31\3\32\5\32\u01f4\n\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u01fa\n\32\3\32\5\32\u01fd\n\32")
        buf.write("\3\33\6\33\u0200\n\33\r\33\16\33\u0201\3\33\2\2\34\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\2\6\3\2\26\26\3\2\4\5\3\2\6\t\5\2\5\5\13\f\30\31\2\u023b")
        buf.write("\2;\3\2\2\2\4A\3\2\2\2\6O\3\2\2\2\be\3\2\2\2\nk\3\2\2")
        buf.write("\2\fm\3\2\2\2\16o\3\2\2\2\20t\3\2\2\2\22\u00d1\3\2\2\2")
        buf.write("\24\u00d3\3\2\2\2\26\u00e7\3\2\2\2\30\u00e9\3\2\2\2\32")
        buf.write("\u00fe\3\2\2\2\34\u0100\3\2\2\2\36\u0115\3\2\2\2 \u0117")
        buf.write("\3\2\2\2\"\u012c\3\2\2\2$\u0141\3\2\2\2&\u014b\3\2\2\2")
        buf.write("(\u0178\3\2\2\2*\u01a5\3\2\2\2,\u01d9\3\2\2\2.\u01db\3")
        buf.write("\2\2\2\60\u01f0\3\2\2\2\62\u01fc\3\2\2\2\64\u01ff\3\2")
        buf.write("\2\2\66\67\7\26\2\2\67:\5\6\4\28:\5\b\5\29\66\3\2\2\2")
        buf.write("98\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\3\3\2\2\2=;")
        buf.write("\3\2\2\2>@\7\33\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3")
        buf.write("\2\2\2BE\3\2\2\2CA\3\2\2\2DF\5\6\4\2ED\3\2\2\2EF\3\2\2")
        buf.write("\2FJ\3\2\2\2GI\7\33\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2")
        buf.write("JK\3\2\2\2KM\3\2\2\2LJ\3\2\2\2MN\7\2\2\3N\5\3\2\2\2OZ")
        buf.write("\5\n\6\2PR\7\33\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3")
        buf.write("\2\2\2TV\3\2\2\2US\3\2\2\2VW\7\17\2\2WY\5\n\6\2XS\3\2")
        buf.write("\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\7\3\2\2\2\\Z\3\2")
        buf.write("\2\2]_\7\33\2\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2")
        buf.write("\2af\3\2\2\2bc\7\26\2\2cf\7\26\2\2df\n\2\2\2e^\3\2\2\2")
        buf.write("eb\3\2\2\2ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\t")
        buf.write("\3\2\2\2il\5\f\7\2jl\5\16\b\2ki\3\2\2\2kj\3\2\2\2l\13")
        buf.write("\3\2\2\2mn\5\64\33\2n\r\3\2\2\2op\7\27\2\2pr\5\20\t\2")
        buf.write("qs\5\22\n\2rq\3\2\2\2rs\3\2\2\2s\17\3\2\2\2tu\5\64\33")
        buf.write("\2u\21\3\2\2\2vz\7\r\2\2wy\7\33\2\2xw\3\2\2\2y|\3\2\2")
        buf.write("\2zx\3\2\2\2z{\3\2\2\2{}\3\2\2\2|z\3\2\2\2}\u008e\5\26")
        buf.write("\f\2~\u0080\7\33\2\2\177~\3\2\2\2\u0080\u0083\3\2\2\2")
        buf.write("\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2")
        buf.write("\2\2\u0083\u0081\3\2\2\2\u0084\u0088\7\22\2\2\u0085\u0087")
        buf.write("\7\33\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\3\2\2\2")
        buf.write("\u008a\u0088\3\2\2\2\u008b\u008d\5\26\f\2\u008c\u0081")
        buf.write("\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u00a1\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0091\u0093\7\33\2\2\u0092\u0091\3\2\2\2\u0093\u0096")
        buf.write("\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0097\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u009b\7\22\2")
        buf.write("\2\u0098\u009a\7\33\2\2\u0099\u0098\3\2\2\2\u009a\u009d")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0\5\24\13")
        buf.write("\2\u009f\u0094\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a7\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a6\7\33\2\2\u00a5\u00a4\3\2\2")
        buf.write("\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa")
        buf.write("\u00ab\7\16\2\2\u00ab\u00d2\3\2\2\2\u00ac\u00b0\7\r\2")
        buf.write("\2\u00ad\u00af\7\33\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\u00b3\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00c4\5\24\13")
        buf.write("\2\u00b4\u00b6\7\33\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b9")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\u00ba\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00be\7\22\2")
        buf.write("\2\u00bb\u00bd\7\33\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0")
        buf.write("\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c1\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\5\24\13")
        buf.write("\2\u00c2\u00b7\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c8\7\16\2\2\u00c8\u00d2\3\2\2")
        buf.write("\2\u00c9\u00cd\7\r\2\2\u00ca\u00cc\7\33\2\2\u00cb\u00ca")
        buf.write("\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00d0\u00d2\7\16\2\2\u00d1v\3\2\2\2\u00d1\u00ac\3\2\2")
        buf.write("\2\u00d1\u00c9\3\2\2\2\u00d2\23\3\2\2\2\u00d3\u00d7\5")
        buf.write("\64\33\2\u00d4\u00d6\7\33\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d8\u00da\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00de\7")
        buf.write("\3\2\2\u00db\u00dd\7\33\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\u00e3\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e4\5")
        buf.write("\30\r\2\u00e2\u00e4\5&\24\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4\25\3\2\2\2\u00e5\u00e8\5\30\r\2\u00e6")
        buf.write("\u00e8\5&\24\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2")
        buf.write("\u00e8\27\3\2\2\2\u00e9\u00fb\5\34\17\2\u00ea\u00ec\7")
        buf.write("\33\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00f0\u00f4\5\32\16\2\u00f1\u00f3")
        buf.write("\7\33\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f7\u00f8\5\34\17\2\u00f8\u00fa")
        buf.write("\3\2\2\2\u00f9\u00ed\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\31\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fe\u00ff\t\3\2\2\u00ff\33\3\2\2\2\u0100")
        buf.write("\u0112\5 \21\2\u0101\u0103\7\33\2\2\u0102\u0101\3\2\2")
        buf.write("\2\u0103\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105")
        buf.write("\3\2\2\2\u0105\u0107\3\2\2\2\u0106\u0104\3\2\2\2\u0107")
        buf.write("\u010b\5\36\20\2\u0108\u010a\7\33\2\2\u0109\u0108\3\2")
        buf.write("\2\2\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010e")
        buf.write("\u010f\5 \21\2\u010f\u0111\3\2\2\2\u0110\u0104\3\2\2\2")
        buf.write("\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3")
        buf.write("\2\2\2\u0113\35\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116")
        buf.write("\t\4\2\2\u0116\37\3\2\2\2\u0117\u0129\5$\23\2\u0118\u011a")
        buf.write("\7\33\2\2\u0119\u0118\3\2\2\2\u011a\u011d\3\2\2\2\u011b")
        buf.write("\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011e\3\2\2\2")
        buf.write("\u011d\u011b\3\2\2\2\u011e\u0122\5\"\22\2\u011f\u0121")
        buf.write("\7\33\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2")
        buf.write("\u0124\u0122\3\2\2\2\u0125\u0126\5$\23\2\u0126\u0128\3")
        buf.write("\2\2\2\u0127\u011b\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u0129\u012a\3\2\2\2\u012a!\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012c\u012d\7\n\2\2\u012d#\3\2\2\2\u012e\u012f")
        buf.write("\7\26\2\2\u012f\u0142\5\6\4\2\u0130\u0142\5\62\32\2\u0131")
        buf.write("\u0135\7\r\2\2\u0132\u0134\7\33\2\2\u0133\u0132\3\2\2")
        buf.write("\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0138")
        buf.write("\u013c\5\30\r\2\u0139\u013b\7\33\2\2\u013a\u0139\3\2\2")
        buf.write("\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u013c\3\2\2\2\u013f")
        buf.write("\u0140\7\16\2\2\u0140\u0142\3\2\2\2\u0141\u012e\3\2\2")
        buf.write("\2\u0141\u0130\3\2\2\2\u0141\u0131\3\2\2\2\u0142%\3\2")
        buf.write("\2\2\u0143\u0144\7\26\2\2\u0144\u014c\5\6\4\2\u0145\u014c")
        buf.write("\5(\25\2\u0146\u014c\5*\26\2\u0147\u014c\5,\27\2\u0148")
        buf.write("\u014c\5\62\32\2\u0149\u014c\7\32\2\2\u014a\u014c\7\f")
        buf.write("\2\2\u014b\u0143\3\2\2\2\u014b\u0145\3\2\2\2\u014b\u0146")
        buf.write("\3\2\2\2\u014b\u0147\3\2\2\2\u014b\u0148\3\2\2\2\u014b")
        buf.write("\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c\'\3\2\2\2\u014d")
        buf.write("\u0151\7\20\2\2\u014e\u0150\7\33\2\2\u014f\u014e\3\2\2")
        buf.write("\2\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0154\3\2\2\2\u0153\u0151\3\2\2\2\u0154")
        buf.write("\u0165\5&\24\2\u0155\u0157\7\33\2\2\u0156\u0155\3\2\2")
        buf.write("\2\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159")
        buf.write("\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015b")
        buf.write("\u015f\7\22\2\2\u015c\u015e\7\33\2\2\u015d\u015c\3\2\2")
        buf.write("\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160")
        buf.write("\3\2\2\2\u0160\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0162")
        buf.write("\u0164\5&\24\2\u0163\u0158\3\2\2\2\u0164\u0167\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u016b\3")
        buf.write("\2\2\2\u0167\u0165\3\2\2\2\u0168\u016a\7\33\2\2\u0169")
        buf.write("\u0168\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2")
        buf.write("\u016b\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u016b\3")
        buf.write("\2\2\2\u016e\u016f\7\21\2\2\u016f\u0179\3\2\2\2\u0170")
        buf.write("\u0174\7\20\2\2\u0171\u0173\7\33\2\2\u0172\u0171\3\2\2")
        buf.write("\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write("\u0179\7\21\2\2\u0178\u014d\3\2\2\2\u0178\u0170\3\2\2")
        buf.write("\2\u0179)\3\2\2\2\u017a\u017e\7\23\2\2\u017b\u017d\7\33")
        buf.write("\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0181\u0192\5&\24\2\u0182\u0184\7\33\2")
        buf.write("\2\u0183\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0188\u018c\7\22\2\2\u0189\u018b\7\33\2")
        buf.write("\2\u018a\u0189\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018f\u0191\5&\24\2\u0190\u0185\3\2\2\2")
        buf.write("\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3")
        buf.write("\2\2\2\u0193\u0198\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0197")
        buf.write("\7\33\2\2\u0196\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019b\u019c\7\24\2\2\u019c\u01a6")
        buf.write("\3\2\2\2\u019d\u01a1\7\23\2\2\u019e\u01a0\7\33\2\2\u019f")
        buf.write("\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2")
        buf.write("\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3")
        buf.write("\2\2\2\u01a4\u01a6\7\24\2\2\u01a5\u017a\3\2\2\2\u01a5")
        buf.write("\u019d\3\2\2\2\u01a6+\3\2\2\2\u01a7\u01ab\7\23\2\2\u01a8")
        buf.write("\u01aa\7\33\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2")
        buf.write("\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae")
        buf.write("\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01bf\5.\30\2\u01af")
        buf.write("\u01b1\7\33\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2")
        buf.write("\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b9\7\22\2\2\u01b6")
        buf.write("\u01b8\7\33\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3\2\2")
        buf.write("\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01be\5.\30\2\u01bd")
        buf.write("\u01b2\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0\u01c5\3\2\2\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c2\u01c4\7\33\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9\7")
        buf.write("\24\2\2\u01c9\u01da\3\2\2\2\u01ca\u01ce\7\23\2\2\u01cb")
        buf.write("\u01cd\7\33\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0\3\2\2")
        buf.write("\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d1")
        buf.write("\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d5\7\25\2\2\u01d2")
        buf.write("\u01d4\7\33\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2")
        buf.write("\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d8")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01da\7\24\2\2\u01d9")
        buf.write("\u01a7\3\2\2\2\u01d9\u01ca\3\2\2\2\u01da-\3\2\2\2\u01db")
        buf.write("\u01df\5\60\31\2\u01dc\u01de\7\33\2\2\u01dd\u01dc\3\2")
        buf.write("\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2")
        buf.write("\u01e6\7\25\2\2\u01e3\u01e5\7\33\2\2\u01e4\u01e3\3\2\2")
        buf.write("\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7")
        buf.write("\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9")
        buf.write("\u01ea\5&\24\2\u01ea/\3\2\2\2\u01eb\u01ec\7\26\2\2\u01ec")
        buf.write("\u01f1\5\6\4\2\u01ed\u01f1\7\32\2\2\u01ee\u01f1\5\62\32")
        buf.write("\2\u01ef\u01f1\7\f\2\2\u01f0\u01eb\3\2\2\2\u01f0\u01ed")
        buf.write("\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1")
        buf.write("\61\3\2\2\2\u01f2\u01f4\t\3\2\2\u01f3\u01f2\3\2\2\2\u01f3")
        buf.write("\u01f4\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6\7\30\2")
        buf.write("\2\u01f6\u01f7\7\17\2\2\u01f7\u01fd\7\30\2\2\u01f8\u01fa")
        buf.write("\t\3\2\2\u01f9\u01f8\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fd\7\30\2\2\u01fc\u01f3\3\2\2")
        buf.write("\2\u01fc\u01f9\3\2\2\2\u01fd\63\3\2\2\2\u01fe\u0200\t")
        buf.write("\5\2\2\u01ff\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\65\3\2\2\2J9;AEJSZ")
        buf.write("`egkrz\u0081\u0088\u008e\u0094\u009b\u00a1\u00a7\u00b0")
        buf.write("\u00b7\u00be\u00c4\u00cd\u00d1\u00d7\u00de\u00e3\u00e7")
        buf.write("\u00ed\u00f4\u00fb\u0104\u010b\u0112\u011b\u0122\u0129")
        buf.write("\u0135\u013c\u0141\u014b\u0151\u0158\u015f\u0165\u016b")
        buf.write("\u0174\u0178\u017e\u0185\u018c\u0192\u0198\u01a1\u01a5")
        buf.write("\u01ab\u01b2\u01b9\u01bf\u01c5\u01ce\u01d5\u01d9\u01df")
        buf.write("\u01e6\u01f0\u01f3\u01f9\u01fc\u0201")
        return buf.getvalue()


class JQLParser ( Parser ):

    grammarFileName = "JQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'/'", "'//'", "'*'", 
                     "'%'", "'**'", "'_'", "<INVALID>", "'('", "')'", "'.'", 
                     "'['", "']'", "','", "'{'", "'}'", "':'", "'@'", "'$'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PRIMITIVE", "LPAREN", "RPAREN", 
                      "DOT", "LBRACKET", "RBRACKET", "COMMA", "LBRACE", 
                      "RBRACE", "SEMI", "AT", "DOLLAR", "DIGITS", "LETTERS", 
                      "STRING", "WS", "LAST" ]

    RULE_jql_multi_query = 0
    RULE_jql_query = 1
    RULE_query = 2
    RULE_raw_text = 3
    RULE_query_part = 4
    RULE_query_field = 5
    RULE_special = 6
    RULE_special_name = 7
    RULE_arguments = 8
    RULE_keyword_argument = 9
    RULE_argument = 10
    RULE_arith_expr = 11
    RULE_arith_operator = 12
    RULE_factor_expr = 13
    RULE_factor_operator = 14
    RULE_power_expr = 15
    RULE_power_operator = 16
    RULE_math_value = 17
    RULE_value = 18
    RULE_list_value = 19
    RULE_set_value = 20
    RULE_object_value = 21
    RULE_pair = 22
    RULE_key = 23
    RULE_number = 24
    RULE_name = 25

    ruleNames =  [ "jql_multi_query", "jql_query", "query", "raw_text", 
                   "query_part", "query_field", "special", "special_name", 
                   "arguments", "keyword_argument", "argument", "arith_expr", 
                   "arith_operator", "factor_expr", "factor_operator", "power_expr", 
                   "power_operator", "math_value", "value", "list_value", 
                   "set_value", "object_value", "pair", "key", "number", 
                   "name" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    PRIMITIVE=10
    LPAREN=11
    RPAREN=12
    DOT=13
    LBRACKET=14
    RBRACKET=15
    COMMA=16
    LBRACE=17
    RBRACE=18
    SEMI=19
    AT=20
    DOLLAR=21
    DIGITS=22
    LETTERS=23
    STRING=24
    WS=25
    LAST=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Jql_multi_queryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.AT)
            else:
                return self.getToken(JQLParser.AT, i)

        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.QueryContext)
            else:
                return self.getTypedRuleContext(JQLParser.QueryContext,i)


        def raw_text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Raw_textContext)
            else:
                return self.getTypedRuleContext(JQLParser.Raw_textContext,i)


        def getRuleIndex(self):
            return JQLParser.RULE_jql_multi_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJql_multi_query" ):
                listener.enterJql_multi_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJql_multi_query" ):
                listener.exitJql_multi_query(self)




    def jql_multi_query(self):

        localctx = JQLParser.Jql_multi_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_jql_multi_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__0) | (1 << JQLParser.T__1) | (1 << JQLParser.T__2) | (1 << JQLParser.T__3) | (1 << JQLParser.T__4) | (1 << JQLParser.T__5) | (1 << JQLParser.T__6) | (1 << JQLParser.T__7) | (1 << JQLParser.T__8) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.LPAREN) | (1 << JQLParser.RPAREN) | (1 << JQLParser.DOT) | (1 << JQLParser.LBRACKET) | (1 << JQLParser.RBRACKET) | (1 << JQLParser.COMMA) | (1 << JQLParser.LBRACE) | (1 << JQLParser.RBRACE) | (1 << JQLParser.SEMI) | (1 << JQLParser.AT) | (1 << JQLParser.DOLLAR) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS) | (1 << JQLParser.STRING) | (1 << JQLParser.WS) | (1 << JQLParser.LAST))) != 0):
                self.state = 55
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self.match(JQLParser.AT)
                    self.state = 53
                    self.query()
                    pass

                elif la_ == 2:
                    self.state = 54
                    self.raw_text()
                    pass


                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jql_queryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(JQLParser.EOF, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def query(self):
            return self.getTypedRuleContext(JQLParser.QueryContext,0)


        def getRuleIndex(self):
            return JQLParser.RULE_jql_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJql_query" ):
                listener.enterJql_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJql_query" ):
                listener.exitJql_query(self)




    def jql_query(self):

        localctx = JQLParser.Jql_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_jql_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 60
                    self.match(JQLParser.WS) 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__2) | (1 << JQLParser.T__8) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.DOLLAR) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS))) != 0):
                self.state = 66
                self.query()


            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 69
                self.match(JQLParser.WS)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(JQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Query_partContext)
            else:
                return self.getTypedRuleContext(JQLParser.Query_partContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.DOT)
            else:
                return self.getToken(JQLParser.DOT, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = JQLParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.query_part()
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 78
                        self.match(JQLParser.WS)
                        self.state = 83
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 84
                    self.match(JQLParser.DOT)
                    self.state = 85
                    self.query_part() 
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Raw_textContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.AT)
            else:
                return self.getToken(JQLParser.AT, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_raw_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_text" ):
                listener.enterRaw_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_text" ):
                listener.exitRaw_text(self)




    def raw_text(self):

        localctx = JQLParser.Raw_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_raw_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 99
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        self.state = 92 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 91
                                self.match(JQLParser.WS)

                            else:
                                raise NoViableAltException(self)
                            self.state = 94 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                        pass

                    elif la_ == 2:
                        self.state = 96
                        self.match(JQLParser.AT)
                        self.state = 97
                        self.match(JQLParser.AT)
                        pass

                    elif la_ == 3:
                        self.state = 98
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==JQLParser.AT:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 101 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query_field(self):
            return self.getTypedRuleContext(JQLParser.Query_fieldContext,0)


        def special(self):
            return self.getTypedRuleContext(JQLParser.SpecialContext,0)


        def getRuleIndex(self):
            return JQLParser.RULE_query_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_part" ):
                listener.enterQuery_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_part" ):
                listener.exitQuery_part(self)




    def query_part(self):

        localctx = JQLParser.Query_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_query_part)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.T__2, JQLParser.T__8, JQLParser.PRIMITIVE, JQLParser.DIGITS, JQLParser.LETTERS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.query_field()
                pass
            elif token in [JQLParser.DOLLAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.special()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(JQLParser.NameContext,0)


        def getRuleIndex(self):
            return JQLParser.RULE_query_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_field" ):
                listener.enterQuery_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_field" ):
                listener.exitQuery_field(self)




    def query_field(self):

        localctx = JQLParser.Query_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_query_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(JQLParser.DOLLAR, 0)

        def special_name(self):
            return self.getTypedRuleContext(JQLParser.Special_nameContext,0)


        def arguments(self):
            return self.getTypedRuleContext(JQLParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return JQLParser.RULE_special

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial" ):
                listener.enterSpecial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial" ):
                listener.exitSpecial(self)




    def special(self):

        localctx = JQLParser.SpecialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_special)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(JQLParser.DOLLAR)
            self.state = 110
            self.special_name()
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 111
                self.arguments()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Special_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(JQLParser.NameContext,0)


        def getRuleIndex(self):
            return JQLParser.RULE_special_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_name" ):
                listener.enterSpecial_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_name" ):
                listener.exitSpecial_name(self)




    def special_name(self):

        localctx = JQLParser.Special_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_special_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(JQLParser.LPAREN, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(JQLParser.ArgumentContext,i)


        def RPAREN(self):
            return self.getToken(JQLParser.RPAREN, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.COMMA)
            else:
                return self.getToken(JQLParser.COMMA, i)

        def keyword_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Keyword_argumentContext)
            else:
                return self.getTypedRuleContext(JQLParser.Keyword_argumentContext,i)


        def getRuleIndex(self):
            return JQLParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = JQLParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(JQLParser.LPAREN)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 117
                    self.match(JQLParser.WS)
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 123
                self.argument()
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 127
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 124
                            self.match(JQLParser.WS)
                            self.state = 129
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 130
                        self.match(JQLParser.COMMA)
                        self.state = 134
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 131
                            self.match(JQLParser.WS)
                            self.state = 136
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 137
                        self.argument() 
                    self.state = 142
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 146
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 143
                            self.match(JQLParser.WS)
                            self.state = 148
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 149
                        self.match(JQLParser.COMMA)
                        self.state = 153
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 150
                            self.match(JQLParser.WS)
                            self.state = 155
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 156
                        self.keyword_argument() 
                    self.state = 161
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 162
                    self.match(JQLParser.WS)
                    self.state = 167
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 168
                self.match(JQLParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(JQLParser.LPAREN)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 171
                    self.match(JQLParser.WS)
                    self.state = 176
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 177
                self.keyword_argument()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.COMMA or _la==JQLParser.WS:
                    self.state = 181
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 178
                        self.match(JQLParser.WS)
                        self.state = 183
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 184
                    self.match(JQLParser.COMMA)
                    self.state = 188
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 185
                        self.match(JQLParser.WS)
                        self.state = 190
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 191
                    self.keyword_argument()
                    self.state = 196
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 197
                self.match(JQLParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(JQLParser.LPAREN)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 200
                    self.match(JQLParser.WS)
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 206
                self.match(JQLParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(JQLParser.NameContext,0)


        def arith_expr(self):
            return self.getTypedRuleContext(JQLParser.Arith_exprContext,0)


        def value(self):
            return self.getTypedRuleContext(JQLParser.ValueContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_keyword_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword_argument" ):
                listener.enterKeyword_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword_argument" ):
                listener.exitKeyword_argument(self)




    def keyword_argument(self):

        localctx = JQLParser.Keyword_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_keyword_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.name()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 210
                self.match(JQLParser.WS)
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(JQLParser.T__0)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 217
                self.match(JQLParser.WS)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 223
                self.arith_expr()
                pass

            elif la_ == 2:
                self.state = 224
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arith_expr(self):
            return self.getTypedRuleContext(JQLParser.Arith_exprContext,0)


        def value(self):
            return self.getTypedRuleContext(JQLParser.ValueContext,0)


        def getRuleIndex(self):
            return JQLParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = JQLParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argument)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.arith_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Factor_exprContext)
            else:
                return self.getTypedRuleContext(JQLParser.Factor_exprContext,i)


        def arith_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Arith_operatorContext)
            else:
                return self.getTypedRuleContext(JQLParser.Arith_operatorContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_arith_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_expr" ):
                listener.enterArith_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_expr" ):
                listener.exitArith_expr(self)




    def arith_expr(self):

        localctx = JQLParser.Arith_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arith_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.factor_expr()
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 232
                        self.match(JQLParser.WS)
                        self.state = 237
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 238
                    self.arith_operator()
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 239
                        self.match(JQLParser.WS)
                        self.state = 244
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 245
                    self.factor_expr() 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JQLParser.RULE_arith_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_operator" ):
                listener.enterArith_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_operator" ):
                listener.exitArith_operator(self)




    def arith_operator(self):

        localctx = JQLParser.Arith_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arith_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            _la = self._input.LA(1)
            if not(_la==JQLParser.T__1 or _la==JQLParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def power_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Power_exprContext)
            else:
                return self.getTypedRuleContext(JQLParser.Power_exprContext,i)


        def factor_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Factor_operatorContext)
            else:
                return self.getTypedRuleContext(JQLParser.Factor_operatorContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_factor_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_expr" ):
                listener.enterFactor_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_expr" ):
                listener.exitFactor_expr(self)




    def factor_expr(self):

        localctx = JQLParser.Factor_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.power_expr()
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 255
                        self.match(JQLParser.WS)
                        self.state = 260
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 261
                    self.factor_operator()
                    self.state = 265
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 262
                        self.match(JQLParser.WS)
                        self.state = 267
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 268
                    self.power_expr() 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JQLParser.RULE_factor_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_operator" ):
                listener.enterFactor_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_operator" ):
                listener.exitFactor_operator(self)




    def factor_operator(self):

        localctx = JQLParser.Factor_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_factor_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__3) | (1 << JQLParser.T__4) | (1 << JQLParser.T__5) | (1 << JQLParser.T__6))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Power_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def math_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Math_valueContext)
            else:
                return self.getTypedRuleContext(JQLParser.Math_valueContext,i)


        def power_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.Power_operatorContext)
            else:
                return self.getTypedRuleContext(JQLParser.Power_operatorContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_power_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower_expr" ):
                listener.enterPower_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower_expr" ):
                listener.exitPower_expr(self)




    def power_expr(self):

        localctx = JQLParser.Power_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_power_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.math_value()
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 281
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 278
                        self.match(JQLParser.WS)
                        self.state = 283
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 284
                    self.power_operator()
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 285
                        self.match(JQLParser.WS)
                        self.state = 290
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 291
                    self.math_value() 
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Power_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JQLParser.RULE_power_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower_operator" ):
                listener.enterPower_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower_operator" ):
                listener.exitPower_operator(self)




    def power_operator(self):

        localctx = JQLParser.Power_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_power_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(JQLParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Math_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(JQLParser.AT, 0)

        def query(self):
            return self.getTypedRuleContext(JQLParser.QueryContext,0)


        def number(self):
            return self.getTypedRuleContext(JQLParser.NumberContext,0)


        def LPAREN(self):
            return self.getToken(JQLParser.LPAREN, 0)

        def arith_expr(self):
            return self.getTypedRuleContext(JQLParser.Arith_exprContext,0)


        def RPAREN(self):
            return self.getToken(JQLParser.RPAREN, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_math_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_value" ):
                listener.enterMath_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_value" ):
                listener.exitMath_value(self)




    def math_value(self):

        localctx = JQLParser.Math_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_math_value)
        self._la = 0 # Token type
        try:
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(JQLParser.AT)
                self.state = 301
                self.query()
                pass
            elif token in [JQLParser.T__1, JQLParser.T__2, JQLParser.DIGITS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.number()
                pass
            elif token in [JQLParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(JQLParser.LPAREN)
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 304
                    self.match(JQLParser.WS)
                    self.state = 309
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 310
                self.arith_expr()
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 311
                    self.match(JQLParser.WS)
                    self.state = 316
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 317
                self.match(JQLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(JQLParser.AT, 0)

        def query(self):
            return self.getTypedRuleContext(JQLParser.QueryContext,0)


        def list_value(self):
            return self.getTypedRuleContext(JQLParser.List_valueContext,0)


        def set_value(self):
            return self.getTypedRuleContext(JQLParser.Set_valueContext,0)


        def object_value(self):
            return self.getTypedRuleContext(JQLParser.Object_valueContext,0)


        def number(self):
            return self.getTypedRuleContext(JQLParser.NumberContext,0)


        def STRING(self):
            return self.getToken(JQLParser.STRING, 0)

        def PRIMITIVE(self):
            return self.getToken(JQLParser.PRIMITIVE, 0)

        def getRuleIndex(self):
            return JQLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = JQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_value)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(JQLParser.AT)
                self.state = 322
                self.query()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.list_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.set_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
                self.object_value()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 326
                self.number()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 327
                self.match(JQLParser.STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 328
                self.match(JQLParser.PRIMITIVE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(JQLParser.LBRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.ValueContext)
            else:
                return self.getTypedRuleContext(JQLParser.ValueContext,i)


        def RBRACKET(self):
            return self.getToken(JQLParser.RBRACKET, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.COMMA)
            else:
                return self.getToken(JQLParser.COMMA, i)

        def getRuleIndex(self):
            return JQLParser.RULE_list_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_value" ):
                listener.enterList_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_value" ):
                listener.exitList_value(self)




    def list_value(self):

        localctx = JQLParser.List_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_value)
        self._la = 0 # Token type
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(JQLParser.LBRACKET)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 332
                    self.match(JQLParser.WS)
                    self.state = 337
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 338
                self.value()
                self.state = 355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 342
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 339
                            self.match(JQLParser.WS)
                            self.state = 344
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 345
                        self.match(JQLParser.COMMA)
                        self.state = 349
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 346
                            self.match(JQLParser.WS)
                            self.state = 351
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 352
                        self.value() 
                    self.state = 357
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 358
                    self.match(JQLParser.WS)
                    self.state = 363
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 364
                self.match(JQLParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(JQLParser.LBRACKET)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 367
                    self.match(JQLParser.WS)
                    self.state = 372
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 373
                self.match(JQLParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(JQLParser.LBRACE, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.ValueContext)
            else:
                return self.getTypedRuleContext(JQLParser.ValueContext,i)


        def RBRACE(self):
            return self.getToken(JQLParser.RBRACE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.COMMA)
            else:
                return self.getToken(JQLParser.COMMA, i)

        def getRuleIndex(self):
            return JQLParser.RULE_set_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_value" ):
                listener.enterSet_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_value" ):
                listener.exitSet_value(self)




    def set_value(self):

        localctx = JQLParser.Set_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_set_value)
        self._la = 0 # Token type
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(JQLParser.LBRACE)
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 377
                    self.match(JQLParser.WS)
                    self.state = 382
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 383
                self.value()
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 387
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 384
                            self.match(JQLParser.WS)
                            self.state = 389
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 390
                        self.match(JQLParser.COMMA)
                        self.state = 394
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 391
                            self.match(JQLParser.WS)
                            self.state = 396
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 397
                        self.value() 
                    self.state = 402
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 403
                    self.match(JQLParser.WS)
                    self.state = 408
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 409
                self.match(JQLParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(JQLParser.LBRACE)
                self.state = 415
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 412
                    self.match(JQLParser.WS)
                    self.state = 417
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 418
                self.match(JQLParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(JQLParser.LBRACE, 0)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.PairContext)
            else:
                return self.getTypedRuleContext(JQLParser.PairContext,i)


        def RBRACE(self):
            return self.getToken(JQLParser.RBRACE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.COMMA)
            else:
                return self.getToken(JQLParser.COMMA, i)

        def SEMI(self):
            return self.getToken(JQLParser.SEMI, 0)

        def getRuleIndex(self):
            return JQLParser.RULE_object_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_value" ):
                listener.enterObject_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_value" ):
                listener.exitObject_value(self)




    def object_value(self):

        localctx = JQLParser.Object_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_object_value)
        self._la = 0 # Token type
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(JQLParser.LBRACE)
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 422
                    self.match(JQLParser.WS)
                    self.state = 427
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 428
                self.pair()
                self.state = 445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 432
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 429
                            self.match(JQLParser.WS)
                            self.state = 434
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 435
                        self.match(JQLParser.COMMA)
                        self.state = 439
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 436
                            self.match(JQLParser.WS)
                            self.state = 441
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 442
                        self.pair() 
                    self.state = 447
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 448
                    self.match(JQLParser.WS)
                    self.state = 453
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 454
                self.match(JQLParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.match(JQLParser.LBRACE)
                self.state = 460
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 457
                    self.match(JQLParser.WS)
                    self.state = 462
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 463
                self.match(JQLParser.SEMI)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 464
                    self.match(JQLParser.WS)
                    self.state = 469
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 470
                self.match(JQLParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(JQLParser.KeyContext,0)


        def SEMI(self):
            return self.getToken(JQLParser.SEMI, 0)

        def value(self):
            return self.getTypedRuleContext(JQLParser.ValueContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.WS)
            else:
                return self.getToken(JQLParser.WS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = JQLParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.key()
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 474
                self.match(JQLParser.WS)
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 480
            self.match(JQLParser.SEMI)
            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 481
                self.match(JQLParser.WS)
                self.state = 486
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 487
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(JQLParser.AT, 0)

        def query(self):
            return self.getTypedRuleContext(JQLParser.QueryContext,0)


        def STRING(self):
            return self.getToken(JQLParser.STRING, 0)

        def number(self):
            return self.getTypedRuleContext(JQLParser.NumberContext,0)


        def PRIMITIVE(self):
            return self.getToken(JQLParser.PRIMITIVE, 0)

        def getRuleIndex(self):
            return JQLParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = JQLParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_key)
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(JQLParser.AT)
                self.state = 490
                self.query()
                pass
            elif token in [JQLParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.match(JQLParser.STRING)
                pass
            elif token in [JQLParser.T__1, JQLParser.T__2, JQLParser.DIGITS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 492
                self.number()
                pass
            elif token in [JQLParser.PRIMITIVE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 493
                self.match(JQLParser.PRIMITIVE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.DIGITS)
            else:
                return self.getToken(JQLParser.DIGITS, i)

        def DOT(self):
            return self.getToken(JQLParser.DOT, 0)

        def getRuleIndex(self):
            return JQLParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = JQLParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JQLParser.T__1 or _la==JQLParser.T__2:
                    self.state = 496
                    _la = self._input.LA(1)
                    if not(_la==JQLParser.T__1 or _la==JQLParser.T__2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 499
                self.match(JQLParser.DIGITS)
                self.state = 500
                self.match(JQLParser.DOT)
                self.state = 501
                self.match(JQLParser.DIGITS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JQLParser.T__1 or _la==JQLParser.T__2:
                    self.state = 502
                    _la = self._input.LA(1)
                    if not(_la==JQLParser.T__1 or _la==JQLParser.T__2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 505
                self.match(JQLParser.DIGITS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRIMITIVE(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.PRIMITIVE)
            else:
                return self.getToken(JQLParser.PRIMITIVE, i)

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.DIGITS)
            else:
                return self.getToken(JQLParser.DIGITS, i)

        def LETTERS(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.LETTERS)
            else:
                return self.getToken(JQLParser.LETTERS, i)

        def getRuleIndex(self):
            return JQLParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = JQLParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 508
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__2) | (1 << JQLParser.T__8) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 511 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





