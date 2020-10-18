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
        buf.write("\u020a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\7\2<\n")
        buf.write("\2\f\2\16\2?\13\2\3\3\7\3B\n\3\f\3\16\3E\13\3\3\3\5\3")
        buf.write("H\n\3\3\3\7\3K\n\3\f\3\16\3N\13\3\3\3\3\3\3\4\3\4\7\4")
        buf.write("T\n\4\f\4\16\4W\13\4\3\4\3\4\7\4[\n\4\f\4\16\4^\13\4\3")
        buf.write("\5\6\5a\n\5\r\5\16\5b\3\5\3\5\3\5\6\5h\n\5\r\5\16\5i\3")
        buf.write("\6\3\6\5\6n\n\6\3\7\3\7\3\b\3\b\3\b\5\bu\n\b\3\t\3\t\3")
        buf.write("\n\3\n\7\n{\n\n\f\n\16\n~\13\n\3\n\3\n\7\n\u0082\n\n\f")
        buf.write("\n\16\n\u0085\13\n\3\n\3\n\7\n\u0089\n\n\f\n\16\n\u008c")
        buf.write("\13\n\3\n\7\n\u008f\n\n\f\n\16\n\u0092\13\n\3\n\7\n\u0095")
        buf.write("\n\n\f\n\16\n\u0098\13\n\3\n\3\n\7\n\u009c\n\n\f\n\16")
        buf.write("\n\u009f\13\n\3\n\7\n\u00a2\n\n\f\n\16\n\u00a5\13\n\3")
        buf.write("\n\7\n\u00a8\n\n\f\n\16\n\u00ab\13\n\3\n\3\n\3\n\3\n\7")
        buf.write("\n\u00b1\n\n\f\n\16\n\u00b4\13\n\3\n\3\n\7\n\u00b8\n\n")
        buf.write("\f\n\16\n\u00bb\13\n\3\n\3\n\7\n\u00bf\n\n\f\n\16\n\u00c2")
        buf.write("\13\n\3\n\7\n\u00c5\n\n\f\n\16\n\u00c8\13\n\3\n\3\n\3")
        buf.write("\n\3\n\7\n\u00ce\n\n\f\n\16\n\u00d1\13\n\3\n\5\n\u00d4")
        buf.write("\n\n\3\13\3\13\7\13\u00d8\n\13\f\13\16\13\u00db\13\13")
        buf.write("\3\13\3\13\7\13\u00df\n\13\f\13\16\13\u00e2\13\13\3\13")
        buf.write("\3\13\5\13\u00e6\n\13\3\f\3\f\5\f\u00ea\n\f\3\r\3\r\7")
        buf.write("\r\u00ee\n\r\f\r\16\r\u00f1\13\r\3\r\3\r\7\r\u00f5\n\r")
        buf.write("\f\r\16\r\u00f8\13\r\3\r\3\r\7\r\u00fc\n\r\f\r\16\r\u00ff")
        buf.write("\13\r\3\16\3\16\3\17\3\17\7\17\u0105\n\17\f\17\16\17\u0108")
        buf.write("\13\17\3\17\3\17\7\17\u010c\n\17\f\17\16\17\u010f\13\17")
        buf.write("\3\17\3\17\7\17\u0113\n\17\f\17\16\17\u0116\13\17\3\20")
        buf.write("\3\20\3\21\3\21\7\21\u011c\n\21\f\21\16\21\u011f\13\21")
        buf.write("\3\21\3\21\7\21\u0123\n\21\f\21\16\21\u0126\13\21\3\21")
        buf.write("\3\21\7\21\u012a\n\21\f\21\16\21\u012d\13\21\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\7\23\u0136\n\23\f\23\16\23\u0139")
        buf.write("\13\23\3\23\3\23\7\23\u013d\n\23\f\23\16\23\u0140\13\23")
        buf.write("\3\23\3\23\5\23\u0144\n\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\5\24\u014d\n\24\3\25\3\25\3\25\5\25\u0152\n\25")
        buf.write("\3\26\3\26\7\26\u0156\n\26\f\26\16\26\u0159\13\26\3\26")
        buf.write("\3\26\7\26\u015d\n\26\f\26\16\26\u0160\13\26\3\26\3\26")
        buf.write("\7\26\u0164\n\26\f\26\16\26\u0167\13\26\3\26\7\26\u016a")
        buf.write("\n\26\f\26\16\26\u016d\13\26\3\26\7\26\u0170\n\26\f\26")
        buf.write("\16\26\u0173\13\26\3\26\3\26\3\26\3\26\7\26\u0179\n\26")
        buf.write("\f\26\16\26\u017c\13\26\3\26\5\26\u017f\n\26\3\27\3\27")
        buf.write("\7\27\u0183\n\27\f\27\16\27\u0186\13\27\3\27\3\27\7\27")
        buf.write("\u018a\n\27\f\27\16\27\u018d\13\27\3\27\3\27\7\27\u0191")
        buf.write("\n\27\f\27\16\27\u0194\13\27\3\27\7\27\u0197\n\27\f\27")
        buf.write("\16\27\u019a\13\27\3\27\7\27\u019d\n\27\f\27\16\27\u01a0")
        buf.write("\13\27\3\27\3\27\3\27\3\27\7\27\u01a6\n\27\f\27\16\27")
        buf.write("\u01a9\13\27\3\27\5\27\u01ac\n\27\3\30\3\30\7\30\u01b0")
        buf.write("\n\30\f\30\16\30\u01b3\13\30\3\30\3\30\7\30\u01b7\n\30")
        buf.write("\f\30\16\30\u01ba\13\30\3\30\3\30\7\30\u01be\n\30\f\30")
        buf.write("\16\30\u01c1\13\30\3\30\7\30\u01c4\n\30\f\30\16\30\u01c7")
        buf.write("\13\30\3\30\7\30\u01ca\n\30\f\30\16\30\u01cd\13\30\3\30")
        buf.write("\3\30\3\30\3\30\7\30\u01d3\n\30\f\30\16\30\u01d6\13\30")
        buf.write("\3\30\3\30\7\30\u01da\n\30\f\30\16\30\u01dd\13\30\3\30")
        buf.write("\5\30\u01e0\n\30\3\31\3\31\7\31\u01e4\n\31\f\31\16\31")
        buf.write("\u01e7\13\31\3\31\3\31\7\31\u01eb\n\31\f\31\16\31\u01ee")
        buf.write("\13\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u01f7\n")
        buf.write("\32\3\33\5\33\u01fa\n\33\3\33\3\33\3\33\3\33\5\33\u0200")
        buf.write("\n\33\3\33\5\33\u0203\n\33\3\34\6\34\u0206\n\34\r\34\16")
        buf.write("\34\u0207\3\34\2\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\66\2\6\3\2\26\26\3\2\4\5\3\2")
        buf.write("\6\t\5\2\5\5\13\f\30\31\2\u0241\2=\3\2\2\2\4C\3\2\2\2")
        buf.write("\6Q\3\2\2\2\bg\3\2\2\2\nm\3\2\2\2\fo\3\2\2\2\16q\3\2\2")
        buf.write("\2\20v\3\2\2\2\22\u00d3\3\2\2\2\24\u00d5\3\2\2\2\26\u00e9")
        buf.write("\3\2\2\2\30\u00eb\3\2\2\2\32\u0100\3\2\2\2\34\u0102\3")
        buf.write("\2\2\2\36\u0117\3\2\2\2 \u0119\3\2\2\2\"\u012e\3\2\2\2")
        buf.write("$\u0143\3\2\2\2&\u014c\3\2\2\2(\u0151\3\2\2\2*\u017e\3")
        buf.write("\2\2\2,\u01ab\3\2\2\2.\u01df\3\2\2\2\60\u01e1\3\2\2\2")
        buf.write("\62\u01f6\3\2\2\2\64\u0202\3\2\2\2\66\u0205\3\2\2\289")
        buf.write("\7\26\2\29<\5\6\4\2:<\5\b\5\2;8\3\2\2\2;:\3\2\2\2<?\3")
        buf.write("\2\2\2=;\3\2\2\2=>\3\2\2\2>\3\3\2\2\2?=\3\2\2\2@B\7\33")
        buf.write("\2\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2DG\3\2\2\2")
        buf.write("EC\3\2\2\2FH\5\6\4\2GF\3\2\2\2GH\3\2\2\2HL\3\2\2\2IK\7")
        buf.write("\33\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2")
        buf.write("\2\2NL\3\2\2\2OP\7\2\2\3P\5\3\2\2\2Q\\\5\n\6\2RT\7\33")
        buf.write("\2\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2VX\3\2\2\2")
        buf.write("WU\3\2\2\2XY\7\17\2\2Y[\5\n\6\2ZU\3\2\2\2[^\3\2\2\2\\")
        buf.write("Z\3\2\2\2\\]\3\2\2\2]\7\3\2\2\2^\\\3\2\2\2_a\7\33\2\2")
        buf.write("`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2ch\3\2\2\2de\7")
        buf.write("\26\2\2eh\7\26\2\2fh\n\2\2\2g`\3\2\2\2gd\3\2\2\2gf\3\2")
        buf.write("\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\t\3\2\2\2kn\5\f\7")
        buf.write("\2ln\5\16\b\2mk\3\2\2\2ml\3\2\2\2n\13\3\2\2\2op\5\66\34")
        buf.write("\2p\r\3\2\2\2qr\7\27\2\2rt\5\20\t\2su\5\22\n\2ts\3\2\2")
        buf.write("\2tu\3\2\2\2u\17\3\2\2\2vw\5\66\34\2w\21\3\2\2\2x|\7\r")
        buf.write("\2\2y{\7\33\2\2zy\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2")
        buf.write("\2}\177\3\2\2\2~|\3\2\2\2\177\u0090\5\26\f\2\u0080\u0082")
        buf.write("\7\33\2\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2\2")
        buf.write("\u0085\u0083\3\2\2\2\u0086\u008a\7\22\2\2\u0087\u0089")
        buf.write("\7\33\2\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d\3\2\2\2")
        buf.write("\u008c\u008a\3\2\2\2\u008d\u008f\5\26\f\2\u008e\u0083")
        buf.write("\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u00a3\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0093\u0095\7\33\2\2\u0094\u0093\3\2\2\2\u0095\u0098")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009d\7\22\2")
        buf.write("\2\u009a\u009c\7\33\2\2\u009b\u009a\3\2\2\2\u009c\u009f")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2\5\24\13")
        buf.write("\2\u00a1\u0096\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a9\3\2\2\2\u00a5")
        buf.write("\u00a3\3\2\2\2\u00a6\u00a8\7\33\2\2\u00a7\u00a6\3\2\2")
        buf.write("\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac")
        buf.write("\u00ad\7\16\2\2\u00ad\u00d4\3\2\2\2\u00ae\u00b2\7\r\2")
        buf.write("\2\u00af\u00b1\7\33\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b4")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00c6\5\24\13")
        buf.write("\2\u00b6\u00b8\7\33\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb")
        buf.write("\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00c0\7\22\2")
        buf.write("\2\u00bd\u00bf\7\33\2\2\u00be\u00bd\3\2\2\2\u00bf\u00c2")
        buf.write("\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1")
        buf.write("\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c5\5\24\13")
        buf.write("\2\u00c4\u00b9\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4")
        buf.write("\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c9\u00ca\7\16\2\2\u00ca\u00d4\3\2\2")
        buf.write("\2\u00cb\u00cf\7\r\2\2\u00cc\u00ce\7\33\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d0\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d2\u00d4\7\16\2\2\u00d3x\3\2\2\2\u00d3\u00ae\3\2\2")
        buf.write("\2\u00d3\u00cb\3\2\2\2\u00d4\23\3\2\2\2\u00d5\u00d9\5")
        buf.write("\66\34\2\u00d6\u00d8\7\33\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00e0\7")
        buf.write("\3\2\2\u00dd\u00df\7\33\2\2\u00de\u00dd\3\2\2\2\u00df")
        buf.write("\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e5\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\5")
        buf.write("\30\r\2\u00e4\u00e6\5&\24\2\u00e5\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6\25\3\2\2\2\u00e7\u00ea\5\30\r\2\u00e8")
        buf.write("\u00ea\5&\24\2\u00e9\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea\27\3\2\2\2\u00eb\u00fd\5\34\17\2\u00ec\u00ee\7")
        buf.write("\33\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f2\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f2\u00f6\5\32\16\2\u00f3\u00f5")
        buf.write("\7\33\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f9\u00fa\5\34\17\2\u00fa\u00fc")
        buf.write("\3\2\2\2\u00fb\u00ef\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\31\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u0100\u0101\t\3\2\2\u0101\33\3\2\2\2\u0102")
        buf.write("\u0114\5 \21\2\u0103\u0105\7\33\2\2\u0104\u0103\3\2\2")
        buf.write("\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3\2\2\2\u0109")
        buf.write("\u010d\5\36\20\2\u010a\u010c\7\33\2\2\u010b\u010a\3\2")
        buf.write("\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e\u0110\3\2\2\2\u010f\u010d\3\2\2\2\u0110")
        buf.write("\u0111\5 \21\2\u0111\u0113\3\2\2\2\u0112\u0106\3\2\2\2")
        buf.write("\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3")
        buf.write("\2\2\2\u0115\35\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118")
        buf.write("\t\4\2\2\u0118\37\3\2\2\2\u0119\u012b\5$\23\2\u011a\u011c")
        buf.write("\7\33\2\2\u011b\u011a\3\2\2\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0120\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u0120\u0124\5\"\22\2\u0121\u0123")
        buf.write("\7\33\2\2\u0122\u0121\3\2\2\2\u0123\u0126\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0127\u0128\5$\23\2\u0128\u012a\3")
        buf.write("\2\2\2\u0129\u011d\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c!\3\2\2\2\u012d\u012b")
        buf.write("\3\2\2\2\u012e\u012f\7\n\2\2\u012f#\3\2\2\2\u0130\u0131")
        buf.write("\7\26\2\2\u0131\u0144\5\6\4\2\u0132\u0144\5\64\33\2\u0133")
        buf.write("\u0137\7\r\2\2\u0134\u0136\7\33\2\2\u0135\u0134\3\2\2")
        buf.write("\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u0137\3\2\2\2\u013a")
        buf.write("\u013e\5\30\r\2\u013b\u013d\7\33\2\2\u013c\u013b\3\2\2")
        buf.write("\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f")
        buf.write("\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u013e\3\2\2\2\u0141")
        buf.write("\u0142\7\16\2\2\u0142\u0144\3\2\2\2\u0143\u0130\3\2\2")
        buf.write("\2\u0143\u0132\3\2\2\2\u0143\u0133\3\2\2\2\u0144%\3\2")
        buf.write("\2\2\u0145\u0146\7\26\2\2\u0146\u014d\5\6\4\2\u0147\u014d")
        buf.write("\5*\26\2\u0148\u014d\5,\27\2\u0149\u014d\5.\30\2\u014a")
        buf.write("\u014d\5\30\r\2\u014b\u014d\5(\25\2\u014c\u0145\3\2\2")
        buf.write("\2\u014c\u0147\3\2\2\2\u014c\u0148\3\2\2\2\u014c\u0149")
        buf.write("\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d")
        buf.write("\'\3\2\2\2\u014e\u0152\5\64\33\2\u014f\u0152\7\32\2\2")
        buf.write("\u0150\u0152\7\f\2\2\u0151\u014e\3\2\2\2\u0151\u014f\3")
        buf.write("\2\2\2\u0151\u0150\3\2\2\2\u0152)\3\2\2\2\u0153\u0157")
        buf.write("\7\20\2\2\u0154\u0156\7\33\2\2\u0155\u0154\3\2\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u016b\5")
        buf.write("&\24\2\u015b\u015d\7\33\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0165\7")
        buf.write("\22\2\2\u0162\u0164\7\33\2\2\u0163\u0162\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166\u0168\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u016a\5")
        buf.write("&\24\2\u0169\u015e\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u0171\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016e\u0170\7\33\2\2\u016f\u016e\3\2\2")
        buf.write("\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0174\3\2\2\2\u0173\u0171\3\2\2\2\u0174")
        buf.write("\u0175\7\21\2\2\u0175\u017f\3\2\2\2\u0176\u017a\7\20\2")
        buf.write("\2\u0177\u0179\7\33\2\2\u0178\u0177\3\2\2\2\u0179\u017c")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017d\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017f\7\21\2")
        buf.write("\2\u017e\u0153\3\2\2\2\u017e\u0176\3\2\2\2\u017f+\3\2")
        buf.write("\2\2\u0180\u0184\7\23\2\2\u0181\u0183\7\33\2\2\u0182\u0181")
        buf.write("\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0187\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0187\u0198\5&\24\2\u0188\u018a\7\33\2\2\u0189\u0188")
        buf.write("\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018c\u018e\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018e\u0192\7\22\2\2\u018f\u0191\7\33\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0195\u0197\5&\24\2\u0196\u018b\3\2\2\2\u0197\u019a\3")
        buf.write("\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019e")
        buf.write("\3\2\2\2\u019a\u0198\3\2\2\2\u019b\u019d\7\33\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3")
        buf.write("\2\2\2\u01a1\u01a2\7\24\2\2\u01a2\u01ac\3\2\2\2\u01a3")
        buf.write("\u01a7\7\23\2\2\u01a4\u01a6\7\33\2\2\u01a5\u01a4\3\2\2")
        buf.write("\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa")
        buf.write("\u01ac\7\24\2\2\u01ab\u0180\3\2\2\2\u01ab\u01a3\3\2\2")
        buf.write("\2\u01ac-\3\2\2\2\u01ad\u01b1\7\23\2\2\u01ae\u01b0\7\33")
        buf.write("\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4\u01c5\5\60\31\2\u01b5\u01b7\7\33")
        buf.write("\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01bb\u01bf\7\22\2\2\u01bc\u01be\7\33\2")
        buf.write("\2\u01bd\u01bc\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1")
        buf.write("\u01bf\3\2\2\2\u01c2\u01c4\5\60\31\2\u01c3\u01b8\3\2\2")
        buf.write("\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6")
        buf.write("\3\2\2\2\u01c6\u01cb\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8")
        buf.write("\u01ca\7\33\2\2\u01c9\u01c8\3\2\2\2\u01ca\u01cd\3\2\2")
        buf.write("\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ce")
        buf.write("\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01cf\7\24\2\2\u01cf")
        buf.write("\u01e0\3\2\2\2\u01d0\u01d4\7\23\2\2\u01d1\u01d3\7\33\2")
        buf.write("\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6")
        buf.write("\u01d4\3\2\2\2\u01d7\u01db\7\25\2\2\u01d8\u01da\7\33\2")
        buf.write("\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01de\u01e0\7\24\2\2\u01df\u01ad\3\2\2")
        buf.write("\2\u01df\u01d0\3\2\2\2\u01e0/\3\2\2\2\u01e1\u01e5\5\62")
        buf.write("\32\2\u01e2\u01e4\7\33\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e7")
        buf.write("\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6")
        buf.write("\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01ec\7\25\2")
        buf.write("\2\u01e9\u01eb\7\33\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ee")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01ef\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f0\5&\24\2")
        buf.write("\u01f0\61\3\2\2\2\u01f1\u01f2\7\26\2\2\u01f2\u01f7\5\6")
        buf.write("\4\2\u01f3\u01f7\7\32\2\2\u01f4\u01f7\5\64\33\2\u01f5")
        buf.write("\u01f7\7\f\2\2\u01f6\u01f1\3\2\2\2\u01f6\u01f3\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f6\u01f5\3\2\2\2\u01f7\63\3\2")
        buf.write("\2\2\u01f8\u01fa\t\3\2\2\u01f9\u01f8\3\2\2\2\u01f9\u01fa")
        buf.write("\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc\7\30\2\2\u01fc")
        buf.write("\u01fd\7\17\2\2\u01fd\u0203\7\30\2\2\u01fe\u0200\t\3\2")
        buf.write("\2\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201")
        buf.write("\3\2\2\2\u0201\u0203\7\30\2\2\u0202\u01f9\3\2\2\2\u0202")
        buf.write("\u01ff\3\2\2\2\u0203\65\3\2\2\2\u0204\u0206\t\5\2\2\u0205")
        buf.write("\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0205\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\67\3\2\2\2K;=CGLU\\bgimt|\u0083")
        buf.write("\u008a\u0090\u0096\u009d\u00a3\u00a9\u00b2\u00b9\u00c0")
        buf.write("\u00c6\u00cf\u00d3\u00d9\u00e0\u00e5\u00e9\u00ef\u00f6")
        buf.write("\u00fd\u0106\u010d\u0114\u011d\u0124\u012b\u0137\u013e")
        buf.write("\u0143\u014c\u0151\u0157\u015e\u0165\u016b\u0171\u017a")
        buf.write("\u017e\u0184\u018b\u0192\u0198\u019e\u01a7\u01ab\u01b1")
        buf.write("\u01b8\u01bf\u01c5\u01cb\u01d4\u01db\u01df\u01e5\u01ec")
        buf.write("\u01f6\u01f9\u01ff\u0202\u0207")
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
    RULE_primitive_value = 19
    RULE_list_value = 20
    RULE_set_value = 21
    RULE_object_value = 22
    RULE_pair = 23
    RULE_key = 24
    RULE_number = 25
    RULE_name = 26

    ruleNames =  [ "jql_multi_query", "jql_query", "query", "raw_text", 
                   "query_part", "query_field", "special", "special_name", 
                   "arguments", "keyword_argument", "argument", "arith_expr", 
                   "arith_operator", "factor_expr", "factor_operator", "power_expr", 
                   "power_operator", "math_value", "value", "primitive_value", 
                   "list_value", "set_value", "object_value", "pair", "key", 
                   "number", "name" ]

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
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__0) | (1 << JQLParser.T__1) | (1 << JQLParser.T__2) | (1 << JQLParser.T__3) | (1 << JQLParser.T__4) | (1 << JQLParser.T__5) | (1 << JQLParser.T__6) | (1 << JQLParser.T__7) | (1 << JQLParser.T__8) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.LPAREN) | (1 << JQLParser.RPAREN) | (1 << JQLParser.DOT) | (1 << JQLParser.LBRACKET) | (1 << JQLParser.RBRACKET) | (1 << JQLParser.COMMA) | (1 << JQLParser.LBRACE) | (1 << JQLParser.RBRACE) | (1 << JQLParser.SEMI) | (1 << JQLParser.AT) | (1 << JQLParser.DOLLAR) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS) | (1 << JQLParser.STRING) | (1 << JQLParser.WS) | (1 << JQLParser.LAST))) != 0):
                self.state = 57
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 54
                    self.match(JQLParser.AT)
                    self.state = 55
                    self.query()
                    pass

                elif la_ == 2:
                    self.state = 56
                    self.raw_text()
                    pass


                self.state = 61
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
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62
                    self.match(JQLParser.WS) 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__2) | (1 << JQLParser.T__8) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.DOLLAR) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS))) != 0):
                self.state = 68
                self.query()


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 71
                self.match(JQLParser.WS)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
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
            self.state = 79
            self.query_part()
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 80
                        self.match(JQLParser.WS)
                        self.state = 85
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 86
                    self.match(JQLParser.DOT)
                    self.state = 87
                    self.query_part() 
                self.state = 92
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
            self.state = 101 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 101
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        self.state = 94 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 93
                                self.match(JQLParser.WS)

                            else:
                                raise NoViableAltException(self)
                            self.state = 96 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                        pass

                    elif la_ == 2:
                        self.state = 98
                        self.match(JQLParser.AT)
                        self.state = 99
                        self.match(JQLParser.AT)
                        pass

                    elif la_ == 3:
                        self.state = 100
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==JQLParser.AT:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 103 
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
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.T__2, JQLParser.T__8, JQLParser.PRIMITIVE, JQLParser.DIGITS, JQLParser.LETTERS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.query_field()
                pass
            elif token in [JQLParser.DOLLAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
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
            self.state = 109
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
            self.state = 111
            self.match(JQLParser.DOLLAR)
            self.state = 112
            self.special_name()
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 113
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
            self.state = 116
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
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(JQLParser.LPAREN)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 119
                    self.match(JQLParser.WS)
                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 125
                self.argument()
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 129
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 126
                            self.match(JQLParser.WS)
                            self.state = 131
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 132
                        self.match(JQLParser.COMMA)
                        self.state = 136
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 133
                            self.match(JQLParser.WS)
                            self.state = 138
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 139
                        self.argument() 
                    self.state = 144
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 148
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 145
                            self.match(JQLParser.WS)
                            self.state = 150
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 151
                        self.match(JQLParser.COMMA)
                        self.state = 155
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 152
                            self.match(JQLParser.WS)
                            self.state = 157
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 158
                        self.keyword_argument() 
                    self.state = 163
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 164
                    self.match(JQLParser.WS)
                    self.state = 169
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 170
                self.match(JQLParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(JQLParser.LPAREN)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 173
                    self.match(JQLParser.WS)
                    self.state = 178
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 179
                self.keyword_argument()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.COMMA or _la==JQLParser.WS:
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 180
                        self.match(JQLParser.WS)
                        self.state = 185
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 186
                    self.match(JQLParser.COMMA)
                    self.state = 190
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 187
                        self.match(JQLParser.WS)
                        self.state = 192
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 193
                    self.keyword_argument()
                    self.state = 198
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 199
                self.match(JQLParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self.match(JQLParser.LPAREN)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 202
                    self.match(JQLParser.WS)
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 208
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
            self.state = 211
            self.name()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 212
                self.match(JQLParser.WS)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            self.match(JQLParser.T__0)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 219
                self.match(JQLParser.WS)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 225
                self.arith_expr()
                pass

            elif la_ == 2:
                self.state = 226
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
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.arith_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
            self.state = 233
            self.factor_expr()
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 234
                        self.match(JQLParser.WS)
                        self.state = 239
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 240
                    self.arith_operator()
                    self.state = 244
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 241
                        self.match(JQLParser.WS)
                        self.state = 246
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 247
                    self.factor_expr() 
                self.state = 253
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
            self.state = 254
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
            self.state = 256
            self.power_expr()
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 260
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 257
                        self.match(JQLParser.WS)
                        self.state = 262
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 263
                    self.factor_operator()
                    self.state = 267
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 264
                        self.match(JQLParser.WS)
                        self.state = 269
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 270
                    self.power_expr() 
                self.state = 276
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
            self.state = 277
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
            self.state = 279
            self.math_value()
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 283
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 280
                        self.match(JQLParser.WS)
                        self.state = 285
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 286
                    self.power_operator()
                    self.state = 290
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==JQLParser.WS:
                        self.state = 287
                        self.match(JQLParser.WS)
                        self.state = 292
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 293
                    self.math_value() 
                self.state = 299
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
            self.state = 300
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
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(JQLParser.AT)
                self.state = 303
                self.query()
                pass
            elif token in [JQLParser.T__1, JQLParser.T__2, JQLParser.DIGITS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.number()
                pass
            elif token in [JQLParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.match(JQLParser.LPAREN)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 306
                    self.match(JQLParser.WS)
                    self.state = 311
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 312
                self.arith_expr()
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 313
                    self.match(JQLParser.WS)
                    self.state = 318
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 319
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


        def arith_expr(self):
            return self.getTypedRuleContext(JQLParser.Arith_exprContext,0)


        def primitive_value(self):
            return self.getTypedRuleContext(JQLParser.Primitive_valueContext,0)


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
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(JQLParser.AT)
                self.state = 324
                self.query()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.list_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.set_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 327
                self.object_value()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 328
                self.arith_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 329
                self.primitive_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(JQLParser.NumberContext,0)


        def STRING(self):
            return self.getToken(JQLParser.STRING, 0)

        def PRIMITIVE(self):
            return self.getToken(JQLParser.PRIMITIVE, 0)

        def getRuleIndex(self):
            return JQLParser.RULE_primitive_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_value" ):
                listener.enterPrimitive_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_value" ):
                listener.exitPrimitive_value(self)




    def primitive_value(self):

        localctx = JQLParser.Primitive_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_primitive_value)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.T__1, JQLParser.T__2, JQLParser.DIGITS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.number()
                pass
            elif token in [JQLParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(JQLParser.STRING)
                pass
            elif token in [JQLParser.PRIMITIVE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
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
        self.enterRule(localctx, 40, self.RULE_list_value)
        self._la = 0 # Token type
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(JQLParser.LBRACKET)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 338
                    self.match(JQLParser.WS)
                    self.state = 343
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 344
                self.value()
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 348
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 345
                            self.match(JQLParser.WS)
                            self.state = 350
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 351
                        self.match(JQLParser.COMMA)
                        self.state = 355
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 352
                            self.match(JQLParser.WS)
                            self.state = 357
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 358
                        self.value() 
                    self.state = 363
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 364
                    self.match(JQLParser.WS)
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 370
                self.match(JQLParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(JQLParser.LBRACKET)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 373
                    self.match(JQLParser.WS)
                    self.state = 378
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 379
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
        self.enterRule(localctx, 42, self.RULE_set_value)
        self._la = 0 # Token type
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(JQLParser.LBRACE)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 383
                    self.match(JQLParser.WS)
                    self.state = 388
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 389
                self.value()
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 393
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 390
                            self.match(JQLParser.WS)
                            self.state = 395
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 396
                        self.match(JQLParser.COMMA)
                        self.state = 400
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 397
                            self.match(JQLParser.WS)
                            self.state = 402
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 403
                        self.value() 
                    self.state = 408
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 409
                    self.match(JQLParser.WS)
                    self.state = 414
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 415
                self.match(JQLParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(JQLParser.LBRACE)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 418
                    self.match(JQLParser.WS)
                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 424
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
        self.enterRule(localctx, 44, self.RULE_object_value)
        self._la = 0 # Token type
        try:
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.match(JQLParser.LBRACE)
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 428
                    self.match(JQLParser.WS)
                    self.state = 433
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 434
                self.pair()
                self.state = 451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 438
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 435
                            self.match(JQLParser.WS)
                            self.state = 440
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 441
                        self.match(JQLParser.COMMA)
                        self.state = 445
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.WS:
                            self.state = 442
                            self.match(JQLParser.WS)
                            self.state = 447
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 448
                        self.pair() 
                    self.state = 453
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 454
                    self.match(JQLParser.WS)
                    self.state = 459
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 460
                self.match(JQLParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.match(JQLParser.LBRACE)
                self.state = 466
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 463
                    self.match(JQLParser.WS)
                    self.state = 468
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 469
                self.match(JQLParser.SEMI)
                self.state = 473
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.WS:
                    self.state = 470
                    self.match(JQLParser.WS)
                    self.state = 475
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 476
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
        self.enterRule(localctx, 46, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.key()
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 480
                self.match(JQLParser.WS)
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 486
            self.match(JQLParser.SEMI)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.WS:
                self.state = 487
                self.match(JQLParser.WS)
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 493
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
        self.enterRule(localctx, 48, self.RULE_key)
        try:
            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.match(JQLParser.AT)
                self.state = 496
                self.query()
                pass
            elif token in [JQLParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
                self.match(JQLParser.STRING)
                pass
            elif token in [JQLParser.T__1, JQLParser.T__2, JQLParser.DIGITS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 498
                self.number()
                pass
            elif token in [JQLParser.PRIMITIVE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 499
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
        self.enterRule(localctx, 50, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
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
                self.state = 506
                self.match(JQLParser.DOT)
                self.state = 507
                self.match(JQLParser.DIGITS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JQLParser.T__1 or _la==JQLParser.T__2:
                    self.state = 508
                    _la = self._input.LA(1)
                    if not(_la==JQLParser.T__1 or _la==JQLParser.T__2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 511
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
        self.enterRule(localctx, 52, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 514
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__2) | (1 << JQLParser.T__8) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 517 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,72,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





