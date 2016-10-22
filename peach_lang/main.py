from antlr4 import *
from antlr4.InputStream import InputStream
from parser.PeachLangLexer import PeachLangLexer
from parser.PeachLangParser import PeachLangParser
from peach_visitor import PeachVisitor

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