grammar PeachLang;

options {
    language = Python3;
}

prog: line+
    ;

line
    : expr NEWLINE  # printExpr
    | NEWLINE       # empty
    ;

expr
    : left=mulDivExpr '+' right=expr    # add
    | left=mulDivExpr '-' right=expr    # sub
    | mulDivExpr                        # mulDiv
    ;

mulDivExpr
    : left=atom '*' right=mulDivExpr    # mult
    | left=atom '/' right=mulDivExpr    # div
    | atom                              # literal
    ;

atom
    : INT           # int
    | '(' expr ')'   # paren
    ;

NEWLINE: '\r'? '\n';
INT: [0-9]+ ; // Matches integers
WHITE: [ '\t'] -> skip;