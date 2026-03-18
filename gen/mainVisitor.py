# Generated from main.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .mainParser import mainParser
else:
    from mainParser import mainParser

# This class defines a complete generic visitor for a parse tree produced by mainParser.

class mainVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mainParser#program.
    def visitProgram(self, ctx:mainParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#statement.
    def visitStatement(self, ctx:mainParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#varDefinition.
    def visitVarDefinition(self, ctx:mainParser.VarDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#ExprVar.
    def visitExprVar(self, ctx:mainParser.ExprVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#ExprAddSub.
    def visitExprAddSub(self, ctx:mainParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#ExprParen.
    def visitExprParen(self, ctx:mainParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#ExprMulDiv.
    def visitExprMulDiv(self, ctx:mainParser.ExprMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#ExprLiteral.
    def visitExprLiteral(self, ctx:mainParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#ExprScope.
    def visitExprScope(self, ctx:mainParser.ExprScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#variable.
    def visitVariable(self, ctx:mainParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#control.
    def visitControl(self, ctx:mainParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#if.
    def visitIf(self, ctx:mainParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#return.
    def visitReturn(self, ctx:mainParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#emit.
    def visitEmit(self, ctx:mainParser.EmitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#NumberLiteral.
    def visitNumberLiteral(self, ctx:mainParser.NumberLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#IntegerLiteral.
    def visitIntegerLiteral(self, ctx:mainParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#StringLiteral.
    def visitStringLiteral(self, ctx:mainParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mainParser#scope.
    def visitScope(self, ctx:mainParser.ScopeContext):
        return self.visitChildren(ctx)



del mainParser