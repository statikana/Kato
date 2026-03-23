// Generated from c:/Users/ryan/Documents/github/kato/main.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class mainParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, ID=20, NUMBER=21, STRING=22, WS=23;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_varDefinition = 2, RULE_funcDefinition = 3, 
		RULE_expr = 4, RULE_variable = 5, RULE_control = 6, RULE_if = 7, RULE_return = 8, 
		RULE_emit = 9, RULE_literal = 10, RULE_scope = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "varDefinition", "funcDefinition", "expr", "variable", 
			"control", "if", "return", "emit", "literal", "scope"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'let '", "'='", "'func '", "'()'", "'('", "')'", "'*'", 
			"'/'", "'+'", "'-'", "'if'", "'else'", "'return'", "'return '", "'emit '", 
			"'.'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "ID", "NUMBER", "STRING", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "main.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public mainParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public ScopeContext scope() {
			return getRuleContext(ScopeContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			scope();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public VarDefinitionContext varDefinition() {
			return getRuleContext(VarDefinitionContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ControlContext control() {
			return getRuleContext(ControlContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				{
				setState(26);
				varDefinition();
				}
				break;
			case T__5:
			case T__9:
			case T__10:
			case T__16:
			case T__17:
			case ID:
			case NUMBER:
			case STRING:
				{
				setState(27);
				expr(0);
				}
				break;
			case T__11:
			case T__13:
			case T__14:
			case T__15:
				{
				setState(28);
				control();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(31);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDefinitionContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public VarDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDefinition; }
	}

	public final VarDefinitionContext varDefinition() throws RecognitionException {
		VarDefinitionContext _localctx = new VarDefinitionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_varDefinition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(T__1);
			setState(34);
			variable();
			setState(35);
			match(T__2);
			setState(36);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncDefinitionContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public ScopeContext scope() {
			return getRuleContext(ScopeContext.class,0);
		}
		public FuncDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcDefinition; }
	}

	public final FuncDefinitionContext funcDefinition() throws RecognitionException {
		FuncDefinitionContext _localctx = new FuncDefinitionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_funcDefinition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(T__3);
			setState(39);
			variable();
			setState(40);
			match(T__4);
			setState(41);
			scope();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprVarContext extends ExprContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public ExprVarContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprAddSubContext extends ExprContext {
		public ExprContext lhs;
		public Token op;
		public ExprContext rhs;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprAddSubContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprCallContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprCallContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprParenContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ExprParenContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprMulDivContext extends ExprContext {
		public ExprContext lhs;
		public Token op;
		public ExprContext rhs;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprMulDivContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprLiteralContext extends ExprContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public ExprLiteralContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExprScopeContext extends ExprContext {
		public ScopeContext scope() {
			return getRuleContext(ScopeContext.class,0);
		}
		public ExprScopeContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				_localctx = new ExprVarContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(44);
				variable();
				}
				break;
			case T__9:
			case T__10:
			case T__16:
			case NUMBER:
			case STRING:
				{
				_localctx = new ExprLiteralContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(45);
				literal();
				}
				break;
			case T__17:
				{
				_localctx = new ExprScopeContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(46);
				scope();
				}
				break;
			case T__5:
				{
				_localctx = new ExprParenContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(47);
				match(T__5);
				setState(48);
				expr(0);
				setState(49);
				match(T__6);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(64);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(62);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						_localctx = new ExprMulDivContext(new ExprContext(_parentctx, _parentState));
						((ExprMulDivContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(53);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(54);
						((ExprMulDivContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__7 || _la==T__8) ) {
							((ExprMulDivContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(55);
						((ExprMulDivContext)_localctx).rhs = expr(4);
						}
						break;
					case 2:
						{
						_localctx = new ExprAddSubContext(new ExprContext(_parentctx, _parentState));
						((ExprAddSubContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(56);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(57);
						((ExprAddSubContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__9 || _la==T__10) ) {
							((ExprAddSubContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(58);
						((ExprAddSubContext)_localctx).rhs = expr(3);
						}
						break;
					case 3:
						{
						_localctx = new ExprCallContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(59);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(60);
						match(T__5);
						setState(61);
						match(T__6);
						}
						break;
					}
					} 
				}
				setState(66);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VariableContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(mainParser.ID, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ControlContext extends ParserRuleContext {
		public IfContext if_() {
			return getRuleContext(IfContext.class,0);
		}
		public ReturnContext return_() {
			return getRuleContext(ReturnContext.class,0);
		}
		public EmitContext emit() {
			return getRuleContext(EmitContext.class,0);
		}
		public ControlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_control; }
	}

	public final ControlContext control() throws RecognitionException {
		ControlContext _localctx = new ControlContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_control);
		try {
			setState(72);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				if_();
				}
				break;
			case T__13:
			case T__14:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				return_();
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 3);
				{
				setState(71);
				emit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfContext extends ParserRuleContext {
		public ExprContext condition;
		public ScopeContext then;
		public ScopeContext else_;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<ScopeContext> scope() {
			return getRuleContexts(ScopeContext.class);
		}
		public ScopeContext scope(int i) {
			return getRuleContext(ScopeContext.class,i);
		}
		public IfContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if; }
	}

	public final IfContext if_() throws RecognitionException {
		IfContext _localctx = new IfContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(T__11);
			setState(75);
			match(T__5);
			setState(76);
			((IfContext)_localctx).condition = expr(0);
			setState(77);
			match(T__6);
			setState(78);
			((IfContext)_localctx).then = scope();
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(79);
				match(T__12);
				setState(80);
				((IfContext)_localctx).else_ = scope();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ReturnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return; }
	}

	public final ReturnContext return_() throws RecognitionException {
		ReturnContext _localctx = new ReturnContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__13:
				{
				setState(83);
				match(T__13);
				}
				break;
			case T__14:
				{
				{
				setState(84);
				match(T__14);
				setState(85);
				expr(0);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EmitContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public EmitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_emit; }
	}

	public final EmitContext emit() throws RecognitionException {
		EmitContext _localctx = new EmitContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_emit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(T__15);
			setState(89);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	 
		public LiteralContext() { }
		public void copyFrom(LiteralContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StringLiteralContext extends LiteralContext {
		public TerminalNode STRING() { return getToken(mainParser.STRING, 0); }
		public StringLiteralContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumberLiteralContext extends LiteralContext {
		public Token sign;
		public Token left;
		public Token right;
		public List<TerminalNode> NUMBER() { return getTokens(mainParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(mainParser.NUMBER, i);
		}
		public NumberLiteralContext(LiteralContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntegerLiteralContext extends LiteralContext {
		public List<TerminalNode> NUMBER() { return getTokens(mainParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(mainParser.NUMBER, i);
		}
		public IntegerLiteralContext(LiteralContext ctx) { copyFrom(ctx); }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_literal);
		int _la;
		try {
			int _alt;
			setState(126);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				_localctx = new NumberLiteralContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__9 || _la==T__10) {
					{
					setState(91);
					((NumberLiteralContext)_localctx).sign = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__9 || _la==T__10) ) {
						((NumberLiteralContext)_localctx).sign = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(118);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
				case 1:
					{
					{
					setState(95); 
					_errHandler.sync(this);
					_la = _input.LA(1);
					do {
						{
						{
						setState(94);
						((NumberLiteralContext)_localctx).left = match(NUMBER);
						}
						}
						setState(97); 
						_errHandler.sync(this);
						_la = _input.LA(1);
					} while ( _la==NUMBER );
					setState(99);
					match(T__16);
					setState(103);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
					while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
						if ( _alt==1 ) {
							{
							{
							setState(100);
							((NumberLiteralContext)_localctx).right = match(NUMBER);
							}
							} 
						}
						setState(105);
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
					}
					}
					}
					break;
				case 2:
					{
					setState(109);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==NUMBER) {
						{
						{
						setState(106);
						((NumberLiteralContext)_localctx).left = match(NUMBER);
						}
						}
						setState(111);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(112);
					match(T__16);
					setState(114); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(113);
							((NumberLiteralContext)_localctx).right = match(NUMBER);
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(116); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					break;
				}
				}
				break;
			case 2:
				_localctx = new IntegerLiteralContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(121); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(120);
						match(NUMBER);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(123); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case 3:
				_localctx = new StringLiteralContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(125);
				match(STRING);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScopeContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ScopeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scope; }
	}

	public final ScopeContext scope() throws RecognitionException {
		ScopeContext _localctx = new ScopeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_scope);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(T__17);
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7855172L) != 0)) {
				{
				{
				setState(129);
				statement();
				}
				}
				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(135);
			match(T__18);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 2);
		case 2:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0017\u008a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u001e\b\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u00044\b\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0005\u0004?\b\u0004\n\u0004\f\u0004B\t\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"I\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0003\u0007R\b\u0007\u0001\b\u0001\b\u0001\b"+
		"\u0003\bW\b\b\u0001\t\u0001\t\u0001\t\u0001\n\u0003\n]\b\n\u0001\n\u0004"+
		"\n`\b\n\u000b\n\f\na\u0001\n\u0001\n\u0005\nf\b\n\n\n\f\ni\t\n\u0001\n"+
		"\u0005\nl\b\n\n\n\f\no\t\n\u0001\n\u0001\n\u0004\ns\b\n\u000b\n\f\nt\u0003"+
		"\nw\b\n\u0001\n\u0004\nz\b\n\u000b\n\f\n{\u0001\n\u0003\n\u007f\b\n\u0001"+
		"\u000b\u0001\u000b\u0005\u000b\u0083\b\u000b\n\u000b\f\u000b\u0086\t\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0000\u0001\b\f\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0000\u0002\u0001\u0000\b\t"+
		"\u0001\u0000\n\u000b\u0093\u0000\u0018\u0001\u0000\u0000\u0000\u0002\u001d"+
		"\u0001\u0000\u0000\u0000\u0004!\u0001\u0000\u0000\u0000\u0006&\u0001\u0000"+
		"\u0000\u0000\b3\u0001\u0000\u0000\u0000\nC\u0001\u0000\u0000\u0000\fH"+
		"\u0001\u0000\u0000\u0000\u000eJ\u0001\u0000\u0000\u0000\u0010V\u0001\u0000"+
		"\u0000\u0000\u0012X\u0001\u0000\u0000\u0000\u0014~\u0001\u0000\u0000\u0000"+
		"\u0016\u0080\u0001\u0000\u0000\u0000\u0018\u0019\u0003\u0016\u000b\u0000"+
		"\u0019\u0001\u0001\u0000\u0000\u0000\u001a\u001e\u0003\u0004\u0002\u0000"+
		"\u001b\u001e\u0003\b\u0004\u0000\u001c\u001e\u0003\f\u0006\u0000\u001d"+
		"\u001a\u0001\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d"+
		"\u001c\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f"+
		" \u0005\u0001\u0000\u0000 \u0003\u0001\u0000\u0000\u0000!\"\u0005\u0002"+
		"\u0000\u0000\"#\u0003\n\u0005\u0000#$\u0005\u0003\u0000\u0000$%\u0003"+
		"\b\u0004\u0000%\u0005\u0001\u0000\u0000\u0000&\'\u0005\u0004\u0000\u0000"+
		"\'(\u0003\n\u0005\u0000()\u0005\u0005\u0000\u0000)*\u0003\u0016\u000b"+
		"\u0000*\u0007\u0001\u0000\u0000\u0000+,\u0006\u0004\uffff\uffff\u0000"+
		",4\u0003\n\u0005\u0000-4\u0003\u0014\n\u0000.4\u0003\u0016\u000b\u0000"+
		"/0\u0005\u0006\u0000\u000001\u0003\b\u0004\u000012\u0005\u0007\u0000\u0000"+
		"24\u0001\u0000\u0000\u00003+\u0001\u0000\u0000\u00003-\u0001\u0000\u0000"+
		"\u00003.\u0001\u0000\u0000\u00003/\u0001\u0000\u0000\u00004@\u0001\u0000"+
		"\u0000\u000056\n\u0003\u0000\u000067\u0007\u0000\u0000\u00007?\u0003\b"+
		"\u0004\u000489\n\u0002\u0000\u00009:\u0007\u0001\u0000\u0000:?\u0003\b"+
		"\u0004\u0003;<\n\u0004\u0000\u0000<=\u0005\u0006\u0000\u0000=?\u0005\u0007"+
		"\u0000\u0000>5\u0001\u0000\u0000\u0000>8\u0001\u0000\u0000\u0000>;\u0001"+
		"\u0000\u0000\u0000?B\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000"+
		"@A\u0001\u0000\u0000\u0000A\t\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000"+
		"\u0000CD\u0005\u0014\u0000\u0000D\u000b\u0001\u0000\u0000\u0000EI\u0003"+
		"\u000e\u0007\u0000FI\u0003\u0010\b\u0000GI\u0003\u0012\t\u0000HE\u0001"+
		"\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000HG\u0001\u0000\u0000\u0000"+
		"I\r\u0001\u0000\u0000\u0000JK\u0005\f\u0000\u0000KL\u0005\u0006\u0000"+
		"\u0000LM\u0003\b\u0004\u0000MN\u0005\u0007\u0000\u0000NQ\u0003\u0016\u000b"+
		"\u0000OP\u0005\r\u0000\u0000PR\u0003\u0016\u000b\u0000QO\u0001\u0000\u0000"+
		"\u0000QR\u0001\u0000\u0000\u0000R\u000f\u0001\u0000\u0000\u0000SW\u0005"+
		"\u000e\u0000\u0000TU\u0005\u000f\u0000\u0000UW\u0003\b\u0004\u0000VS\u0001"+
		"\u0000\u0000\u0000VT\u0001\u0000\u0000\u0000W\u0011\u0001\u0000\u0000"+
		"\u0000XY\u0005\u0010\u0000\u0000YZ\u0003\b\u0004\u0000Z\u0013\u0001\u0000"+
		"\u0000\u0000[]\u0007\u0001\u0000\u0000\\[\u0001\u0000\u0000\u0000\\]\u0001"+
		"\u0000\u0000\u0000]v\u0001\u0000\u0000\u0000^`\u0005\u0015\u0000\u0000"+
		"_^\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000"+
		"\u0000ab\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000cg\u0005\u0011"+
		"\u0000\u0000df\u0005\u0015\u0000\u0000ed\u0001\u0000\u0000\u0000fi\u0001"+
		"\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000"+
		"hw\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000jl\u0005\u0015\u0000"+
		"\u0000kj\u0001\u0000\u0000\u0000lo\u0001\u0000\u0000\u0000mk\u0001\u0000"+
		"\u0000\u0000mn\u0001\u0000\u0000\u0000np\u0001\u0000\u0000\u0000om\u0001"+
		"\u0000\u0000\u0000pr\u0005\u0011\u0000\u0000qs\u0005\u0015\u0000\u0000"+
		"rq\u0001\u0000\u0000\u0000st\u0001\u0000\u0000\u0000tr\u0001\u0000\u0000"+
		"\u0000tu\u0001\u0000\u0000\u0000uw\u0001\u0000\u0000\u0000v_\u0001\u0000"+
		"\u0000\u0000vm\u0001\u0000\u0000\u0000w\u007f\u0001\u0000\u0000\u0000"+
		"xz\u0005\u0015\u0000\u0000yx\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000"+
		"\u0000{y\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|\u007f\u0001"+
		"\u0000\u0000\u0000}\u007f\u0005\u0016\u0000\u0000~\\\u0001\u0000\u0000"+
		"\u0000~y\u0001\u0000\u0000\u0000~}\u0001\u0000\u0000\u0000\u007f\u0015"+
		"\u0001\u0000\u0000\u0000\u0080\u0084\u0005\u0012\u0000\u0000\u0081\u0083"+
		"\u0003\u0002\u0001\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0083\u0086"+
		"\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0084\u0085"+
		"\u0001\u0000\u0000\u0000\u0085\u0087\u0001\u0000\u0000\u0000\u0086\u0084"+
		"\u0001\u0000\u0000\u0000\u0087\u0088\u0005\u0013\u0000\u0000\u0088\u0017"+
		"\u0001\u0000\u0000\u0000\u0010\u001d3>@HQV\\agmtv{~\u0084";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}