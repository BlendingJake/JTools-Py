grammar QUERY;

multi_query
    : raw_text ('@' query raw_text)*
    ;

raw_text
    : (SYMBOL | ' ' | '\n' | '\r' | '\t' | '\f' | '@@' | ~'@')*
    ;

query
    : query_part ('.' query_part)*
    ;

query_part
    : query_field
    | special
    ;

query_field: name ;

special
    : '$' special_name arguments?
    ;

special_name: name ;

arguments
    : '(' value (',' value)* ')'
    | '(' ')'
    ;

value
    : '@' query
    | list_value
    | set_value
    | object_value
    | number
    | STRING
    | 'true'
    | 'false'
    | 'null'
    ;

list_value
    : '[' value (',' value)* ']'
    | '[' ']'
    ;

set_value
    : '{' value (',' value)* '}'
    | '{' '}'
    ;

object_value
    : '{' pair (',' pair)* '}'
    | '{' ':' '}'
    ;

pair: key ':' value ;

key: '@' query | STRING | number | 'true' | 'false' | 'null' ;

number
    : ('-' | '+')? DIGITS '.' DIGITS
    | ('-' | '+')? DIGITS
    ;

name
    : 'true' | 'false' | 'null' | DIGITS | ('-' | '_' | LETTERS | DIGITS)+
    ;

DIGITS: [0-9]+ ;
LETTERS: [a-zA-Z]+;
SYMBOL: [~!#$%^&*()_+=\-`[\]{};':",./<>?\\|];
STRING
    : '"' ('\\"' | ~'"')* '"'
    | '\'' ('\\\'' | ~'\'')* '\''
    ;
WS: [ \r\f\t\n]+ -> skip ;