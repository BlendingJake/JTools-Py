grammar JQL;

jql_multi_query: (AT query | raw_text)* ;

jql_query: query? EOF ;

query: query_part (DOT query_part)* ;

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
    : LPAREN SPACE* value (SPACE* COMMA SPACE* value)* SPACE* RPAREN
    | LPAREN SPACE* RPAREN
    ;

value
    : AT query
    | list_value
    | set_value
    | object_value
    | number
    | STRING
    | PRIMITIVE
    ;

list_value
    : LBRACKET SPACE* value (SPACE* COMMA SPACE* value)* SPACE* RBRACKET
    | LBRACKET SPACE*RBRACKET
    ;

set_value
    : LBRACE SPACE* value (SPACE* COMMA SPACE* value)* SPACE* RBRACE
    | LBRACE SPACE* RBRACE
    ;

object_value
    : LBRACE SPACE* pair (SPACE* COMMA SPACE* pair)* SPACE* RBRACE
    | LBRACE SPACE* SEMI SPACE* RBRACE
    ;

pair: key SPACE* SEMI SPACE* value ;

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
SPACE: [ ];
WS: SPACE | [\n\t\r\f];
LAST: ~[\n];