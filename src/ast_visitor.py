# type: ignore
# antlr4 is horribly, horribly typed.

from antlr4.tree.Tree import Tree

from gen.mainLexer import mainLexer as MainLexer
from gen.mainParser import mainParser as MainParser
from gen.mainVisitor import mainVisitor as MainVisitor

from .ast import *
from .datatype.datatype import *

class ASTVisitor(MainVisitor):
    def visit(self, tree: Tree) -> ASTNode:
        return super().visit(tree)
    
    def visitProgram(self, ctx: MainParser.ProgramContext):
        return self.visit(ctx.scope())
    
    def visitStatement(self, ctx: MainParser.StatementContext):
        return self.visit(ctx.varDefinition() or ctx.expr() or ctx.control())

    def visitVarDefinition(self, ctx: MainParser.VarDefinitionContext):
        print("var def", ctx.getText())
        return VarDef(
            name=ctx.variable().getText(),
            value=self.visit(ctx.expr())
        )

    #
    # expression labels
    #
    def visitExprVar(self, ctx: MainParser.ExprVarContext):
        return self.visit(ctx.variable())
    
    def visitExprLiteral(self, ctx: MainParser.ExprLiteralContext):
        return self.visit(ctx.literal())
    
    def visitExprScope(self, ctx: MainParser.ExprScopeContext):
        return self.visit(ctx.scope())
    
    def visitExprAddSub(self, ctx: MainParser.ExprAddSubContext):
        lhs = self.visit(ctx.lhs)
        rhs = self.visit(ctx.rhs)
        match ctx.op.text:
            case '+':
                return OpAdd(lhs, rhs)
            case '-':
                return OpSub(lhs, rhs)

    
    def visitExprMulDiv(self, ctx: MainParser.ExprMulDivContext):
        lhs = self.visit(ctx.lhs)
        rhs = self.visit(ctx.rhs)
        match ctx.op.text:
            case '*':
                return OpMul(lhs, rhs)
            case '/':
                return OpDiv(lhs, rhs)
    
    def visitExprParen(self, ctx: MainParser.ExprParenContext):
        return self.visit(ctx.expr())
    


    def visitVariable(self, ctx: MainParser.VariableContext):
        print("variable", ctx.getText())
        return VarGet(ctx.getText())
    
    def visitScope(self, ctx: MainParser.ScopeContext):
        s = ctx.statement()
        return Scope(list(map(self.visit, s)))

    
    def visitControl(self, ctx: MainParser.ControlContext):
        return self.visit(ctx.return_() or ctx.if_() or ctx.emit())
    
    def visitIf(self, ctx: MainParser.IfContext):
        return IfElse(
            condition=self.visit(ctx.condition),
            scope_true=self.visit(ctx.then),
            scope_false=self.visit(ctx.else_)  # Might be None, is OK
        )

    def visitReturn(self, ctx: MainParser.ReturnContext):
        if exp := ctx.expr():
            return Return(self.visit(exp))
        return Return(Void())
    
    def visitEmit(self, ctx: MainParser.EmitContext):
        return Emit(self.visit(ctx.expr()))
    

    def visitNumberLiteral(self, ctx: MainParser.NumberLiteralContext):
        negative = (ctx.sign.text == '-')
        number = f"{ctx.left.text}.{ctx.right.text}"
        if negative: 
            number *= -1
        return Number(float(number))

    def visitIntegerLiteral(self, ctx: MainParser.IntegerLiteralContext):
        return Integer(int(str(''.join(map(lambda n: n.getText(), ctx.NUMBER())))))

    def visitStringLiteral(self, ctx: MainParser.StringLiteralContext):
        return String(ctx.STRING().getText()[1:-1])