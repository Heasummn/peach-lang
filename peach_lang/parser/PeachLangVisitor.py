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


    # Visit a parse tree produced by PeachLangParser#addSub.
    def visitAddSub(self, ctx:PeachLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#int.
    def visitInt(self, ctx:PeachLangParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PeachLangParser#mulDiv.
    def visitMulDiv(self, ctx:PeachLangParser.MulDivContext):
        return self.visitChildren(ctx)



del PeachLangParser