grammar PeachLang;

options {
    language = Python3;
}

prog: line+ ;

line:
      expr NEWLINE  # printExpr
    | NEWLINE       # empty
    ;

expr:
        left=expr op=('*'|'/') right=expr # mulDiv
    |   left=expr op=('+'|'-') right=expr # addSub
    |   INT     # int
    ;

NEWLINE: '\r'? '\n';
INT: [0-9]+ ; // Matches integers
WHITE: [ '\t'] -> skip;