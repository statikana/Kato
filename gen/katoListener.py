# Generated from kato.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .katoParser import katoParser
else:
    from katoParser import katoParser

# This class defines a complete listener for a parse tree produced by katoParser.
class katoListener(ParseTreeListener):

    # Enter a parse tree produced by katoParser#program.
    def enterProgram(self, ctx:katoParser.ProgramContext):
        pass

    # Exit a parse tree produced by katoParser#program.
    def exitProgram(self, ctx:katoParser.ProgramContext):
        pass


    # Enter a parse tree produced by katoParser#statement.
    def enterStatement(self, ctx:katoParser.StatementContext):
        pass

    # Exit a parse tree produced by katoParser#statement.
    def exitStatement(self, ctx:katoParser.StatementContext):
        pass


    # Enter a parse tree produced by katoParser#varDefinition.
    def enterVarDefinition(self, ctx:katoParser.VarDefinitionContext):
        pass

    # Exit a parse tree produced by katoParser#varDefinition.
    def exitVarDefinition(self, ctx:katoParser.VarDefinitionContext):
        pass


    # Enter a parse tree produced by katoParser#funcDefinition.
    def enterFuncDefinition(self, ctx:katoParser.FuncDefinitionContext):
        pass

    # Exit a parse tree produced by katoParser#funcDefinition.
    def exitFuncDefinition(self, ctx:katoParser.FuncDefinitionContext):
        pass


    # Enter a parse tree produced by katoParser#ExprVar.
    def enterExprVar(self, ctx:katoParser.ExprVarContext):
        pass

    # Exit a parse tree produced by katoParser#ExprVar.
    def exitExprVar(self, ctx:katoParser.ExprVarContext):
        pass


    # Enter a parse tree produced by katoParser#ExprAddSub.
    def enterExprAddSub(self, ctx:katoParser.ExprAddSubContext):
        pass

    # Exit a parse tree produced by katoParser#ExprAddSub.
    def exitExprAddSub(self, ctx:katoParser.ExprAddSubContext):
        pass


    # Enter a parse tree produced by katoParser#ExprCall.
    def enterExprCall(self, ctx:katoParser.ExprCallContext):
        pass

    # Exit a parse tree produced by katoParser#ExprCall.
    def exitExprCall(self, ctx:katoParser.ExprCallContext):
        pass


    # Enter a parse tree produced by katoParser#ExprParen.
    def enterExprParen(self, ctx:katoParser.ExprParenContext):
        pass

    # Exit a parse tree produced by katoParser#ExprParen.
    def exitExprParen(self, ctx:katoParser.ExprParenContext):
        pass


    # Enter a parse tree produced by katoParser#ExprMulDiv.
    def enterExprMulDiv(self, ctx:katoParser.ExprMulDivContext):
        pass

    # Exit a parse tree produced by katoParser#ExprMulDiv.
    def exitExprMulDiv(self, ctx:katoParser.ExprMulDivContext):
        pass


    # Enter a parse tree produced by katoParser#ExprLiteral.
    def enterExprLiteral(self, ctx:katoParser.ExprLiteralContext):
        pass

    # Exit a parse tree produced by katoParser#ExprLiteral.
    def exitExprLiteral(self, ctx:katoParser.ExprLiteralContext):
        pass


    # Enter a parse tree produced by katoParser#ExprScope.
    def enterExprScope(self, ctx:katoParser.ExprScopeContext):
        pass

    # Exit a parse tree produced by katoParser#ExprScope.
    def exitExprScope(self, ctx:katoParser.ExprScopeContext):
        pass


    # Enter a parse tree produced by katoParser#variable.
    def enterVariable(self, ctx:katoParser.VariableContext):
        pass

    # Exit a parse tree produced by katoParser#variable.
    def exitVariable(self, ctx:katoParser.VariableContext):
        pass


    # Enter a parse tree produced by katoParser#control.
    def enterControl(self, ctx:katoParser.ControlContext):
        pass

    # Exit a parse tree produced by katoParser#control.
    def exitControl(self, ctx:katoParser.ControlContext):
        pass


    # Enter a parse tree produced by katoParser#if.
    def enterIf(self, ctx:katoParser.IfContext):
        pass

    # Exit a parse tree produced by katoParser#if.
    def exitIf(self, ctx:katoParser.IfContext):
        pass


    # Enter a parse tree produced by katoParser#return.
    def enterReturn(self, ctx:katoParser.ReturnContext):
        pass

    # Exit a parse tree produced by katoParser#return.
    def exitReturn(self, ctx:katoParser.ReturnContext):
        pass


    # Enter a parse tree produced by katoParser#emit.
    def enterEmit(self, ctx:katoParser.EmitContext):
        pass

    # Exit a parse tree produced by katoParser#emit.
    def exitEmit(self, ctx:katoParser.EmitContext):
        pass


    # Enter a parse tree produced by katoParser#LiteralNumber.
    def enterLiteralNumber(self, ctx:katoParser.LiteralNumberContext):
        pass

    # Exit a parse tree produced by katoParser#LiteralNumber.
    def exitLiteralNumber(self, ctx:katoParser.LiteralNumberContext):
        pass


    # Enter a parse tree produced by katoParser#LiteralInteger.
    def enterLiteralInteger(self, ctx:katoParser.LiteralIntegerContext):
        pass

    # Exit a parse tree produced by katoParser#LiteralInteger.
    def exitLiteralInteger(self, ctx:katoParser.LiteralIntegerContext):
        pass


    # Enter a parse tree produced by katoParser#LiteralBoolean.
    def enterLiteralBoolean(self, ctx:katoParser.LiteralBooleanContext):
        pass

    # Exit a parse tree produced by katoParser#LiteralBoolean.
    def exitLiteralBoolean(self, ctx:katoParser.LiteralBooleanContext):
        pass


    # Enter a parse tree produced by katoParser#LiteralString.
    def enterLiteralString(self, ctx:katoParser.LiteralStringContext):
        pass

    # Exit a parse tree produced by katoParser#LiteralString.
    def exitLiteralString(self, ctx:katoParser.LiteralStringContext):
        pass


    # Enter a parse tree produced by katoParser#scope.
    def enterScope(self, ctx:katoParser.ScopeContext):
        pass

    # Exit a parse tree produced by katoParser#scope.
    def exitScope(self, ctx:katoParser.ScopeContext):
        pass



del katoParser