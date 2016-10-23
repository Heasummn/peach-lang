# Generated from /home/heasummn/usr/dev/Python/peach-lang/peach_lang/PeachLang.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PeachLangParser import PeachLangParser
else:
    from PeachLangParser import PeachLangParser

# This class defines a complete generic visitor for a parse tree produced by PeachLangParser.

class PeachLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PeachLangParser#prog.
    def visitProg(self, ctx:PeachLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#printExpr.
    def visitPrintExpr(self, ctx:PeachLangParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#empty.
    def visitEmpty(self, ctx:PeachLangParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#add.
    def visitAdd(self, ctx:PeachLangParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#sub.
    def visitSub(self, ctx:PeachLangParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#mulDiv.
    def visitMulDiv(self, ctx:PeachLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#mult.
    def visitMult(self, ctx:PeachLangParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#div.
    def visitDiv(self, ctx:PeachLangParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#literal.
    def visitLiteral(self, ctx:PeachLangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#int.
    def visitInt(self, ctx:PeachLangParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#paren.
    def visitParen(self, ctx:PeachLangParser.ParenContext):
        return self.visitChildren(ctx)



del PeachLangParser