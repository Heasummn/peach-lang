# Generated from /home/heasummn/usr/dev/Python/peach-lang/peach_lang/PeachLang.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\t")
        buf.write("\'\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\5\6\33\n")
        buf.write("\6\3\6\3\6\3\7\6\7 \n\7\r\7\16\7!\3\b\3\b\3\b\3\b\2\2")
        buf.write("\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\4\3\2\62;\5\2\13")
        buf.write("\13\"\"))(\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2")
        buf.write("\2\5\23\3\2\2\2\7\25\3\2\2\2\t\27\3\2\2\2\13\32\3\2\2")
        buf.write("\2\r\37\3\2\2\2\17#\3\2\2\2\21\22\7,\2\2\22\4\3\2\2\2")
        buf.write("\23\24\7\61\2\2\24\6\3\2\2\2\25\26\7-\2\2\26\b\3\2\2\2")
        buf.write("\27\30\7/\2\2\30\n\3\2\2\2\31\33\7\17\2\2\32\31\3\2\2")
        buf.write("\2\32\33\3\2\2\2\33\34\3\2\2\2\34\35\7\f\2\2\35\f\3\2")
        buf.write("\2\2\36 \t\2\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!")
        buf.write("\"\3\2\2\2\"\16\3\2\2\2#$\t\3\2\2$%\3\2\2\2%&\b\b\2\2")
        buf.write("&\20\3\2\2\2\5\2\32!\3\b\2\2")
        return buf.getvalue()


class PeachLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NEWLINE = 5
    INT = 6
    WHITE = 7

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "INT", "WHITE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NEWLINE", "INT", "WHITE" ]

    grammarFileName = "PeachLang.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


