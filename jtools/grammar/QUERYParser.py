# Generated from jtools/grammar/QUERY.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36")
        buf.write("\u00bc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\7\2(\n\2\f\2\16\2+\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\7\3\65\n\3\f\3\16\38\13\3\3\4\3\4\3\4\7\4=\n\4\f")
        buf.write("\4\16\4@\13\4\3\5\3\5\5\5D\n\5\3\6\3\6\3\7\3\7\3\7\5\7")
        buf.write("K\n\7\3\b\3\b\3\t\3\t\3\t\3\t\7\tS\n\t\f\t\16\tV\13\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\\\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\nh\n\n\3\13\3\13\3\13\3\13\7\13n\n\13\f")
        buf.write("\13\16\13q\13\13\3\13\3\13\3\13\3\13\5\13w\n\13\3\f\3")
        buf.write("\f\3\f\3\f\7\f}\n\f\f\f\16\f\u0080\13\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u0086\n\f\3\r\3\r\3\r\3\r\7\r\u008c\n\r\f\r\16")
        buf.write("\r\u008f\13\r\3\r\3\r\3\r\3\r\3\r\5\r\u0096\n\r\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00a3\n\17\3\20\5\20\u00a6\n\20\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00ac\n\20\3\20\5\20\u00af\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\6\21\u00b6\n\21\r\21\16\21\u00b7\5\21\u00ba\n\21")
        buf.write("\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \2")
        buf.write("\5\3\2\3\3\3\2\27\30\4\2\27\27\31\33\2\u00d4\2\"\3\2\2")
        buf.write("\2\4\66\3\2\2\2\69\3\2\2\2\bC\3\2\2\2\nE\3\2\2\2\fG\3")
        buf.write("\2\2\2\16L\3\2\2\2\20[\3\2\2\2\22g\3\2\2\2\24v\3\2\2\2")
        buf.write("\26\u0085\3\2\2\2\30\u0095\3\2\2\2\32\u0097\3\2\2\2\34")
        buf.write("\u00a2\3\2\2\2\36\u00ae\3\2\2\2 \u00b9\3\2\2\2\")\5\4")
        buf.write("\3\2#$\7\3\2\2$%\5\6\4\2%&\5\4\3\2&(\3\2\2\2\'#\3\2\2")
        buf.write("\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\3\3\2\2\2+)\3\2\2\2")
        buf.write(",\65\7\34\2\2-\65\7\4\2\2.\65\7\5\2\2/\65\7\6\2\2\60\65")
        buf.write("\7\7\2\2\61\65\7\b\2\2\62\65\7\t\2\2\63\65\n\2\2\2\64")
        buf.write(",\3\2\2\2\64-\3\2\2\2\64.\3\2\2\2\64/\3\2\2\2\64\60\3")
        buf.write("\2\2\2\64\61\3\2\2\2\64\62\3\2\2\2\64\63\3\2\2\2\658\3")
        buf.write("\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\5\3\2\2\28\66\3")
        buf.write("\2\2\29>\5\b\5\2:;\7\n\2\2;=\5\b\5\2<:\3\2\2\2=@\3\2\2")
        buf.write("\2><\3\2\2\2>?\3\2\2\2?\7\3\2\2\2@>\3\2\2\2AD\5\n\6\2")
        buf.write("BD\5\f\7\2CA\3\2\2\2CB\3\2\2\2D\t\3\2\2\2EF\5 \21\2F\13")
        buf.write("\3\2\2\2GH\7\13\2\2HJ\5\16\b\2IK\5\20\t\2JI\3\2\2\2JK")
        buf.write("\3\2\2\2K\r\3\2\2\2LM\5 \21\2M\17\3\2\2\2NO\7\f\2\2OT")
        buf.write("\5\22\n\2PQ\7\r\2\2QS\5\22\n\2RP\3\2\2\2SV\3\2\2\2TR\3")
        buf.write("\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3\2\2\2WX\7\16\2\2X\\\3\2")
        buf.write("\2\2YZ\7\f\2\2Z\\\7\16\2\2[N\3\2\2\2[Y\3\2\2\2\\\21\3")
        buf.write("\2\2\2]^\7\3\2\2^h\5\6\4\2_h\5\24\13\2`h\5\26\f\2ah\5")
        buf.write("\30\r\2bh\5\36\20\2ch\7\35\2\2dh\7\17\2\2eh\7\20\2\2f")
        buf.write("h\7\21\2\2g]\3\2\2\2g_\3\2\2\2g`\3\2\2\2ga\3\2\2\2gb\3")
        buf.write("\2\2\2gc\3\2\2\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2h\23\3\2")
        buf.write("\2\2ij\7\22\2\2jo\5\22\n\2kl\7\r\2\2ln\5\22\n\2mk\3\2")
        buf.write("\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2pr\3\2\2\2qo\3\2\2\2")
        buf.write("rs\7\23\2\2sw\3\2\2\2tu\7\22\2\2uw\7\23\2\2vi\3\2\2\2")
        buf.write("vt\3\2\2\2w\25\3\2\2\2xy\7\24\2\2y~\5\22\n\2z{\7\r\2\2")
        buf.write("{}\5\22\n\2|z\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3")
        buf.write("\2\2\2\177\u0081\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\7")
        buf.write("\25\2\2\u0082\u0086\3\2\2\2\u0083\u0084\7\24\2\2\u0084")
        buf.write("\u0086\7\25\2\2\u0085x\3\2\2\2\u0085\u0083\3\2\2\2\u0086")
        buf.write("\27\3\2\2\2\u0087\u0088\7\24\2\2\u0088\u008d\5\32\16\2")
        buf.write("\u0089\u008a\7\r\2\2\u008a\u008c\5\32\16\2\u008b\u0089")
        buf.write("\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\u0091\7\25\2\2\u0091\u0096\3\2\2\2\u0092\u0093")
        buf.write("\7\24\2\2\u0093\u0094\7\26\2\2\u0094\u0096\7\25\2\2\u0095")
        buf.write("\u0087\3\2\2\2\u0095\u0092\3\2\2\2\u0096\31\3\2\2\2\u0097")
        buf.write("\u0098\5\34\17\2\u0098\u0099\7\26\2\2\u0099\u009a\5\22")
        buf.write("\n\2\u009a\33\3\2\2\2\u009b\u009c\7\3\2\2\u009c\u00a3")
        buf.write("\5\6\4\2\u009d\u00a3\7\35\2\2\u009e\u00a3\5\36\20\2\u009f")
        buf.write("\u00a3\7\17\2\2\u00a0\u00a3\7\20\2\2\u00a1\u00a3\7\21")
        buf.write("\2\2\u00a2\u009b\3\2\2\2\u00a2\u009d\3\2\2\2\u00a2\u009e")
        buf.write("\3\2\2\2\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a3\35\3\2\2\2\u00a4\u00a6\t\3\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00a8\7\32\2\2\u00a8\u00a9\7\n\2\2\u00a9\u00af")
        buf.write("\7\32\2\2\u00aa\u00ac\t\3\2\2\u00ab\u00aa\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\7\32\2")
        buf.write("\2\u00ae\u00a5\3\2\2\2\u00ae\u00ab\3\2\2\2\u00af\37\3")
        buf.write("\2\2\2\u00b0\u00ba\7\17\2\2\u00b1\u00ba\7\20\2\2\u00b2")
        buf.write("\u00ba\7\21\2\2\u00b3\u00ba\7\32\2\2\u00b4\u00b6\t\4\2")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9")
        buf.write("\u00b0\3\2\2\2\u00b9\u00b1\3\2\2\2\u00b9\u00b2\3\2\2\2")
        buf.write("\u00b9\u00b3\3\2\2\2\u00b9\u00b5\3\2\2\2\u00ba!\3\2\2")
        buf.write("\2\27)\64\66>CJT[gov~\u0085\u008d\u0095\u00a2\u00a5\u00ab")
        buf.write("\u00ae\u00b7\u00b9")
        return buf.getvalue()


class QUERYParser ( Parser ):

    grammarFileName = "QUERY.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "' '", "'\n'", "'\r'", "'\t'", 
                     "'\f'", "'@@'", "'.'", "'$'", "'('", "','", "')'", 
                     "'true'", "'false'", "'null'", "'['", "']'", "'{'", 
                     "'}'", "':'", "'-'", "'+'", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DIGITS", "LETTERS", "SYMBOL", "STRING", "WS" ]

    RULE_multi_query = 0
    RULE_raw_text = 1
    RULE_query = 2
    RULE_query_part = 3
    RULE_query_field = 4
    RULE_special = 5
    RULE_special_name = 6
    RULE_arguments = 7
    RULE_value = 8
    RULE_list_value = 9
    RULE_set_value = 10
    RULE_object_value = 11
    RULE_pair = 12
    RULE_key = 13
    RULE_number = 14
    RULE_name = 15

    ruleNames =  [ "multi_query", "raw_text", "query", "query_part", "query_field", 
                   "special", "special_name", "arguments", "value", "list_value", 
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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    DIGITS=24
    LETTERS=25
    SYMBOL=26
    STRING=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Multi_queryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def raw_text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.Raw_textContext)
            else:
                return self.getTypedRuleContext(QUERYParser.Raw_textContext,i)


        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.QueryContext)
            else:
                return self.getTypedRuleContext(QUERYParser.QueryContext,i)


        def getRuleIndex(self):
            return QUERYParser.RULE_multi_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulti_query" ):
                listener.enterMulti_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulti_query" ):
                listener.exitMulti_query(self)




    def multi_query(self):

        localctx = QUERYParser.Multi_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_multi_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.raw_text()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QUERYParser.T__0:
                self.state = 33
                self.match(QUERYParser.T__0)
                self.state = 34
                self.query()
                self.state = 35
                self.raw_text()
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


    class Raw_textContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(QUERYParser.SYMBOL)
            else:
                return self.getToken(QUERYParser.SYMBOL, i)

        def getRuleIndex(self):
            return QUERYParser.RULE_raw_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_text" ):
                listener.enterRaw_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_text" ):
                listener.exitRaw_text(self)




    def raw_text(self):

        localctx = QUERYParser.Raw_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_raw_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QUERYParser.T__1) | (1 << QUERYParser.T__2) | (1 << QUERYParser.T__3) | (1 << QUERYParser.T__4) | (1 << QUERYParser.T__5) | (1 << QUERYParser.T__6) | (1 << QUERYParser.T__7) | (1 << QUERYParser.T__8) | (1 << QUERYParser.T__9) | (1 << QUERYParser.T__10) | (1 << QUERYParser.T__11) | (1 << QUERYParser.T__12) | (1 << QUERYParser.T__13) | (1 << QUERYParser.T__14) | (1 << QUERYParser.T__15) | (1 << QUERYParser.T__16) | (1 << QUERYParser.T__17) | (1 << QUERYParser.T__18) | (1 << QUERYParser.T__19) | (1 << QUERYParser.T__20) | (1 << QUERYParser.T__21) | (1 << QUERYParser.T__22) | (1 << QUERYParser.DIGITS) | (1 << QUERYParser.LETTERS) | (1 << QUERYParser.SYMBOL) | (1 << QUERYParser.STRING) | (1 << QUERYParser.WS))) != 0):
                self.state = 50
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 42
                    self.match(QUERYParser.SYMBOL)
                    pass

                elif la_ == 2:
                    self.state = 43
                    self.match(QUERYParser.T__1)
                    pass

                elif la_ == 3:
                    self.state = 44
                    self.match(QUERYParser.T__2)
                    pass

                elif la_ == 4:
                    self.state = 45
                    self.match(QUERYParser.T__3)
                    pass

                elif la_ == 5:
                    self.state = 46
                    self.match(QUERYParser.T__4)
                    pass

                elif la_ == 6:
                    self.state = 47
                    self.match(QUERYParser.T__5)
                    pass

                elif la_ == 7:
                    self.state = 48
                    self.match(QUERYParser.T__6)
                    pass

                elif la_ == 8:
                    self.state = 49
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==QUERYParser.T__0:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass


                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
                return self.getTypedRuleContexts(QUERYParser.Query_partContext)
            else:
                return self.getTypedRuleContext(QUERYParser.Query_partContext,i)


        def getRuleIndex(self):
            return QUERYParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = QUERYParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.query_part()
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 56
                    self.match(QUERYParser.T__7)
                    self.state = 57
                    self.query_part() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            return self.getTypedRuleContext(QUERYParser.Query_fieldContext,0)


        def special(self):
            return self.getTypedRuleContext(QUERYParser.SpecialContext,0)


        def getRuleIndex(self):
            return QUERYParser.RULE_query_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_part" ):
                listener.enterQuery_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_part" ):
                listener.exitQuery_part(self)




    def query_part(self):

        localctx = QUERYParser.Query_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_query_part)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QUERYParser.T__12, QUERYParser.T__13, QUERYParser.T__14, QUERYParser.T__20, QUERYParser.T__22, QUERYParser.DIGITS, QUERYParser.LETTERS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.query_field()
                pass
            elif token in [QUERYParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
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
            return self.getTypedRuleContext(QUERYParser.NameContext,0)


        def getRuleIndex(self):
            return QUERYParser.RULE_query_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_field" ):
                listener.enterQuery_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_field" ):
                listener.exitQuery_field(self)




    def query_field(self):

        localctx = QUERYParser.Query_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_query_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
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

        def special_name(self):
            return self.getTypedRuleContext(QUERYParser.Special_nameContext,0)


        def arguments(self):
            return self.getTypedRuleContext(QUERYParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return QUERYParser.RULE_special

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial" ):
                listener.enterSpecial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial" ):
                listener.exitSpecial(self)




    def special(self):

        localctx = QUERYParser.SpecialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_special)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(QUERYParser.T__8)
            self.state = 70
            self.special_name()
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 71
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
            return self.getTypedRuleContext(QUERYParser.NameContext,0)


        def getRuleIndex(self):
            return QUERYParser.RULE_special_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_name" ):
                listener.enterSpecial_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_name" ):
                listener.exitSpecial_name(self)




    def special_name(self):

        localctx = QUERYParser.Special_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_special_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.ValueContext)
            else:
                return self.getTypedRuleContext(QUERYParser.ValueContext,i)


        def getRuleIndex(self):
            return QUERYParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = QUERYParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(QUERYParser.T__9)
                self.state = 77
                self.value()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==QUERYParser.T__10:
                    self.state = 78
                    self.match(QUERYParser.T__10)
                    self.state = 79
                    self.value()
                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 85
                self.match(QUERYParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(QUERYParser.T__9)
                self.state = 88
                self.match(QUERYParser.T__11)
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

        def query(self):
            return self.getTypedRuleContext(QUERYParser.QueryContext,0)


        def list_value(self):
            return self.getTypedRuleContext(QUERYParser.List_valueContext,0)


        def set_value(self):
            return self.getTypedRuleContext(QUERYParser.Set_valueContext,0)


        def object_value(self):
            return self.getTypedRuleContext(QUERYParser.Object_valueContext,0)


        def number(self):
            return self.getTypedRuleContext(QUERYParser.NumberContext,0)


        def STRING(self):
            return self.getToken(QUERYParser.STRING, 0)

        def getRuleIndex(self):
            return QUERYParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = QUERYParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(QUERYParser.T__0)
                self.state = 92
                self.query()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.list_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.set_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.object_value()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.number()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 97
                self.match(QUERYParser.STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.match(QUERYParser.T__12)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 99
                self.match(QUERYParser.T__13)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 100
                self.match(QUERYParser.T__14)
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.ValueContext)
            else:
                return self.getTypedRuleContext(QUERYParser.ValueContext,i)


        def getRuleIndex(self):
            return QUERYParser.RULE_list_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_value" ):
                listener.enterList_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_value" ):
                listener.exitList_value(self)




    def list_value(self):

        localctx = QUERYParser.List_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_value)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(QUERYParser.T__15)
                self.state = 104
                self.value()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==QUERYParser.T__10:
                    self.state = 105
                    self.match(QUERYParser.T__10)
                    self.state = 106
                    self.value()
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 112
                self.match(QUERYParser.T__16)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(QUERYParser.T__15)
                self.state = 115
                self.match(QUERYParser.T__16)
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.ValueContext)
            else:
                return self.getTypedRuleContext(QUERYParser.ValueContext,i)


        def getRuleIndex(self):
            return QUERYParser.RULE_set_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_value" ):
                listener.enterSet_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_value" ):
                listener.exitSet_value(self)




    def set_value(self):

        localctx = QUERYParser.Set_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_set_value)
        self._la = 0 # Token type
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(QUERYParser.T__17)
                self.state = 119
                self.value()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==QUERYParser.T__10:
                    self.state = 120
                    self.match(QUERYParser.T__10)
                    self.state = 121
                    self.value()
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 127
                self.match(QUERYParser.T__18)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(QUERYParser.T__17)
                self.state = 130
                self.match(QUERYParser.T__18)
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

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QUERYParser.PairContext)
            else:
                return self.getTypedRuleContext(QUERYParser.PairContext,i)


        def getRuleIndex(self):
            return QUERYParser.RULE_object_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_value" ):
                listener.enterObject_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_value" ):
                listener.exitObject_value(self)




    def object_value(self):

        localctx = QUERYParser.Object_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_object_value)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(QUERYParser.T__17)
                self.state = 134
                self.pair()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==QUERYParser.T__10:
                    self.state = 135
                    self.match(QUERYParser.T__10)
                    self.state = 136
                    self.pair()
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 142
                self.match(QUERYParser.T__18)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(QUERYParser.T__17)
                self.state = 145
                self.match(QUERYParser.T__19)
                self.state = 146
                self.match(QUERYParser.T__18)
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
            return self.getTypedRuleContext(QUERYParser.KeyContext,0)


        def value(self):
            return self.getTypedRuleContext(QUERYParser.ValueContext,0)


        def getRuleIndex(self):
            return QUERYParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = QUERYParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.key()
            self.state = 150
            self.match(QUERYParser.T__19)
            self.state = 151
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

        def query(self):
            return self.getTypedRuleContext(QUERYParser.QueryContext,0)


        def STRING(self):
            return self.getToken(QUERYParser.STRING, 0)

        def number(self):
            return self.getTypedRuleContext(QUERYParser.NumberContext,0)


        def getRuleIndex(self):
            return QUERYParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = QUERYParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_key)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QUERYParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(QUERYParser.T__0)
                self.state = 154
                self.query()
                pass
            elif token in [QUERYParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(QUERYParser.STRING)
                pass
            elif token in [QUERYParser.T__20, QUERYParser.T__21, QUERYParser.DIGITS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.number()
                pass
            elif token in [QUERYParser.T__12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.match(QUERYParser.T__12)
                pass
            elif token in [QUERYParser.T__13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.match(QUERYParser.T__13)
                pass
            elif token in [QUERYParser.T__14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 159
                self.match(QUERYParser.T__14)
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
                return self.getTokens(QUERYParser.DIGITS)
            else:
                return self.getToken(QUERYParser.DIGITS, i)

        def getRuleIndex(self):
            return QUERYParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = QUERYParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QUERYParser.T__20 or _la==QUERYParser.T__21:
                    self.state = 162
                    _la = self._input.LA(1)
                    if not(_la==QUERYParser.T__20 or _la==QUERYParser.T__21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 165
                self.match(QUERYParser.DIGITS)
                self.state = 166
                self.match(QUERYParser.T__7)
                self.state = 167
                self.match(QUERYParser.DIGITS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==QUERYParser.T__20 or _la==QUERYParser.T__21:
                    self.state = 168
                    _la = self._input.LA(1)
                    if not(_la==QUERYParser.T__20 or _la==QUERYParser.T__21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 171
                self.match(QUERYParser.DIGITS)
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

        def DIGITS(self, i:int=None):
            if i is None:
                return self.getTokens(QUERYParser.DIGITS)
            else:
                return self.getToken(QUERYParser.DIGITS, i)

        def LETTERS(self, i:int=None):
            if i is None:
                return self.getTokens(QUERYParser.LETTERS)
            else:
                return self.getToken(QUERYParser.LETTERS, i)

        def getRuleIndex(self):
            return QUERYParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = QUERYParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(QUERYParser.T__12)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(QUERYParser.T__13)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(QUERYParser.T__14)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.match(QUERYParser.DIGITS)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 179 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 178
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QUERYParser.T__20) | (1 << QUERYParser.T__22) | (1 << QUERYParser.DIGITS) | (1 << QUERYParser.LETTERS))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 181 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





