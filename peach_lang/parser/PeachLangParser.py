# Generated from /home/heasummn/usr/dev/Python/peach-lang/peach_lang/PeachLang.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\13")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\3\3\3\3\3\3\3\5\3\26\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4!\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5,\n\5\3\6\3\6\3\6\3\6\3\6\5\6\63")
        buf.write("\n\6\3\6\2\2\7\2\4\6\b\n\2\2\66\2\r\3\2\2\2\4\25\3\2\2")
        buf.write("\2\6 \3\2\2\2\b+\3\2\2\2\n\62\3\2\2\2\f\16\5\4\3\2\r\f")
        buf.write("\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\3")
        buf.write("\3\2\2\2\21\22\5\6\4\2\22\23\7\t\2\2\23\26\3\2\2\2\24")
        buf.write("\26\7\t\2\2\25\21\3\2\2\2\25\24\3\2\2\2\26\5\3\2\2\2\27")
        buf.write("\30\5\b\5\2\30\31\7\3\2\2\31\32\5\6\4\2\32!\3\2\2\2\33")
        buf.write("\34\5\b\5\2\34\35\7\4\2\2\35\36\5\6\4\2\36!\3\2\2\2\37")
        buf.write("!\5\b\5\2 \27\3\2\2\2 \33\3\2\2\2 \37\3\2\2\2!\7\3\2\2")
        buf.write("\2\"#\5\n\6\2#$\7\5\2\2$%\5\b\5\2%,\3\2\2\2&\'\5\n\6\2")
        buf.write("\'(\7\6\2\2()\5\b\5\2),\3\2\2\2*,\5\n\6\2+\"\3\2\2\2+")
        buf.write("&\3\2\2\2+*\3\2\2\2,\t\3\2\2\2-\63\7\n\2\2./\7\7\2\2/")
        buf.write("\60\5\6\4\2\60\61\7\b\2\2\61\63\3\2\2\2\62-\3\2\2\2\62")
        buf.write(".\3\2\2\2\63\13\3\2\2\2\7\17\25 +\62")
        return buf.getvalue()


class PeachLangParser ( Parser ):

    grammarFileName = "PeachLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINE", 
                      "INT", "WHITE" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_expr = 2
    RULE_mulDivExpr = 3
    RULE_atom = 4

    ruleNames =  [ "prog", "line", "expr", "mulDivExpr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NEWLINE=7
    INT=8
    WHITE=9

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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.line()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PeachLangParser.T__4) | (1 << PeachLangParser.NEWLINE) | (1 << PeachLangParser.INT))) != 0)):
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
            self.state = 19
            token = self._input.LA(1)
            if token in [PeachLangParser.T__4, PeachLangParser.INT]:
                localctx = PeachLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr()
                self.state = 16
                self.match(PeachLangParser.NEWLINE)

            elif token in [PeachLangParser.NEWLINE]:
                localctx = PeachLangParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
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



    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.ExprContext
            super().__init__(parser)
            self.left = None # MulDivExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def mulDivExpr(self):
            return self.getTypedRuleContext(PeachLangParser.MulDivExprContext,0)

        def expr(self):
            return self.getTypedRuleContext(PeachLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.ExprContext
            super().__init__(parser)
            self.left = None # MulDivExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def mulDivExpr(self):
            return self.getTypedRuleContext(PeachLangParser.MulDivExprContext,0)

        def expr(self):
            return self.getTypedRuleContext(PeachLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulDivExpr(self):
            return self.getTypedRuleContext(PeachLangParser.MulDivExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = PeachLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 30
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = PeachLangParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                localctx.left = self.mulDivExpr()
                self.state = 22
                self.match(PeachLangParser.T__0)
                self.state = 23
                localctx.right = self.expr()
                pass

            elif la_ == 2:
                localctx = PeachLangParser.SubContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                localctx.left = self.mulDivExpr()
                self.state = 26
                self.match(PeachLangParser.T__1)
                self.state = 27
                localctx.right = self.expr()
                pass

            elif la_ == 3:
                localctx = PeachLangParser.MulDivContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.mulDivExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulDivExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PeachLangParser.RULE_mulDivExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivContext(MulDivExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.MulDivExprContext
            super().__init__(parser)
            self.left = None # AtomContext
            self.right = None # MulDivExprContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(PeachLangParser.AtomContext,0)

        def mulDivExpr(self):
            return self.getTypedRuleContext(PeachLangParser.MulDivExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(MulDivExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.MulDivExprContext
            super().__init__(parser)
            self.left = None # AtomContext
            self.right = None # MulDivExprContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(PeachLangParser.AtomContext,0)

        def mulDivExpr(self):
            return self.getTypedRuleContext(PeachLangParser.MulDivExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class LiteralContext(MulDivExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.MulDivExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(PeachLangParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)



    def mulDivExpr(self):

        localctx = PeachLangParser.MulDivExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mulDivExpr)
        try:
            self.state = 41
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = PeachLangParser.MultContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                localctx.left = self.atom()
                self.state = 33
                self.match(PeachLangParser.T__2)
                self.state = 34
                localctx.right = self.mulDivExpr()
                pass

            elif la_ == 2:
                localctx = PeachLangParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                localctx.left = self.atom()
                self.state = 37
                self.match(PeachLangParser.T__3)
                self.state = 38
                localctx.right = self.mulDivExpr()
                pass

            elif la_ == 3:
                localctx = PeachLangParser.LiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PeachLangParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PeachLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PeachLangParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PeachLangParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = PeachLangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 48
            token = self._input.LA(1)
            if token in [PeachLangParser.INT]:
                localctx = PeachLangParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(PeachLangParser.INT)

            elif token in [PeachLangParser.T__4]:
                localctx = PeachLangParser.ParenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(PeachLangParser.T__4)
                self.state = 45
                self.expr()
                self.state = 46
                self.match(PeachLangParser.T__5)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





