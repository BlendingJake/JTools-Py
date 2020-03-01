# Generated from jtools/grammar/QUERY.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QUERYParser import QUERYParser
else:
    from QUERYParser import QUERYParser

# This class defines a complete listener for a parse tree produced by QUERYParser.
class QUERYListener(ParseTreeListener):

    # Enter a parse tree produced by QUERYParser#multi_query.
    def enterMulti_query(self, ctx:QUERYParser.Multi_queryContext):
        pass

    # Exit a parse tree produced by QUERYParser#multi_query.
    def exitMulti_query(self, ctx:QUERYParser.Multi_queryContext):
        pass


    # Enter a parse tree produced by QUERYParser#raw_text.
    def enterRaw_text(self, ctx:QUERYParser.Raw_textContext):
        pass

    # Exit a parse tree produced by QUERYParser#raw_text.
    def exitRaw_text(self, ctx:QUERYParser.Raw_textContext):
        pass


    # Enter a parse tree produced by QUERYParser#query.
    def enterQuery(self, ctx:QUERYParser.QueryContext):
        pass

    # Exit a parse tree produced by QUERYParser#query.
    def exitQuery(self, ctx:QUERYParser.QueryContext):
        pass


    # Enter a parse tree produced by QUERYParser#query_part.
    def enterQuery_part(self, ctx:QUERYParser.Query_partContext):
        pass

    # Exit a parse tree produced by QUERYParser#query_part.
    def exitQuery_part(self, ctx:QUERYParser.Query_partContext):
        pass


    # Enter a parse tree produced by QUERYParser#query_field.
    def enterQuery_field(self, ctx:QUERYParser.Query_fieldContext):
        pass

    # Exit a parse tree produced by QUERYParser#query_field.
    def exitQuery_field(self, ctx:QUERYParser.Query_fieldContext):
        pass


    # Enter a parse tree produced by QUERYParser#special.
    def enterSpecial(self, ctx:QUERYParser.SpecialContext):
        pass

    # Exit a parse tree produced by QUERYParser#special.
    def exitSpecial(self, ctx:QUERYParser.SpecialContext):
        pass


    # Enter a parse tree produced by QUERYParser#special_name.
    def enterSpecial_name(self, ctx:QUERYParser.Special_nameContext):
        pass

    # Exit a parse tree produced by QUERYParser#special_name.
    def exitSpecial_name(self, ctx:QUERYParser.Special_nameContext):
        pass


    # Enter a parse tree produced by QUERYParser#arguments.
    def enterArguments(self, ctx:QUERYParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by QUERYParser#arguments.
    def exitArguments(self, ctx:QUERYParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by QUERYParser#value.
    def enterValue(self, ctx:QUERYParser.ValueContext):
        pass

    # Exit a parse tree produced by QUERYParser#value.
    def exitValue(self, ctx:QUERYParser.ValueContext):
        pass


    # Enter a parse tree produced by QUERYParser#list_value.
    def enterList_value(self, ctx:QUERYParser.List_valueContext):
        pass

    # Exit a parse tree produced by QUERYParser#list_value.
    def exitList_value(self, ctx:QUERYParser.List_valueContext):
        pass


    # Enter a parse tree produced by QUERYParser#set_value.
    def enterSet_value(self, ctx:QUERYParser.Set_valueContext):
        pass

    # Exit a parse tree produced by QUERYParser#set_value.
    def exitSet_value(self, ctx:QUERYParser.Set_valueContext):
        pass


    # Enter a parse tree produced by QUERYParser#object_value.
    def enterObject_value(self, ctx:QUERYParser.Object_valueContext):
        pass

    # Exit a parse tree produced by QUERYParser#object_value.
    def exitObject_value(self, ctx:QUERYParser.Object_valueContext):
        pass


    # Enter a parse tree produced by QUERYParser#pair.
    def enterPair(self, ctx:QUERYParser.PairContext):
        pass

    # Exit a parse tree produced by QUERYParser#pair.
    def exitPair(self, ctx:QUERYParser.PairContext):
        pass


    # Enter a parse tree produced by QUERYParser#key.
    def enterKey(self, ctx:QUERYParser.KeyContext):
        pass

    # Exit a parse tree produced by QUERYParser#key.
    def exitKey(self, ctx:QUERYParser.KeyContext):
        pass


    # Enter a parse tree produced by QUERYParser#number.
    def enterNumber(self, ctx:QUERYParser.NumberContext):
        pass

    # Exit a parse tree produced by QUERYParser#number.
    def exitNumber(self, ctx:QUERYParser.NumberContext):
        pass


    # Enter a parse tree produced by QUERYParser#name.
    def enterName(self, ctx:QUERYParser.NameContext):
        pass

    # Exit a parse tree produced by QUERYParser#name.
    def exitName(self, ctx:QUERYParser.NameContext):
        pass



del QUERYParser