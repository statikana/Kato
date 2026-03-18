# Generated from main.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,128,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,1,3,1,28,8,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,45,8,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,9,3,1,4,
        1,4,1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,72,8,
        6,1,7,1,7,1,7,3,7,77,8,7,1,8,1,8,1,8,1,9,3,9,83,8,9,1,9,4,9,86,8,
        9,11,9,12,9,87,1,9,1,9,5,9,92,8,9,10,9,12,9,95,9,9,1,9,5,9,98,8,
        9,10,9,12,9,101,9,9,1,9,1,9,4,9,105,8,9,11,9,12,9,106,3,9,109,8,
        9,1,9,4,9,112,8,9,11,9,12,9,113,1,9,3,9,117,8,9,1,10,1,10,5,10,121,
        8,10,10,10,12,10,124,9,10,1,10,1,10,1,10,0,1,6,11,0,2,4,6,8,10,12,
        14,16,18,20,0,2,1,0,4,5,1,0,6,7,137,0,22,1,0,0,0,2,27,1,0,0,0,4,
        31,1,0,0,0,6,44,1,0,0,0,8,57,1,0,0,0,10,62,1,0,0,0,12,64,1,0,0,0,
        14,76,1,0,0,0,16,78,1,0,0,0,18,116,1,0,0,0,20,118,1,0,0,0,22,23,
        3,20,10,0,23,1,1,0,0,0,24,28,3,4,2,0,25,28,3,6,3,0,26,28,3,10,5,
        0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,30,
        5,1,0,0,30,3,1,0,0,0,31,32,5,2,0,0,32,33,3,8,4,0,33,34,5,3,0,0,34,
        35,3,6,3,0,35,5,1,0,0,0,36,37,6,3,-1,0,37,45,3,8,4,0,38,45,3,18,
        9,0,39,45,3,20,10,0,40,41,5,8,0,0,41,42,3,6,3,0,42,43,5,9,0,0,43,
        45,1,0,0,0,44,36,1,0,0,0,44,38,1,0,0,0,44,39,1,0,0,0,44,40,1,0,0,
        0,45,54,1,0,0,0,46,47,10,3,0,0,47,48,7,0,0,0,48,53,3,6,3,4,49,50,
        10,2,0,0,50,51,7,1,0,0,51,53,3,6,3,3,52,46,1,0,0,0,52,49,1,0,0,0,
        53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,54,1,0,
        0,0,57,58,5,18,0,0,58,9,1,0,0,0,59,63,3,12,6,0,60,63,3,14,7,0,61,
        63,3,16,8,0,62,59,1,0,0,0,62,60,1,0,0,0,62,61,1,0,0,0,63,11,1,0,
        0,0,64,65,5,10,0,0,65,66,5,8,0,0,66,67,3,6,3,0,67,68,5,9,0,0,68,
        71,3,20,10,0,69,70,5,11,0,0,70,72,3,20,10,0,71,69,1,0,0,0,71,72,
        1,0,0,0,72,13,1,0,0,0,73,77,5,12,0,0,74,75,5,13,0,0,75,77,3,6,3,
        0,76,73,1,0,0,0,76,74,1,0,0,0,77,15,1,0,0,0,78,79,5,14,0,0,79,80,
        3,6,3,0,80,17,1,0,0,0,81,83,7,1,0,0,82,81,1,0,0,0,82,83,1,0,0,0,
        83,108,1,0,0,0,84,86,5,19,0,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,
        1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,0,89,93,5,15,0,0,90,92,5,19,0,
        0,91,90,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,109,
        1,0,0,0,95,93,1,0,0,0,96,98,5,19,0,0,97,96,1,0,0,0,98,101,1,0,0,
        0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,
        104,5,15,0,0,103,105,5,19,0,0,104,103,1,0,0,0,105,106,1,0,0,0,106,
        104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,85,1,0,0,0,108,99,
        1,0,0,0,109,117,1,0,0,0,110,112,5,19,0,0,111,110,1,0,0,0,112,113,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,117,1,0,0,0,115,117,
        5,20,0,0,116,82,1,0,0,0,116,111,1,0,0,0,116,115,1,0,0,0,117,19,1,
        0,0,0,118,122,5,16,0,0,119,121,3,2,1,0,120,119,1,0,0,0,121,124,1,
        0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,
        0,0,0,125,126,5,17,0,0,126,21,1,0,0,0,16,27,44,52,54,62,71,76,82,
        87,93,99,106,108,113,116,122
    ]

class mainParser ( Parser ):

    grammarFileName = "main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'let '", "'='", "'*'", "'/'", 
                     "'+'", "'-'", "'('", "')'", "'if'", "'else'", "'return'", 
                     "'return '", "'emit '", "'.'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDefinition = 2
    RULE_expr = 3
    RULE_variable = 4
    RULE_control = 5
    RULE_if = 6
    RULE_return = 7
    RULE_emit = 8
    RULE_literal = 9
    RULE_scope = 10

    ruleNames =  [ "program", "statement", "varDefinition", "expr", "variable", 
                   "control", "if", "return", "emit", "literal", "scope" ]

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
    ID=18
    NUMBER=19
    STRING=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scope(self):
            return self.getTypedRuleContext(mainParser.ScopeContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = mainParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDefinition(self):
            return self.getTypedRuleContext(mainParser.VarDefinitionContext,0)


        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def control(self):
            return self.getTypedRuleContext(mainParser.ControlContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = mainParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 24
                self.varDefinition()
                pass
            elif token in [6, 7, 8, 15, 16, 18, 19, 20]:
                self.state = 25
                self.expr(0)
                pass
            elif token in [10, 12, 13, 14]:
                self.state = 26
                self.control()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 29
            self.match(mainParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(mainParser.VariableContext,0)


        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_varDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDefinition" ):
                listener.enterVarDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDefinition" ):
                listener.exitVarDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDefinition" ):
                return visitor.visitVarDefinition(self)
            else:
                return visitor.visitChildren(self)




    def varDefinition(self):

        localctx = mainParser.VarDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(mainParser.T__1)
            self.state = 32
            self.variable()
            self.state = 33
            self.match(mainParser.T__2)
            self.state = 34
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mainParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprVarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(mainParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprVar" ):
                listener.enterExprVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprVar" ):
                listener.exitExprVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprVar" ):
                return visitor.visitExprVar(self)
            else:
                return visitor.visitChildren(self)


    class ExprAddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.op = None # Token
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.ExprContext)
            else:
                return self.getTypedRuleContext(mainParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAddSub" ):
                listener.enterExprAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAddSub" ):
                listener.exitExprAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddSub" ):
                return visitor.visitExprAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ExprParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprParen" ):
                listener.enterExprParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprParen" ):
                listener.exitExprParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParen" ):
                return visitor.visitExprParen(self)
            else:
                return visitor.visitChildren(self)


    class ExprMulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.op = None # Token
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.ExprContext)
            else:
                return self.getTypedRuleContext(mainParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMulDiv" ):
                listener.enterExprMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMulDiv" ):
                listener.exitExprMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMulDiv" ):
                return visitor.visitExprMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(mainParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLiteral" ):
                listener.enterExprLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLiteral" ):
                listener.exitExprLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteral" ):
                return visitor.visitExprLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ExprScopeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def scope(self):
            return self.getTypedRuleContext(mainParser.ScopeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprScope" ):
                listener.enterExprScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprScope" ):
                listener.exitExprScope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprScope" ):
                return visitor.visitExprScope(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mainParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = mainParser.ExprVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 37
                self.variable()
                pass
            elif token in [6, 7, 15, 19, 20]:
                localctx = mainParser.ExprLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.literal()
                pass
            elif token in [16]:
                localctx = mainParser.ExprScopeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.scope()
                pass
            elif token in [8]:
                localctx = mainParser.ExprParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(mainParser.T__7)
                self.state = 41
                self.expr(0)
                self.state = 42
                self.match(mainParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = mainParser.ExprMulDivContext(self, mainParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 47
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        localctx.rhs = self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = mainParser.ExprAddSubContext(self, mainParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 50
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        localctx.rhs = self.expr(3)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(mainParser.ID, 0)

        def getRuleIndex(self):
            return mainParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = mainParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(mainParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(mainParser.IfContext,0)


        def return_(self):
            return self.getTypedRuleContext(mainParser.ReturnContext,0)


        def emit(self):
            return self.getTypedRuleContext(mainParser.EmitContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_control

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl" ):
                listener.enterControl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl" ):
                listener.exitControl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl" ):
                return visitor.visitControl(self)
            else:
                return visitor.visitChildren(self)




    def control(self):

        localctx = mainParser.ControlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_control)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.if_()
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.return_()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.emit()
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


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # ExprContext
            self.then = None # ScopeContext
            self.else_ = None # ScopeContext

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def scope(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.ScopeContext)
            else:
                return self.getTypedRuleContext(mainParser.ScopeContext,i)


        def getRuleIndex(self):
            return mainParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = mainParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(mainParser.T__9)
            self.state = 65
            self.match(mainParser.T__7)
            self.state = 66
            localctx.condition = self.expr(0)
            self.state = 67
            self.match(mainParser.T__8)
            self.state = 68
            localctx.then = self.scope()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 69
                self.match(mainParser.T__10)
                self.state = 70
                localctx.else_ = self.scope()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = mainParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 73
                self.match(mainParser.T__11)
                pass
            elif token in [13]:
                self.state = 74
                self.match(mainParser.T__12)
                self.state = 75
                self.expr(0)
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


    class EmitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_emit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmit" ):
                listener.enterEmit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmit" ):
                listener.exitEmit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmit" ):
                return visitor.visitEmit(self)
            else:
                return visitor.visitChildren(self)




    def emit(self):

        localctx = mainParser.EmitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_emit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(mainParser.T__13)
            self.state = 79
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mainParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(mainParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class NumberLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.LiteralContext
            super().__init__(parser)
            self.sign = None # Token
            self.left = None # Token
            self.right = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.NUMBER)
            else:
                return self.getToken(mainParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberLiteral" ):
                listener.enterNumberLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberLiteral" ):
                listener.exitNumberLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberLiteral" ):
                return visitor.visitNumberLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntegerLiteralContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(mainParser.NUMBER)
            else:
                return self.getToken(mainParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerLiteral" ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerLiteral" ):
                listener.exitIntegerLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerLiteral" ):
                return visitor.visitIntegerLiteral(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = mainParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = mainParser.NumberLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6 or _la==7:
                    self.state = 81
                    localctx.sign = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        localctx.sign = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 85 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 84
                        localctx.left = self.match(mainParser.NUMBER)
                        self.state = 87 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==19):
                            break

                    self.state = 89
                    self.match(mainParser.T__14)
                    self.state = 93
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 90
                            localctx.right = self.match(mainParser.NUMBER) 
                        self.state = 95
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                    pass

                elif la_ == 2:
                    self.state = 99
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==19:
                        self.state = 96
                        localctx.left = self.match(mainParser.NUMBER)
                        self.state = 101
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 102
                    self.match(mainParser.T__14)
                    self.state = 104 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 103
                            localctx.right = self.match(mainParser.NUMBER)

                        else:
                            raise NoViableAltException(self)
                        self.state = 106 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                    pass


                pass

            elif la_ == 2:
                localctx = mainParser.IntegerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 111 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 110
                        self.match(mainParser.NUMBER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 113 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                pass

            elif la_ == 3:
                localctx = mainParser.StringLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(mainParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mainParser.StatementContext)
            else:
                return self.getTypedRuleContext(mainParser.StatementContext,i)


        def getRuleIndex(self):
            return mainParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScope" ):
                return visitor.visitScope(self)
            else:
                return visitor.visitChildren(self)




    def scope(self):

        localctx = mainParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(mainParser.T__15)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1963460) != 0):
                self.state = 119
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(mainParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




