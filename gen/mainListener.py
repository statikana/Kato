# Generated from main.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete listener for a parse tree produced by mainParser.
class mainListener(ParseTreeListener):

    # Enter a parse tree produced by mainParser#program.
    def enterProgram(self, ctx:mainParser.ProgramContext):
        pass

    # Exit a parse tree produced by mainParser#program.
    def exitProgram(self, ctx:mainParser.ProgramContext):
        pass


    # Enter a parse tree produced by mainParser#statement.
    def enterStatement(self, ctx:mainParser.StatementContext):
        pass

    # Exit a parse tree produced by mainParser#statement.
    def exitStatement(self, ctx:mainParser.StatementContext):
        pass


    # Enter a parse tree produced by mainParser#varDefinition.
    def enterVarDefinition(self, ctx:mainParser.VarDefinitionContext):
        pass

    # Exit a parse tree produced by mainParser#varDefinition.
    def exitVarDefinition(self, ctx:mainParser.VarDefinitionContext):
        pass


    # Enter a parse tree produced by mainParser#ExprVar.
    def enterExprVar(self, ctx:mainParser.ExprVarContext):
        pass

    # Exit a parse tree produced by mainParser#ExprVar.
    def exitExprVar(self, ctx:mainParser.ExprVarContext):
        pass


    # Enter a parse tree produced by mainParser#ExprAddSub.
    def enterExprAddSub(self, ctx:mainParser.ExprAddSubContext):
        pass

    # Exit a parse tree produced by mainParser#ExprAddSub.
    def exitExprAddSub(self, ctx:mainParser.ExprAddSubContext):
        pass


    # Enter a parse tree produced by mainParser#ExprParen.
    def enterExprParen(self, ctx:mainParser.ExprParenContext):
        pass

    # Exit a parse tree produced by mainParser#ExprParen.
    def exitExprParen(self, ctx:mainParser.ExprParenContext):
        pass


    # Enter a parse tree produced by mainParser#ExprMulDiv.
    def enterExprMulDiv(self, ctx:mainParser.ExprMulDivContext):
        pass

    # Exit a parse tree produced by mainParser#ExprMulDiv.
    def exitExprMulDiv(self, ctx:mainParser.ExprMulDivContext):
        pass


    # Enter a parse tree produced by mainParser#ExprLiteral.
    def enterExprLiteral(self, ctx:mainParser.ExprLiteralContext):
        pass

    # Exit a parse tree produced by mainParser#ExprLiteral.
    def exitExprLiteral(self, ctx:mainParser.ExprLiteralContext):
        pass


    # Enter a parse tree produced by mainParser#ExprScope.
    def enterExprScope(self, ctx:mainParser.ExprScopeContext):
        pass

    # Exit a parse tree produced by mainParser#ExprScope.
    def exitExprScope(self, ctx:mainParser.ExprScopeContext):
        pass


    # Enter a parse tree produced by mainParser#variable.
    def enterVariable(self, ctx:mainParser.VariableContext):
        pass

    # Exit a parse tree produced by mainParser#variable.
    def exitVariable(self, ctx:mainParser.VariableContext):
        pass


    # Enter a parse tree produced by mainParser#control.
    def enterControl(self, ctx:mainParser.ControlContext):
        pass

    # Exit a parse tree produced by mainParser#control.
    def exitControl(self, ctx:mainParser.ControlContext):
        pass


    # Enter a parse tree produced by mainParser#if.
    def enterIf(self, ctx:mainParser.IfContext):
        pass

    # Exit a parse tree produced by mainParser#if.
    def exitIf(self, ctx:mainParser.IfContext):
        pass


    # Enter a parse tree produced by mainParser#return.
    def enterReturn(self, ctx:mainParser.ReturnContext):
        pass

    # Exit a parse tree produced by mainParser#return.
    def exitReturn(self, ctx:mainParser.ReturnContext):
        pass


    # Enter a parse tree produced by mainParser#emit.
    def enterEmit(self, ctx:mainParser.EmitContext):
        pass

    # Exit a parse tree produced by mainParser#emit.
    def exitEmit(self, ctx:mainParser.EmitContext):
        pass


    # Enter a parse tree produced by mainParser#NumberLiteral.
    def enterNumberLiteral(self, ctx:mainParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by mainParser#NumberLiteral.
    def exitNumberLiteral(self, ctx:mainParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by mainParser#IntegerLiteral.
    def enterIntegerLiteral(self, ctx:mainParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by mainParser#IntegerLiteral.
    def exitIntegerLiteral(self, ctx:mainParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by mainParser#StringLiteral.
    def enterStringLiteral(self, ctx:mainParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by mainParser#StringLiteral.
    def exitStringLiteral(self, ctx:mainParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by mainParser#scope.
    def enterScope(self, ctx:mainParser.ScopeContext):
        pass

    # Exit a parse tree produced by mainParser#scope.
    def exitScope(self, ctx:mainParser.ScopeContext):
        pass



del mainParser