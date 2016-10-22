# This is a temporary file, only used to serve an example of an ANTLR grammar

from parser.PeachLangVisitor import PeachLangVisitor
from parser.PeachLangParser import PeachLangParser

class PeachVisitor(PeachLangVisitor):

    def visitEmpty(self, ctx:PeachLangParser.EmptyContext):
        return 0

    def visitPrintExpr(self, ctx:PeachLangParser.PrintExprContext):
        print(self.visit(ctx.expr()))
        return 0

    def visitMulDiv(self, ctx:PeachLangParser.MulDivContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if ctx.op.text == '*':
            return left * right
        else:
            return left / right # TODO: Throw an error on Division by zero

    def visitAddSub(self, ctx:PeachLangParser.AddSubContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitInt(self, ctx:PeachLangParser.IntContext):
        return int(ctx.getText())