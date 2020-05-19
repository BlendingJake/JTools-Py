grammar JQL;

jql_multi_query: (AT query | raw_text)* ;

jql_query: WS* query? WS* EOF ;

query: query_part (WS* DOT query_part)* ;

raw_text: (WS+ | (AT AT) | ~AT)+;

query_part
    : query_field
    | special
    ;

query_field: name ;

special
    : DOLLAR special_name arguments?
    ;

special_name: name ;

arguments
    : LPAREN WS* argument (WS* COMMA WS* argument)* (WS* COMMA WS* keyword_argument)* WS* RPAREN
    | LPAREN WS* keyword_argument (WS* COMMA WS* keyword_argument)* RPAREN
    | LPAREN WS* RPAREN
    ;

keyword_argument: name WS* '=' WS* (arith_expr | value);
argument: arith_expr | value;

arith_expr: factor_expr (WS* arith_operator WS* factor_expr)*;
arith_operator: '+' | '-';

factor_expr: power_expr ( WS* factor_operator WS* power_expr)*;
factor_operator: '/' | '//' | '*' | '%';

power_expr: math_value ( WS* power_operator WS* math_value)*;
power_operator: '**';

math_value
    : AT query
    | number
    | LPAREN WS* arith_expr WS* RPAREN
    ;

value
    : AT query
    | list_value
    | set_value
    | object_value
    | arith_expr
    | primitive_value
    ;

primitive_value
    : number
    | STRING
    | PRIMITIVE
    ;

list_value
    : LBRACKET WS* value (WS* COMMA WS* value)* WS* RBRACKET
    | LBRACKET WS* RBRACKET
    ;

set_value
    : LBRACE WS* value (WS* COMMA WS* value)* WS* RBRACE
    | LBRACE WS* RBRACE
    ;

object_value
    : LBRACE WS* pair (WS* COMMA  WS* pair)* WS* RBRACE
    | LBRACE WS* SEMI WS* RBRACE
    ;

pair: key WS* SEMI WS* value ;

key: '@' query | STRING | number | PRIMITIVE ;

number
    : ('-' | '+')? DIGITS DOT DIGITS
    | ('-' | '+')? DIGITS
    ;

name
    : (PRIMITIVE | DIGITS | '-' | '_' | LETTERS )+
    ;

PRIMITIVE: 'true' | 'false' | 'null' ;
LPAREN: '(';
RPAREN: ')';
DOT: '.';
LBRACKET: '[';
RBRACKET: ']';
COMMA: ',';
LBRACE: '{';
RBRACE: '}';
SEMI: ':';
AT: '@';
DOLLAR: '$';
DIGITS: [0-9]+ ;
LETTERS: [a-zA-Z]+ ;
STRING
    : '"' ('\\"' | ~'"')* '"'
    | '\'' ('\\\'' | ~'\'')* '\''
    ;
WS: [ \n\t\r\f];
LAST: ~[\n];