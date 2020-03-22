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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("\u0140\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\7\2(\n\2\f\2\16\2+\13\2\3\3\5\3.\n\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\7\4\65\n\4\f\4\16\48\13\4\3\5\6\5;\n\5\r\5\16")
        buf.write("\5<\3\5\3\5\3\5\6\5B\n\5\r\5\16\5C\3\6\3\6\5\6H\n\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\5\bO\n\b\3\t\3\t\3\n\3\n\7\nU\n\n\f")
        buf.write("\n\16\nX\13\n\3\n\3\n\7\n\\\n\n\f\n\16\n_\13\n\3\n\3\n")
        buf.write("\7\nc\n\n\f\n\16\nf\13\n\3\n\7\ni\n\n\f\n\16\nl\13\n\3")
        buf.write("\n\7\no\n\n\f\n\16\nr\13\n\3\n\3\n\3\n\3\n\7\nx\n\n\f")
        buf.write("\n\16\n{\13\n\3\n\5\n~\n\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u0088\n\13\3\f\3\f\7\f\u008c\n\f\f")
        buf.write("\f\16\f\u008f\13\f\3\f\3\f\7\f\u0093\n\f\f\f\16\f\u0096")
        buf.write("\13\f\3\f\3\f\7\f\u009a\n\f\f\f\16\f\u009d\13\f\3\f\7")
        buf.write("\f\u00a0\n\f\f\f\16\f\u00a3\13\f\3\f\7\f\u00a6\n\f\f\f")
        buf.write("\16\f\u00a9\13\f\3\f\3\f\3\f\3\f\7\f\u00af\n\f\f\f\16")
        buf.write("\f\u00b2\13\f\3\f\5\f\u00b5\n\f\3\r\3\r\7\r\u00b9\n\r")
        buf.write("\f\r\16\r\u00bc\13\r\3\r\3\r\7\r\u00c0\n\r\f\r\16\r\u00c3")
        buf.write("\13\r\3\r\3\r\7\r\u00c7\n\r\f\r\16\r\u00ca\13\r\3\r\7")
        buf.write("\r\u00cd\n\r\f\r\16\r\u00d0\13\r\3\r\7\r\u00d3\n\r\f\r")
        buf.write("\16\r\u00d6\13\r\3\r\3\r\3\r\3\r\7\r\u00dc\n\r\f\r\16")
        buf.write("\r\u00df\13\r\3\r\5\r\u00e2\n\r\3\16\3\16\7\16\u00e6\n")
        buf.write("\16\f\16\16\16\u00e9\13\16\3\16\3\16\7\16\u00ed\n\16\f")
        buf.write("\16\16\16\u00f0\13\16\3\16\3\16\7\16\u00f4\n\16\f\16\16")
        buf.write("\16\u00f7\13\16\3\16\7\16\u00fa\n\16\f\16\16\16\u00fd")
        buf.write("\13\16\3\16\7\16\u0100\n\16\f\16\16\16\u0103\13\16\3\16")
        buf.write("\3\16\3\16\3\16\7\16\u0109\n\16\f\16\16\16\u010c\13\16")
        buf.write("\3\16\3\16\7\16\u0110\n\16\f\16\16\16\u0113\13\16\3\16")
        buf.write("\5\16\u0116\n\16\3\17\3\17\7\17\u011a\n\17\f\17\16\17")
        buf.write("\u011d\13\17\3\17\3\17\7\17\u0121\n\17\f\17\16\17\u0124")
        buf.write("\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\5\20\u012d\n")
        buf.write("\20\3\21\5\21\u0130\n\21\3\21\3\21\3\21\3\21\5\21\u0136")
        buf.write("\n\21\3\21\5\21\u0139\n\21\3\22\6\22\u013c\n\22\r\22\16")
        buf.write("\22\u013d\3\22\2\2\23\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"\2\5\3\2\20\20\3\2\3\4\5\2\3\3\5\6\22\23\2\u0164")
        buf.write("\2)\3\2\2\2\4-\3\2\2\2\6\61\3\2\2\2\bA\3\2\2\2\nG\3\2")
        buf.write("\2\2\fI\3\2\2\2\16K\3\2\2\2\20P\3\2\2\2\22}\3\2\2\2\24")
        buf.write("\u0087\3\2\2\2\26\u00b4\3\2\2\2\30\u00e1\3\2\2\2\32\u0115")
        buf.write("\3\2\2\2\34\u0117\3\2\2\2\36\u012c\3\2\2\2 \u0138\3\2")
        buf.write("\2\2\"\u013b\3\2\2\2$%\7\20\2\2%(\5\6\4\2&(\5\b\5\2\'")
        buf.write("$\3\2\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\3")
        buf.write("\3\2\2\2+)\3\2\2\2,.\5\6\4\2-,\3\2\2\2-.\3\2\2\2./\3\2")
        buf.write("\2\2/\60\7\2\2\3\60\5\3\2\2\2\61\66\5\n\6\2\62\63\7\t")
        buf.write("\2\2\63\65\5\n\6\2\64\62\3\2\2\2\658\3\2\2\2\66\64\3\2")
        buf.write("\2\2\66\67\3\2\2\2\67\7\3\2\2\28\66\3\2\2\29;\7\26\2\2")
        buf.write(":9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=B\3\2\2\2>?\7")
        buf.write("\20\2\2?B\7\20\2\2@B\n\2\2\2A:\3\2\2\2A>\3\2\2\2A@\3\2")
        buf.write("\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\t\3\2\2\2EH\5\f\7")
        buf.write("\2FH\5\16\b\2GE\3\2\2\2GF\3\2\2\2H\13\3\2\2\2IJ\5\"\22")
        buf.write("\2J\r\3\2\2\2KL\7\21\2\2LN\5\20\t\2MO\5\22\n\2NM\3\2\2")
        buf.write("\2NO\3\2\2\2O\17\3\2\2\2PQ\5\"\22\2Q\21\3\2\2\2RV\7\7")
        buf.write("\2\2SU\7\25\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2")
        buf.write("\2WY\3\2\2\2XV\3\2\2\2Yj\5\24\13\2Z\\\7\25\2\2[Z\3\2\2")
        buf.write("\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2")
        buf.write("`d\7\f\2\2ac\7\25\2\2ba\3\2\2\2cf\3\2\2\2db\3\2\2\2de")
        buf.write("\3\2\2\2eg\3\2\2\2fd\3\2\2\2gi\5\24\13\2h]\3\2\2\2il\3")
        buf.write("\2\2\2jh\3\2\2\2jk\3\2\2\2kp\3\2\2\2lj\3\2\2\2mo\7\25")
        buf.write("\2\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qs\3\2\2\2")
        buf.write("rp\3\2\2\2st\7\b\2\2t~\3\2\2\2uy\7\7\2\2vx\7\25\2\2wv")
        buf.write("\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{y\3\2")
        buf.write("\2\2|~\7\b\2\2}R\3\2\2\2}u\3\2\2\2~\23\3\2\2\2\177\u0080")
        buf.write("\7\20\2\2\u0080\u0088\5\6\4\2\u0081\u0088\5\26\f\2\u0082")
        buf.write("\u0088\5\30\r\2\u0083\u0088\5\32\16\2\u0084\u0088\5 \21")
        buf.write("\2\u0085\u0088\7\24\2\2\u0086\u0088\7\6\2\2\u0087\177")
        buf.write("\3\2\2\2\u0087\u0081\3\2\2\2\u0087\u0082\3\2\2\2\u0087")
        buf.write("\u0083\3\2\2\2\u0087\u0084\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\25\3\2\2\2\u0089\u008d\7\n")
        buf.write("\2\2\u008a\u008c\7\25\2\2\u008b\u008a\3\2\2\2\u008c\u008f")
        buf.write("\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u00a1\5\24\13")
        buf.write("\2\u0091\u0093\7\25\2\2\u0092\u0091\3\2\2\2\u0093\u0096")
        buf.write("\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0097\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u009b\7\f\2\2")
        buf.write("\u0098\u009a\7\25\2\2\u0099\u0098\3\2\2\2\u009a\u009d")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u00a0\5\24\13")
        buf.write("\2\u009f\u0094\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a7\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a6\7\25\2\2\u00a5\u00a4\3\2\2")
        buf.write("\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa")
        buf.write("\u00ab\7\13\2\2\u00ab\u00b5\3\2\2\2\u00ac\u00b0\7\n\2")
        buf.write("\2\u00ad\u00af\7\25\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\u00b3\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\7\13\2")
        buf.write("\2\u00b4\u0089\3\2\2\2\u00b4\u00ac\3\2\2\2\u00b5\27\3")
        buf.write("\2\2\2\u00b6\u00ba\7\r\2\2\u00b7\u00b9\7\25\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bd\u00ce\5\24\13\2\u00be\u00c0\7\25\2\2\u00bf")
        buf.write("\u00be\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3")
        buf.write("\2\2\2\u00c4\u00c8\7\f\2\2\u00c5\u00c7\7\25\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8\3")
        buf.write("\2\2\2\u00cb\u00cd\5\24\13\2\u00cc\u00c1\3\2\2\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d4\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d3\7")
        buf.write("\25\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d7\u00d8\7\16\2\2\u00d8\u00e2")
        buf.write("\3\2\2\2\u00d9\u00dd\7\r\2\2\u00da\u00dc\7\25\2\2\u00db")
        buf.write("\u00da\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\u00e0\3\2\2\2\u00df\u00dd\3")
        buf.write("\2\2\2\u00e0\u00e2\7\16\2\2\u00e1\u00b6\3\2\2\2\u00e1")
        buf.write("\u00d9\3\2\2\2\u00e2\31\3\2\2\2\u00e3\u00e7\7\r\2\2\u00e4")
        buf.write("\u00e6\7\25\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e9\3\2\2")
        buf.write("\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea")
        buf.write("\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00fb\5\34\17\2\u00eb")
        buf.write("\u00ed\7\25\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f5\7\f\2\2\u00f2")
        buf.write("\u00f4\7\25\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00f7\3\2\2")
        buf.write("\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00fa\5\34\17\2\u00f9")
        buf.write("\u00ee\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fc\3\2\2\2\u00fc\u0101\3\2\2\2\u00fd\u00fb\3")
        buf.write("\2\2\2\u00fe\u0100\7\25\2\2\u00ff\u00fe\3\2\2\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\7")
        buf.write("\16\2\2\u0105\u0116\3\2\2\2\u0106\u010a\7\r\2\2\u0107")
        buf.write("\u0109\7\25\2\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2")
        buf.write("\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010d")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u0111\7\17\2\2\u010e")
        buf.write("\u0110\7\25\2\2\u010f\u010e\3\2\2\2\u0110\u0113\3\2\2")
        buf.write("\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114")
        buf.write("\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0116\7\16\2\2\u0115")
        buf.write("\u00e3\3\2\2\2\u0115\u0106\3\2\2\2\u0116\33\3\2\2\2\u0117")
        buf.write("\u011b\5\36\20\2\u0118\u011a\7\25\2\2\u0119\u0118\3\2")
        buf.write("\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c")
        buf.write("\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011e")
        buf.write("\u0122\7\17\2\2\u011f\u0121\7\25\2\2\u0120\u011f\3\2\2")
        buf.write("\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u0123\u0125\3\2\2\2\u0124\u0122\3\2\2\2\u0125")
        buf.write("\u0126\5\24\13\2\u0126\35\3\2\2\2\u0127\u0128\7\20\2\2")
        buf.write("\u0128\u012d\5\6\4\2\u0129\u012d\7\24\2\2\u012a\u012d")
        buf.write("\5 \21\2\u012b\u012d\7\6\2\2\u012c\u0127\3\2\2\2\u012c")
        buf.write("\u0129\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2")
        buf.write("\u012d\37\3\2\2\2\u012e\u0130\t\3\2\2\u012f\u012e\3\2")
        buf.write("\2\2\u012f\u0130\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132")
        buf.write("\7\22\2\2\u0132\u0133\7\t\2\2\u0133\u0139\7\22\2\2\u0134")
        buf.write("\u0136\t\3\2\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137\u0139\7\22\2\2\u0138\u012f")
        buf.write("\3\2\2\2\u0138\u0135\3\2\2\2\u0139!\3\2\2\2\u013a\u013c")
        buf.write("\t\4\2\2\u013b\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e#\3\2\2\2\60\'")
        buf.write(")-\66<ACGNV]djpy}\u0087\u008d\u0094\u009b\u00a1\u00a7")
        buf.write("\u00b0\u00b4\u00ba\u00c1\u00c8\u00ce\u00d4\u00dd\u00e1")
        buf.write("\u00e7\u00ee\u00f5\u00fb\u0101\u010a\u0111\u0115\u011b")
        buf.write("\u0122\u012c\u012f\u0135\u0138\u013d")
        return buf.getvalue()


class JQLParser ( Parser ):

    grammarFileName = "JQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'+'", "'_'", "<INVALID>", "'('", 
                     "')'", "'.'", "'['", "']'", "','", "'{'", "'}'", "':'", 
                     "'@'", "'$'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PRIMITIVE", "LPAREN", "RPAREN", "DOT", "LBRACKET", 
                      "RBRACKET", "COMMA", "LBRACE", "RBRACE", "SEMI", "AT", 
                      "DOLLAR", "DIGITS", "LETTERS", "STRING", "SPACE", 
                      "WS", "LAST" ]

    RULE_jql_multi_query = 0
    RULE_jql_query = 1
    RULE_query = 2
    RULE_raw_text = 3
    RULE_query_part = 4
    RULE_query_field = 5
    RULE_special = 6
    RULE_special_name = 7
    RULE_arguments = 8
    RULE_value = 9
    RULE_list_value = 10
    RULE_set_value = 11
    RULE_object_value = 12
    RULE_pair = 13
    RULE_key = 14
    RULE_number = 15
    RULE_name = 16

    ruleNames =  [ "jql_multi_query", "jql_query", "query", "raw_text", 
                   "query_part", "query_field", "special", "special_name", 
                   "arguments", "value", "list_value", "set_value", "object_value", 
                   "pair", "key", "number", "name" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    PRIMITIVE=4
    LPAREN=5
    RPAREN=6
    DOT=7
    LBRACKET=8
    RBRACKET=9
    COMMA=10
    LBRACE=11
    RBRACE=12
    SEMI=13
    AT=14
    DOLLAR=15
    DIGITS=16
    LETTERS=17
    STRING=18
    SPACE=19
    WS=20
    LAST=21

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
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__0) | (1 << JQLParser.T__1) | (1 << JQLParser.T__2) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.LPAREN) | (1 << JQLParser.RPAREN) | (1 << JQLParser.DOT) | (1 << JQLParser.LBRACKET) | (1 << JQLParser.RBRACKET) | (1 << JQLParser.COMMA) | (1 << JQLParser.LBRACE) | (1 << JQLParser.RBRACE) | (1 << JQLParser.SEMI) | (1 << JQLParser.AT) | (1 << JQLParser.DOLLAR) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS) | (1 << JQLParser.STRING) | (1 << JQLParser.SPACE) | (1 << JQLParser.WS) | (1 << JQLParser.LAST))) != 0):
                self.state = 37
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 34
                    self.match(JQLParser.AT)
                    self.state = 35
                    self.query()
                    pass

                elif la_ == 2:
                    self.state = 36
                    self.raw_text()
                    pass


                self.state = 41
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
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__0) | (1 << JQLParser.T__2) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.DOLLAR) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS))) != 0):
                self.state = 42
                self.query()


            self.state = 45
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.query_part()
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 48
                    self.match(JQLParser.DOT)
                    self.state = 49
                    self.query_part() 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            self.state = 63 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        self.state = 56 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 55
                                self.match(JQLParser.WS)

                            else:
                                raise NoViableAltException(self)
                            self.state = 58 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                        pass

                    elif la_ == 2:
                        self.state = 60
                        self.match(JQLParser.AT)
                        self.state = 61
                        self.match(JQLParser.AT)
                        pass

                    elif la_ == 3:
                        self.state = 62
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==JQLParser.AT:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 65 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.T__0, JQLParser.T__2, JQLParser.PRIMITIVE, JQLParser.DIGITS, JQLParser.LETTERS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.query_field()
                pass
            elif token in [JQLParser.DOLLAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
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
            self.state = 71
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
            self.state = 73
            self.match(JQLParser.DOLLAR)
            self.state = 74
            self.special_name()
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 75
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
            self.state = 78
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JQLParser.ValueContext)
            else:
                return self.getTypedRuleContext(JQLParser.ValueContext,i)


        def RPAREN(self):
            return self.getToken(JQLParser.RPAREN, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.SPACE)
            else:
                return self.getToken(JQLParser.SPACE, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.COMMA)
            else:
                return self.getToken(JQLParser.COMMA, i)

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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(JQLParser.LPAREN)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 81
                    self.match(JQLParser.SPACE)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.value()
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 91
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.SPACE:
                            self.state = 88
                            self.match(JQLParser.SPACE)
                            self.state = 93
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 94
                        self.match(JQLParser.COMMA)
                        self.state = 98
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.SPACE:
                            self.state = 95
                            self.match(JQLParser.SPACE)
                            self.state = 100
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 101
                        self.value() 
                    self.state = 106
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 107
                    self.match(JQLParser.SPACE)
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 113
                self.match(JQLParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(JQLParser.LPAREN)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 116
                    self.match(JQLParser.SPACE)
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 122
                self.match(JQLParser.RPAREN)
                pass


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
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.match(JQLParser.AT)
                self.state = 126
                self.query()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.list_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.set_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.object_value()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.number()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.match(JQLParser.STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 132
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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.SPACE)
            else:
                return self.getToken(JQLParser.SPACE, i)

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
        self.enterRule(localctx, 20, self.RULE_list_value)
        self._la = 0 # Token type
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(JQLParser.LBRACKET)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 136
                    self.match(JQLParser.SPACE)
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 142
                self.value()
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 146
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.SPACE:
                            self.state = 143
                            self.match(JQLParser.SPACE)
                            self.state = 148
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 149
                        self.match(JQLParser.COMMA)
                        self.state = 153
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.SPACE:
                            self.state = 150
                            self.match(JQLParser.SPACE)
                            self.state = 155
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 156
                        self.value() 
                    self.state = 161
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 162
                    self.match(JQLParser.SPACE)
                    self.state = 167
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 168
                self.match(JQLParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(JQLParser.LBRACKET)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 171
                    self.match(JQLParser.SPACE)
                    self.state = 176
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 177
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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.SPACE)
            else:
                return self.getToken(JQLParser.SPACE, i)

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
        self.enterRule(localctx, 22, self.RULE_set_value)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(JQLParser.LBRACE)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 181
                    self.match(JQLParser.SPACE)
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 187
                self.value()
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 191
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.SPACE:
                            self.state = 188
                            self.match(JQLParser.SPACE)
                            self.state = 193
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 194
                        self.match(JQLParser.COMMA)
                        self.state = 198
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.SPACE:
                            self.state = 195
                            self.match(JQLParser.SPACE)
                            self.state = 200
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 201
                        self.value() 
                    self.state = 206
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 207
                    self.match(JQLParser.SPACE)
                    self.state = 212
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 213
                self.match(JQLParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(JQLParser.LBRACE)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 216
                    self.match(JQLParser.SPACE)
                    self.state = 221
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 222
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

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.SPACE)
            else:
                return self.getToken(JQLParser.SPACE, i)

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
        self.enterRule(localctx, 24, self.RULE_object_value)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(JQLParser.LBRACE)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 226
                    self.match(JQLParser.SPACE)
                    self.state = 231
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 232
                self.pair()
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 236
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.SPACE:
                            self.state = 233
                            self.match(JQLParser.SPACE)
                            self.state = 238
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 239
                        self.match(JQLParser.COMMA)
                        self.state = 243
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==JQLParser.SPACE:
                            self.state = 240
                            self.match(JQLParser.SPACE)
                            self.state = 245
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 246
                        self.pair() 
                    self.state = 251
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 252
                    self.match(JQLParser.SPACE)
                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 258
                self.match(JQLParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(JQLParser.LBRACE)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 261
                    self.match(JQLParser.SPACE)
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 267
                self.match(JQLParser.SEMI)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JQLParser.SPACE:
                    self.state = 268
                    self.match(JQLParser.SPACE)
                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 274
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


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(JQLParser.SPACE)
            else:
                return self.getToken(JQLParser.SPACE, i)

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
        self.enterRule(localctx, 26, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.key()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.SPACE:
                self.state = 278
                self.match(JQLParser.SPACE)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 284
            self.match(JQLParser.SEMI)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JQLParser.SPACE:
                self.state = 285
                self.match(JQLParser.SPACE)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
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
        self.enterRule(localctx, 28, self.RULE_key)
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JQLParser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.match(JQLParser.AT)
                self.state = 294
                self.query()
                pass
            elif token in [JQLParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(JQLParser.STRING)
                pass
            elif token in [JQLParser.T__0, JQLParser.T__1, JQLParser.DIGITS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.number()
                pass
            elif token in [JQLParser.PRIMITIVE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 297
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
        self.enterRule(localctx, 30, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JQLParser.T__0 or _la==JQLParser.T__1:
                    self.state = 300
                    _la = self._input.LA(1)
                    if not(_la==JQLParser.T__0 or _la==JQLParser.T__1):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 303
                self.match(JQLParser.DIGITS)
                self.state = 304
                self.match(JQLParser.DOT)
                self.state = 305
                self.match(JQLParser.DIGITS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==JQLParser.T__0 or _la==JQLParser.T__1:
                    self.state = 306
                    _la = self._input.LA(1)
                    if not(_la==JQLParser.T__0 or _la==JQLParser.T__1):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 309
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
        self.enterRule(localctx, 32, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 312
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JQLParser.T__0) | (1 << JQLParser.T__2) | (1 << JQLParser.PRIMITIVE) | (1 << JQLParser.DIGITS) | (1 << JQLParser.LETTERS))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 315 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





