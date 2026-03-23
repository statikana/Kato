# type: ignore
# antlr4 is horribly, horribly typed.

from antlr4.tree.Tree import Tree

from gen.katoLexer import katoLexer as KatoLexer
from gen.katoParser import katoParser as KatoParser
from gen.katoVisitor import katoVisitor as KatoVisitor

from .ast import *
from .datatype.datatype import *

class ASTVisitor(KatoVisitor):
    def visit(self, tree: Tree) -> ASTNode:
        return super().visit(tree)
    
    def visitProgram(self, ctx: KatoParser.ProgramContext):
        print("program", ctx.getText())
        return self.visit(ctx.scope())
    
    def visitStatement(self, ctx: KatoParser.StatementContext):
        print("statement", ctx.getText())
        return self.visit(ctx.varDefinition() or ctx.funcDefinition() or ctx.expr() or ctx.control())

    def visitVarDefinition(self, ctx: KatoParser.VarDefinitionContext):
        print("var def", ctx.getText())
        return VarDef(
            name=ctx.variable().getText(),
            value=self.visit(ctx.expr())
        )
    
    def visitFuncDefinition(self, ctx: KatoParser.FuncDefinitionContext):
        print("func def", ctx.getText())
        return FunctionDef(
            name=ctx.variable().getText(),
            args=list(map(lambda n: n.getText(), ctx.expr())),
            scope=self.visit(ctx.scope())
        )
    

    #
    # expression labels
    #
    def visitExprVar(self, ctx: KatoParser.ExprVarContext):
        print("exprVar", ctx.getText())
        return self.visit(ctx.variable())
    
    def visitExprLiteral(self, ctx: KatoParser.ExprLiteralContext):
        print("exprLiteral", ctx.getText())
        return self.visit(ctx.literal())
    
    def visitExprScope(self, ctx: KatoParser.ExprScopeContext):
        print("exprScope", ctx.getText())
        return self.visit(ctx.scope())
    
    def visitExprAddSub(self, ctx: KatoParser.ExprAddSubContext):
        print("exprAddSub", ctx.getText())
        lhs = self.visit(ctx.lhs)
        rhs = self.visit(ctx.rhs)
        match ctx.op.text:
            case '+':
                return OpAdd(lhs, rhs)
            case '-':
                return OpSub(lhs, rhs)

    
    def visitExprMulDiv(self, ctx: KatoParser.ExprMulDivContext):
        print("exprMulDiv", ctx.getText())
        lhs = self.visit(ctx.lhs)
        rhs = self.visit(ctx.rhs)
        match ctx.op.text:
            case '*':
                return OpMul(lhs, rhs)
            case '/':
                return OpDiv(lhs, rhs)
    
    def visitExprParen(self, ctx: KatoParser.ExprParenContext):
        print("exprParen", ctx.getText())
        return self.visit(ctx.expr())

    def visitExprCall(self, ctx: KatoParser.ExprCallContext):
        print("exprCall", ctx.getText())
        exprs = list(map(self.visit, ctx.expr()))
        return Call(
            value=exprs[0],
            args=exprs[1:]
        )

    def visitVariable(self, ctx: KatoParser.VariableContext):
        print("variable", ctx.getText())
        return VarGet(ctx.getText())
    
    def visitScope(self, ctx: KatoParser.ScopeContext):
        print("scope", ctx.getText())
        return Scope(list(map(self.visit, ctx.statement())))

    
    def visitControl(self, ctx: KatoParser.ControlContext):
        print("control", ctx.getText())
        return self.visit(ctx.return_() or ctx.if_() or ctx.emit())
    
    def visitIf(self, ctx: KatoParser.IfContext):
        print("if", ctx.getText())
        return IfElse(
            condition=self.visit(ctx.condition),
            scope_true=self.visit(ctx.then),
            scope_false=self.visit(ctx.else_)  # Might be None, is OK
        )

    def visitReturn(self, ctx: KatoParser.ReturnContext):
        print("return", ctx.getText())
        if exp := ctx.expr():
            return Return(self.visit(exp))
        return Return(Void())
    
    def visitEmit(self, ctx: KatoParser.EmitContext):
        print("emit", ctx.getText())
        return Emit(self.visit(ctx.expr()))
    

    def visitLiteralNumber(self, ctx: KatoParser.LiteralNumberContext):
        print("numberLiteral", ctx.getText())
        negative = (ctx.sign.text == '-')
        number = f"{ctx.left.text}.{ctx.right.text}"
        if negative: 
            number *= -1
        return Number(float(number))

    def visitLiteralInteger(self, ctx: KatoParser.LiteralIntegerContext):
        print("integerLiteral", ctx.getText())
        return Integer(int(str(''.join(map(lambda n: n.getText(), ctx.NUMBER())))))

    def visitLiteralBoolean(self, ctx: KatoParser.LiteralBooleanContext):
        return Boolean(ctx.getText() == "true")
    
    def visitLiteralString(self, ctx: KatoParser.LiteralStringContext):
        print("stringLiteral", ctx.getText())
        return String(ctx.STRING().getText()[1:-1])