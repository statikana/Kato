grammar main;

program: scope;

statement: (varDefinition | expr | control) ';';

// variable and function definitions
varDefinition: 'let ' variable '=' expr ;

// expressions
expr
    : variable  #ExprVar
    | literal   #ExprLiteral
    | scope     #ExprScope

    | lhs=expr op=('*' | '/') rhs=expr  #ExprMulDiv
    | lhs=expr op=('+' | '-') rhs=expr  #ExprAddSub
    | '(' expr ')'                      #ExprParen
    ;

variable: ID;

control: if | return | emit;
if: 'if' '(' condition=expr ')' then=scope ('else' else=scope)?;
return: ('return' | ('return ' expr));
emit: 'emit ' expr;

literal
    : sign=('+' | '-')? ((left=NUMBER+ '.' right=NUMBER*) | left=NUMBER* '.' right=NUMBER+) #NumberLiteral
    | NUMBER+ #IntegerLiteral
    | STRING #StringLiteral
    ;

scope: '{' statement* '}';


ID: CHAR (CHAR | NUMBER)*;
NUMBER: [0-9];

fragment CHAR: [a-zA-Z];
STRING: '"' .*? '"';
WS: [ \t\n] -> skip;
