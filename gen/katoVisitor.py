# Generated from kato.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .katoParser import katoParser
else:
    from katoParser import katoParser

# This class defines a complete generic visitor for a parse tree produced by katoParser.

class katoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by katoParser#program.
    def visitProgram(self, ctx:katoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#statement.
    def visitStatement(self, ctx:katoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#varDefinition.
    def visitVarDefinition(self, ctx:katoParser.VarDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#funcDefinition.
    def visitFuncDefinition(self, ctx:katoParser.FuncDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#ExprVar.
    def visitExprVar(self, ctx:katoParser.ExprVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#ExprAddSub.
    def visitExprAddSub(self, ctx:katoParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#ExprCall.
    def visitExprCall(self, ctx:katoParser.ExprCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#ExprParen.
    def visitExprParen(self, ctx:katoParser.ExprParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#ExprMulDiv.
    def visitExprMulDiv(self, ctx:katoParser.ExprMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#ExprLiteral.
    def visitExprLiteral(self, ctx:katoParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#ExprScope.
    def visitExprScope(self, ctx:katoParser.ExprScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#variable.
    def visitVariable(self, ctx:katoParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#control.
    def visitControl(self, ctx:katoParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#if.
    def visitIf(self, ctx:katoParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#return.
    def visitReturn(self, ctx:katoParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#emit.
    def visitEmit(self, ctx:katoParser.EmitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#LiteralNumber.
    def visitLiteralNumber(self, ctx:katoParser.LiteralNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#LiteralInteger.
    def visitLiteralInteger(self, ctx:katoParser.LiteralIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#LiteralBoolean.
    def visitLiteralBoolean(self, ctx:katoParser.LiteralBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#LiteralString.
    def visitLiteralString(self, ctx:katoParser.LiteralStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by katoParser#scope.
    def visitScope(self, ctx:katoParser.ScopeContext):
        return self.visitChildren(ctx)



del katoParser