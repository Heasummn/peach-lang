import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from peach_lang.parser.PeachLangLexer import PeachLangLexer
from peach_lang.parser.PeachLangParser import PeachLangParser
from peach_lang.peach_visitor import PeachVisitor

def main():
    prog = ""
    text = input("> ")
    while text != "END":
        prog += (text + "\n")
        text = input("> ")


    stream = InputStream(prog)
    lexer = PeachLangLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = PeachLangParser(tokens)
    tree = parser.prog()

    visitor = PeachVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()