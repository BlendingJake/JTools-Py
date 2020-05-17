# Generated from jtools/grammar/JQL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JQLParser import JQLParser
else:
    from JQLParser import JQLParser

# This class defines a complete listener for a parse tree produced by JQLParser.
class JQLListener(ParseTreeListener):

    # Enter a parse tree produced by JQLParser#jql_multi_query.
    def enterJql_multi_query(self, ctx:JQLParser.Jql_multi_queryContext):
        pass

    # Exit a parse tree produced by JQLParser#jql_multi_query.
    def exitJql_multi_query(self, ctx:JQLParser.Jql_multi_queryContext):
        pass


    # Enter a parse tree produced by JQLParser#jql_query.
    def enterJql_query(self, ctx:JQLParser.Jql_queryContext):
        pass

    # Exit a parse tree produced by JQLParser#jql_query.
    def exitJql_query(self, ctx:JQLParser.Jql_queryContext):
        pass


    # Enter a parse tree produced by JQLParser#query.
    def enterQuery(self, ctx:JQLParser.QueryContext):
        pass

    # Exit a parse tree produced by JQLParser#query.
    def exitQuery(self, ctx:JQLParser.QueryContext):
        pass


    # Enter a parse tree produced by JQLParser#raw_text.
    def enterRaw_text(self, ctx:JQLParser.Raw_textContext):
        pass

    # Exit a parse tree produced by JQLParser#raw_text.
    def exitRaw_text(self, ctx:JQLParser.Raw_textContext):
        pass


    # Enter a parse tree produced by JQLParser#query_part.
    def enterQuery_part(self, ctx:JQLParser.Query_partContext):
        pass

    # Exit a parse tree produced by JQLParser#query_part.
    def exitQuery_part(self, ctx:JQLParser.Query_partContext):
        pass


    # Enter a parse tree produced by JQLParser#query_field.
    def enterQuery_field(self, ctx:JQLParser.Query_fieldContext):
        pass

    # Exit a parse tree produced by JQLParser#query_field.
    def exitQuery_field(self, ctx:JQLParser.Query_fieldContext):
        pass


    # Enter a parse tree produced by JQLParser#special.
    def enterSpecial(self, ctx:JQLParser.SpecialContext):
        pass

    # Exit a parse tree produced by JQLParser#special.
    def exitSpecial(self, ctx:JQLParser.SpecialContext):
        pass


    # Enter a parse tree produced by JQLParser#special_name.
    def enterSpecial_name(self, ctx:JQLParser.Special_nameContext):
        pass

    # Exit a parse tree produced by JQLParser#special_name.
    def exitSpecial_name(self, ctx:JQLParser.Special_nameContext):
        pass


    # Enter a parse tree produced by JQLParser#arguments.
    def enterArguments(self, ctx:JQLParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by JQLParser#arguments.
    def exitArguments(self, ctx:JQLParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by JQLParser#keyword_argument.
    def enterKeyword_argument(self, ctx:JQLParser.Keyword_argumentContext):
        pass

    # Exit a parse tree produced by JQLParser#keyword_argument.
    def exitKeyword_argument(self, ctx:JQLParser.Keyword_argumentContext):
        pass


    # Enter a parse tree produced by JQLParser#argument.
    def enterArgument(self, ctx:JQLParser.ArgumentContext):
        pass

    # Exit a parse tree produced by JQLParser#argument.
    def exitArgument(self, ctx:JQLParser.ArgumentContext):
        pass


    # Enter a parse tree produced by JQLParser#arith_expr.
    def enterArith_expr(self, ctx:JQLParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by JQLParser#arith_expr.
    def exitArith_expr(self, ctx:JQLParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by JQLParser#arith_operator.
    def enterArith_operator(self, ctx:JQLParser.Arith_operatorContext):
        pass

    # Exit a parse tree produced by JQLParser#arith_operator.
    def exitArith_operator(self, ctx:JQLParser.Arith_operatorContext):
        pass


    # Enter a parse tree produced by JQLParser#factor_expr.
    def enterFactor_expr(self, ctx:JQLParser.Factor_exprContext):
        pass

    # Exit a parse tree produced by JQLParser#factor_expr.
    def exitFactor_expr(self, ctx:JQLParser.Factor_exprContext):
        pass


    # Enter a parse tree produced by JQLParser#factor_operator.
    def enterFactor_operator(self, ctx:JQLParser.Factor_operatorContext):
        pass

    # Exit a parse tree produced by JQLParser#factor_operator.
    def exitFactor_operator(self, ctx:JQLParser.Factor_operatorContext):
        pass


    # Enter a parse tree produced by JQLParser#power_expr.
    def enterPower_expr(self, ctx:JQLParser.Power_exprContext):
        pass

    # Exit a parse tree produced by JQLParser#power_expr.
    def exitPower_expr(self, ctx:JQLParser.Power_exprContext):
        pass


    # Enter a parse tree produced by JQLParser#power_operator.
    def enterPower_operator(self, ctx:JQLParser.Power_operatorContext):
        pass

    # Exit a parse tree produced by JQLParser#power_operator.
    def exitPower_operator(self, ctx:JQLParser.Power_operatorContext):
        pass


    # Enter a parse tree produced by JQLParser#math_value.
    def enterMath_value(self, ctx:JQLParser.Math_valueContext):
        pass

    # Exit a parse tree produced by JQLParser#math_value.
    def exitMath_value(self, ctx:JQLParser.Math_valueContext):
        pass


    # Enter a parse tree produced by JQLParser#value.
    def enterValue(self, ctx:JQLParser.ValueContext):
        pass

    # Exit a parse tree produced by JQLParser#value.
    def exitValue(self, ctx:JQLParser.ValueContext):
        pass


    # Enter a parse tree produced by JQLParser#list_value.
    def enterList_value(self, ctx:JQLParser.List_valueContext):
        pass

    # Exit a parse tree produced by JQLParser#list_value.
    def exitList_value(self, ctx:JQLParser.List_valueContext):
        pass


    # Enter a parse tree produced by JQLParser#set_value.
    def enterSet_value(self, ctx:JQLParser.Set_valueContext):
        pass

    # Exit a parse tree produced by JQLParser#set_value.
    def exitSet_value(self, ctx:JQLParser.Set_valueContext):
        pass


    # Enter a parse tree produced by JQLParser#object_value.
    def enterObject_value(self, ctx:JQLParser.Object_valueContext):
        pass

    # Exit a parse tree produced by JQLParser#object_value.
    def exitObject_value(self, ctx:JQLParser.Object_valueContext):
        pass


    # Enter a parse tree produced by JQLParser#pair.
    def enterPair(self, ctx:JQLParser.PairContext):
        pass

    # Exit a parse tree produced by JQLParser#pair.
    def exitPair(self, ctx:JQLParser.PairContext):
        pass


    # Enter a parse tree produced by JQLParser#key.
    def enterKey(self, ctx:JQLParser.KeyContext):
        pass

    # Exit a parse tree produced by JQLParser#key.
    def exitKey(self, ctx:JQLParser.KeyContext):
        pass


    # Enter a parse tree produced by JQLParser#number.
    def enterNumber(self, ctx:JQLParser.NumberContext):
        pass

    # Exit a parse tree produced by JQLParser#number.
    def exitNumber(self, ctx:JQLParser.NumberContext):
        pass


    # Enter a parse tree produced by JQLParser#name.
    def enterName(self, ctx:JQLParser.NameContext):
        pass

    # Exit a parse tree produced by JQLParser#name.
    def exitName(self, ctx:JQLParser.NameContext):
        pass



del JQLParser