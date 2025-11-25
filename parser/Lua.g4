grammar Lua;

program :
        chunk EOF
        ;

chunk :
        block
        ;

block :
        expression* retstat?
        ;

expression :
         SEMI
        | ifExpr
        | FUNCTION funcname funcbody
        ;

ifExpr:
        IF exp THEN block (ELSEIF exp THEN block)+ (ELSE block) END 
        ;

retstat :
        'return' explist? ';'?
        ;
    
explist : 
        (exp) (',' (exp))*
        ;


exp :
         TRUE 
        | FALSE
        | INT
        | FLOAT
        | STRING
        | functiondef
        | exp MULT exp     
        | exp DIV exp     
        | exp ADD exp     
        | exp SUB exp     
        | exp EQ exp 
        | exp OR exp
        | exp AND exp
        | exp CONCAT exp
        | NOT exp 
        | ifExpr  
        | tableconstructor
        ;

fragment                
ALPHA : [a-zA-Z]
      ;

fragment
DIGIT : [0-9]
      ;

ID : ALPHA (ALPHA | DIGIT)*
   ;

fragment
POSITIVE : [1-9]
         ;
INT : (POSITIVE DIGIT* | '0')
;

fragment
EXPONENT : ('e' | 'E') ('+' | '-')? DIGIT+
         ;

FLOAT : INT '.' DIGIT+ EXPONENT?
         ;

STRING : '\'' ( ~[\\'] )*? '\'' ;

NAME: [a-zA-Z_][a-zA-Z_0-9]*;


funcname
    : NAME ('.' NAME)* (':' NAME)?
    ;

functiondef:
        FUNCTION funcbody
       ;

funcbody:
    LP parlist RP block END
    ;

parlist:
    namelist (',' '...')?
    | '...'
    | /*empty option */
    ;

namelist:
    NAME (',' NAME)*
    ;



tableconstructor
    : LB fieldlist? RB
    ;

fieldlist
    : field (fieldsep field)* fieldsep?
    ;

field
    : exp
    | NAME ASSIGN exp
    ;

fieldsep
    : COMMA
    | SEMI
    ;



END         : 'end';
FUNCTION    : 'function';
SEMI        : ';';
ADD         : '+';
SUB         : '-';
MULT        : '*';
DIV         : '/';
EQ          : '==';
FDIV        : '//';

ASSIGN      :  '=';

AND         :  'and';
OR          :  'or';
NOT         :  'not';


IF          :  'if';
THEN        :  'then';
ELSEIF      :  'elseif';
ELSE        :  'else';


TRUE        : 'true';
FALSE       : 'false';

LP          : '(';
RP          : ')';
LB          : '{';
RB          : '}';
LK          : '[';
RK          : ']';
DOT         : '.';
COMMA       : ',';
COLON       : ':';
CONCAT      : '...';

