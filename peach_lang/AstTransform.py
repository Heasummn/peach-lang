# This is a temporary file, only used to serve an example of an ANTLR grammar

from parser.PeachLangVisitor import PeachLangVisitor
from parser.PeachLangParser import PeachLangParser
import ast

class Transformer(PeachLangVisitor):
    """
    Converts the ANTLR generated CST into our own AST.
    """
    def visitProg(self, ctx:PeachLangParser.ProgContext):
        expressions = []
        for line in ctx.line():
            expr = self.visit(line)
            if expr is None:
                continue
            expressions.append(expr)
        return ast.Program(expressions)

    # Helper function that makes the given binary node out of a ctx
    def _createBinary(self, ctx, node):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        return node(left, right)

    def visitAdd(self, ctx:PeachLangParser.AddContext):
        return self._createBinary(ctx, ast.Add)

    def visitSub(self, ctx:PeachLangParser.SubContext):
        return self._createBinary(ctx, ast.Sub)

    def visitMult(self, ctx:PeachLangParser.MultContext):
        return self._createBinary(ctx, ast.Mult)

    def visitDiv(self, ctx:PeachLangParser.DivContext):
        return self._createBinary(ctx, ast.Div)

    def visitPrintExpr(self, ctx:PeachLangParser.PrintExprContext):
        return self.visit(ctx.expr())

    # If we do it like this, we can't see the parens
    # We can only see the associativity in the repr() of a node
    def visitParen(self, ctx:PeachLangParser.ParenContext):
        return self.visit(ctx.expr())

    def visitInt(self, ctx:PeachLangParser.IntContext):
        return ast.Literal(int(ctx.getText()))