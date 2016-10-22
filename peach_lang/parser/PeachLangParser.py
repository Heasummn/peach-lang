# Generated from /home/heasummn/usr/dev/Python/peach-lang/peach_lang/PeachLang.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\t")
        buf.write("\"\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\5\3\22\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\7\4\35\n\4\f\4\16\4 \13\4\3\4\2\3\6\5\2\4\6\2")
        buf.write("\4\3\2\3\4\3\2\5\6\"\2\t\3\2\2\2\4\21\3\2\2\2\6\23\3\2")
        buf.write("\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2")
        buf.write("\13\f\3\2\2\2\f\3\3\2\2\2\r\16\5\6\4\2\16\17\7\7\2\2\17")
        buf.write("\22\3\2\2\2\20\22\7\7\2\2\21\r\3\2\2\2\21\20\3\2\2\2\22")
        buf.write("\5\3\2\2\2\23\24\b\4\1\2\24\25\7\b\2\2\25\36\3\2\2\2\26")
        buf.write("\27\f\5\2\2\27\30\t\2\2\2\30\35\5\6\4\6\31\32\f\4\2\2")
        buf.write("\32\33\t\3\2\2\33\35\5\6\4\5\34\26\3\2\2\2\34\31\3\2\2")
        buf.write("\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37\7\3\2\2")
        buf.write("\2 \36\3\2\2\2\6\13\21\34\36")
        return buf.getvalue()


class PeachLangParser ( Parser ):

    grammarFileName = "PeachLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NEWLINE", "INT", "WHITE" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "line", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NEWLINE=5
    INT=6
    WHITE=7

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PeachLangParser.LineContext)
            else:
                return self.getTypedRuleContext(PeachLangParser.LineContext,i)


        def getRuleIndex(self):
            return PeachLangParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PeachLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.line()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==PeachLangParser.NEWLINE or _la==PeachLangParser.INT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PeachLangParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintExprContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PeachLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(PeachLangParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class EmptyContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(PeachLangParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty" ):
                return visitor.visitEmpty(self)
            else:
                return visitor.visitChildren(self)



    def line(self):

        localctx = PeachLangParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 15
            token = self._input.LA(1)
            if token in [PeachLangParser.INT]:
                localctx = PeachLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(PeachLangParser.NEWLINE)

            elif token in [PeachLangParser.NEWLINE]:
                localctx = PeachLangParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(PeachLangParser.NEWLINE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PeachLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PeachLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(PeachLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PeachLangParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PeachLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(PeachLangParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PeachLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = PeachLangParser.IntContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 18
            self.match(PeachLangParser.INT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 26
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = PeachLangParser.MulDivContext(self, PeachLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 21
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PeachLangParser.T__0 or _la==PeachLangParser.T__1):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 22
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = PeachLangParser.AddSubContext(self, PeachLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 24
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PeachLangParser.T__2 or _la==PeachLangParser.T__3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 25
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
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
         




