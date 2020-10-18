# JTools

>JTools is a robust library for interacting with JSON-like objects:
>providing the ability to quickly query, format, and filter JSON-like data.

>JTools is available in Python and JavaScript and consists of three main components:

* `Query`: Extract and transform the values of nested fields.
  * `Query("data.timestamp.$parse_timestamp.$time_part('year')").many(items)`
* `Filter`: Combine the querying capabilities of `Query` with the ability
 to define filtering conditions to find just the elements you want.
  * `Filter(Key("data.timestamp.$parse_timestamp.$time_part('year')").gt(2015)).many(data)`
* `Formatter`: Take multiple queries and format them into a string
  * `Formatter("Item @data.id was released in @data.timestamp.$parse_timestamp.$time_part('year')").single(data[0])`

JTools exists in two different langauges with almost identical names and capabilities to allow you to move between the packages seamlessly. 

## Python - [jtools](https://pypi.org/project/jtools/)

## JavaScript - [@blending_jake/jtools](https://www.npmjs.com/package/@blending_jake/jtools)
>Written in TypeScript and distributed as an ES6 style module with type
declaration files. 

### Differences

 * In JTools-Py, the `==` and `===` filter operators will behave the same, as well as `!=` and `!==`. 
 * JTools-Py uses the `datetime` package for time related queries, while JavaScript uses `moment`
 * JTools-Py replicates JavaScript's lack of differentiation between `item[0]` and `item["0"]` by default. 
 However, this can be changed in the Python version by setting `Query(..., convert_ints=False)`. 
 If that argument is set to `False` in Python, then `item.0` would work on `{"item": {"0": ...}}`, 
 but not on `{"item": {0: ...}}`. The JavaScript version essentially always has `convert_ints=True`.

## Recent Changes
 * `2.0.0`
   * Numerous new language features
     * Support for arithmetic in arguments. The supported operators are
     `-`, `+`, `*`, `/`, `//` (floor division), `**` (exponentiation), and `%`. The operators can be used any
     place a value is valid within an argument, such as `$special(14000 * 2)`, `$special(@value // 2)`,
     `$special([1, 1+1, 1+2])`. The order of operations follows typical precedence, and arithmetic 
     can be nested in `()`.
     * Support for keyword arguments:`$index("value", fallback=12)`
     * Whitespace is allowed in a lot more places in a query now, which is very helpful since both
      JavaScript and Python support multi-line strings.
   * Performance increase for cases were a `Query` field doesn't have any specials. A faster parsing
   method can be used for about a 40x performance increase in creating the `Query` object. Note, this
   just speeds up `Query` creation and not the speed of `.single()`, `.many()`, etc.
   * Added functionality so that `Filter` values can be queries.
     * Using JSON: `{ field: <field>, operator: <op>, value: { query: <value query> } }`
     * Using `Key`: `Key(<field>).<op>(Key(<value_query>))`
     * For example: `Key("tag.tag1").gt(Key("tag.tag2"))`
   * Four new filters: `subset`, `!subset`, `superset`, `!superset`. These should be read 
   `field value <op> filter value`, so `subset` means all of the values returned from the field query
   are in the filter value, which allows better filtering when both the field query and value are iterable.
   * Many new specials
     * `$key_of_min_value` - Gets the key of the min value in an dict/map/object
     * `$key_of_max_value` - Gets the key of the max value in an dict/map/object
     * `$time_part(part) -> int` - Get a specific part of a datetime/moment object. Valid values for `part` are as follows:
       * 'millisecond'
       * 'second'
       * 'minute' - Starting from 0
       * 'hour' - Starting from 0
       * 'day' - Day of month, starting from 1
       * 'month' - Month of year, starting from 1
       * 'year'
       * 'dayOfWeek' - Value in 0-6, corresponding to Monday-Sunday
       * 'dayOfYear' - Day of year, starting from 1
     * `$min` and `$max`
     * `$arith(op, arg_value)` - Perform an arithmetic operation on the current value. `op` can be
     any of the support [math operators](#math-operators). 
     * `$lowercase`, `$uppercase`, and `$titlecase`
     * `$filter(field, op, value, single=true)` OR `$filter({<filter>}, single=true)` OR 
     `$filter([<filters>], single=true)` - Allow a single value or list of values to be filtered.
     The filters should be formatted that same way they are for `Filter`.
     * `$pipeline(pipeline)` - Apply multiple specials to value in a given order. Can be very useful
     when used in conjunction with `$map` to apply multiple specials at once. `pipeline` must be of format:
```
[
    <special>

    OR

    [<special>, arg1, arg2, ..., (optional) map/object/dict of keyword arguments],
    ...
]

for example

$pipeline([
    ['index', 'balance'],
    ['range', 1],
    ['replace', {'old': ',', 'new': ''}],
    ['float']
])

is the same as
$index("balance").$range(1).$replace(old=",", new="").$float
```
   * Updates to old specials
     * `$index(i, fallback=null, extended=false)` - added `extended` argument to allow
     `$index` to support any valid JQL query for `i` if `extended=true`
   * Bug fixes
     * Fixed issue with filters not shortcutting properly
     * Fixed Python issue with `$print`
     * Fixed issues with `$fallback` with `Filter` and `Formatter`
     * Fixed issue causing an error when trying to use an integer value in
     `$sort` and `$group_by`
  
## Glossary
 * [`Installation`](#installation)
 * [`Quickstart`](#quickstart)
 * [`JQL`](#jql)
   * [`Arguments`](#arguments)
   * [`Math Operators`](#math-operators)
 * [`Query`](#query)
   * [`Context`](#context)
   * [`Specials`](#specials)
 * [`Filter`](#filter)
   * [`Key`](#key)
   * [`Condition`](#condition)
 * [`Formatter`](#formatter)
 * [`Performance`](#performance)
 * [`Changelog`](#changelog)
   
## Installation

### Python
`pip install jtools`
```python
# import
from jtools import Query, Filter, Key, Condition, Formatter
```

### JavaScript
`npm i @blending_jake/jtools`
```javascript
// import
import { Query, Filter, Key, Condition, Formatter } from "@blending_jake/jtools";
```

## Quickstart
```python
from jtools import Query
# sort by nested timestamp field by month
q = Query("meta.timestamp.$parse_timestamp.$time_part('month')")
data = [ ... ]
sorted_data = sorted(data, key=q.single)
```

## `JQL`
>`JQL` or the `JSON Query Language` is a custom built query language for `JTools` which supports powerful features
>like accessing nested fields, transforming values, and even using nested queries as arguments. 
>The basic format of the language is: 
```
(<field> | $<special>) (. (<field> | $<special>))*
EX: 'data', 'data.timestamp', 'data.$split', '$split.0'
```
### field
A field is just a value that can be used as an index, like a string or integer key for a map/dict or an integer for an array. JavaScript has very loose type-checking between strings
and integers, so either can essentially work in place of the other when indexing.

Fields can only contain the following characters: `[-a-zA-Z0-9_]`. However, fields with prohibited characters can still
be indexed by using the `$index` special, so to index `range[0]` use `$index("range[0]")`.

### $special
A special is a function that is applied to the value that has been queried so far. There is a complete list of specials
[here](#specials). These specials can be passed arguments, which is one of the most powerful features
of `JQL`.

#### Arguments
Arguments can be passed into specials as a positional or keyword arguments. Positional arguments
must come first and are denoted using the standard notation in most programming languages:
`$special(arg1, arg2, ...)`. Keyword arguments must come after any positional arguments and
can be used to specify a specific argument to set the value for: 
`$special(arg1, name1=arg2, name2=arg3, ...)`. Keyword arguments can be used to make it clear
what argument you are setting - improving readability, or can be used to skip arguments which
have default values. 

For example, the index special has the following definition:
`$index(key, fallback=null, extended=false)`. If you want to use a JQL query for `key`, then you need
to set `extended=true`. You can either write `$index(key, null, true)`, or you can skip the 
fallback argument and write `$index(key, extended=true)`. Using keyword arguments might not save many 
characters if the the special has few arguments, but can still greatly improve readability.

It is important to note that arguments, and the parenthesis surrounding them can be left
completely off of a special if the default argument values are acceptable or there are no
arguments - so a query like `data.$values.$max.$divide(@data.$values.$sum)` can be written
where most of the parenthesis and arguments are just left off.

##### value
Arguments are considered `values` and must be one of the following types.
```
Math Expression
[] or [<value>(, <value>)*] - List
{} or {<value>(, <value>)*} - Set
{:} or {<key>: <value>(, <key>: <value>)*} - Map/Dict/Object (see below for <key> spec)
Integer
Float
String w/ '' or ""
true
false
null
@<query> - Yep! Nested queries!

Math Expression:
    Operators listed below
    Operands must be one of: Integer, Float, or @<query>

<key>:
    Math Expression
    @<query>    
    Integer
    Float
    String
    true
    false
    null
``` 
As shown above, values and queries can be nested, so `[[1, 2], ["bob"], {"Ann", 'Ralph'}, {'key': 4, 23: 5}]`
is valid. Additionally, the support for nesting queries is extremely powerful and allows for queries like:
`item.tag.$lookup(@table.colors)`, which, for `{"item": {"tag": "product"}, "table": {"colors": {"product": "red"}}}`
results in `"red"`

Basic math expressions are supported in arguments and, subsequently, nested values.
The supported operators are listed below and follow normal arithmetic precedence with
the order of evaluation from first -> last being: `()`, `**`, ` *  and / and // and %`,
`+ and -`.

The operands for math expressions are limited to numbers (Float and Integer) and nested
queries.

Math expressions can be nested in other values, for example: 
`$special([ 1, @value, @value**2, @value**3 ])`

##### Math Operators
* `+`
* `-`
* `*`
* `/`
* `//` - Floor division, aka `Math.floor(a / b)`
* `%` - Mod operator
* `**` - Exponentiation, aka `Math.pow(a, b)` or `a^b`
* `()` - Parenthesis can be use to change precedence and/or improve readability


## Query
>`Query` takes the power of `JQL` and puts it into practice querying and transforming values
>in JSON-like data. 

### `Query(query, fallback=null, [convert_ints=true (if Python)])`
* `query`: `str | List[str]` The field or fields to query
* `fallback`: The value that will result if a non-existent field is queried
* `convert_ints`: Whether or not to convert any digit-only fields to integers

#### `.single(item, context={})`
* `item`: The item to query
* `context`: See [`Context`](#context) for more details

>Take a single item and query it using the query(ies) provided
>
>`Query(field).single(...) -> result`
>
>`Query([field, field, ...]).single(...) -> [result, result, ...]`

#### `.many(items, context={})`
* `items`: The items to query
* `context`: See [`Context`](#context) for more details

>Take a list of items, and query each item using the query(ies) provided
>
>`Query(field).many(...) -> [result, result, ...]`
>
>`Query([field, field, ...]).many(...) -> [[result, result, ...], [result, result, ...], ...]`

### Notes
 * More specials can be added by using the class method `.register_special()` 
 like so: `Query.register_special(<name>, <func>, <argDef> [if JavaScript])`. The function should be formatted as such: 
  ```python
 # Python
lambda value, *args, context: ...
 ```
 ```javascript
// JavaScript
(value, context, args) => { ... }
 ```
Where `value` is the current query value, and `context` is the current context.

#### Registering a special in JavaScript
Registering a special works differently in JavaScript because the language does not support keyword arguments. To get
around this, an argument definition should be provided whenever the special is registered. The argument definition
should be formatted:
```javascript
[
    '<argument name>' | { 'name': '<argument name>', [ 'default': <default value> ] }
]
```
The argument definition allows you to state what the name of each parameter is, and allows a default value to be provided. 
Additionally, '$args' and '$kwargs' can be placed in the argument definition to capture a variable number of positional 
arguments or keyword arguments, respectively. 

Each registered special function is then passed an object, `args`, which is `{ <argument name>: <argument value>, ... }`.
The keys '$args' and '$kwargs' capture the variable number of positional and keyword arguments, respectively. 

Some example argument definitions and usages:
```javascript
Query.register_special('index', (value, context, args) => {
    // use args.key, args.fallback, and args.extended to access arguments
}, [ 'key', { name: 'fallback', default: null }, { name: 'extended', default: false } ])

Query.register_special('filter', (value, context, args) => {
    // args.$args is an array of any positional arguments
    // args.single must be specified as a keyword argument (as it's after $args)
}, [ '$args', { name: 'single', default: false } ])

Query.register_special('update', (value, context, args) => {
    // args.$kwargs is an object of any captured key->value pairs
    return { ...value, ...args.$kwargs };
}, [ '$kwargs' ])
```

#### Context
>Context is a way of putting temporary variables into the query search space.

##### How do I add something to `context`?
 1. Manually introduce values through `.single(..., context)` or `.many(..., context)`.
 2. Use the `$store_as()` special to place a value in the current context for later use

##### How do I access something in `context`?
 1. Any top-level field name is first looked for on the current item, then in `context`. Note, top-level means
 it is the main query in a `Query` string, or it follows an `@`, either as an argument or in a `Formatter` string.
 2. It is important to note that fields on the current item will shadow fields in the context, so make sure to use unique field names.

##### Ok, but give me an example.
```python
# Python
context = {
  "NOW": time.time()
}

Query("NOW.$subtract(@meta.timestamp).$divide(86400).$round.$suffix(' Days Ago')").single({ ... }, context)
```
```javascript
// JavaScript
const context = {
  NOW: Date.now() / 1000
}

new Query("NOW.$subtract(@meta.timestamp).$divide(86400).$round.$suffix(' Days Ago')").single({ ... }, context)
```
 
#### Specials
General
  * `$inject(value: any) -> any`: Inject a value into the query
  * `$length -> int`
  * `$lookup(lookup: dict, fallback=null) -> any`: Lookup the current value in the provided map/dict 
  * `$store_as(name: string) -> any`: Store the current query value in the current context for later use in the query. This does not 
   change the underlying data being queried.
  * `$pipeline(pipeline) -> any`: Take a value and run it through multiple specials. Can be used in conjunction
  with `$map` or `$value_map` to apply a series of transformations across a list of values. `pipeline` must
  be a list where each value is:
    * `string` - Name of special
    * `[string, *args]` - Name + positional arguments
    * `[string, dict of keyword args]` - Name + dict/map/object of keyword arguments
    * `[string, *args, dict of keyword args]` - Name + positional arguments +
    dict/map/object of keyword arguments
```python
# Python
Query("""
    meta    
    .timestamp
    .$pipeline([
        ['divide', 1000],
        'parse_timestamp',
        ['time_part', 'year']
    ])
""")
```
  * `$print -> any`: Print the current query value before continuing to pass that value along
  * `$filter(field, op, value, single=true)` OR `$filter({<filter>}, single=true)` OR 
     `$filter([<filters>], single=true)`: Allow a single value or list of values to be filtered.
     The filters should be formatted that same way they are for `Filter`. `single` can only be supplied
     as a keyword argument.
  
Dict/Maps/Objects
  * `$items -> List[[any, any]]`
  * `$keys -> List[any]`
  * `$key_of_max_value(just_key=true) -> any | [any, any]`: Find the key of the max value in a dict/object/map. If
  `just_key=true`, then just the value of the key will be returned. Otherwise, the `[key, value`] will be
  returned.
  * `$key_of_min_value(just_key=true) -> any | [any, any]`: Find the key of the min value in a dict/object/map. If
  `just_key=true`, then just the value of the key will be returned. Otherwise, the `[key, value`] will be
  returned.
  * `$wildcard(nxt, just_field=true) -> List[any]`: On a given map or list, go through all values and see if `nxt` is
  a defined field. If it is, then return just the value of `nxt` on that item, if `just_field=true`, or the entire 
  item otherwise. This special allows a nested field to be extracted across multiple items where it it present. 
  For example: 
```python
# Python
data = {
  "a": {"tag": "run"},
  "b": {"tag": "to-do", "other": "task"},
  "meta": None
}
Query('$wildcard("tag")').single(data)  # => ["run", "to-do"]
Query('$wildcard("tag", false)').single(data) # => [{"tag": "run"}, {"tag": "to-do", "other": "task"}]
```
```javascript
// JavaScript
let data = {
  "a": {"tag": "run"},
  "b": {"tag": "to-do", "other": "task"},
  "meta": null
}
new Query('$wildcard("tag")').single(data)  // => ["run", "to-do"]
new Query('$wildcard("tag", false)').single(data) // => [{"tag": "run"}, {"tag": "to-do", "other": "task"}]
```
 * `$values -> List[any]`
 * `$value_map(special, duplicate=true, *args, **kwargs): Dict[any: any]`: Go through the values on the current item in the query, applying a special
 to each one in-place. If `duplicate=true`, then the original value will not be modified. Similar to:
 ```python
# Python
for key in value:
    value[key] = SPECIALS[special](value[key], *args, **kwargs)
 ```
 ```javascript
 // JavaScript
Object.keys(value).forEach(key => {
    value[key] = SPECIALS[special](value[key], ...args, ...kwargs);
});
 ```
  
Type Conversions
  * `$dict -> Dict[any: any]`: Take an incoming list of `(key, value)` pairs and make a map/dict/object out of them.
  * `$fallback(fallback) -> value or fallback`: If the value is `null`, then it will be replaced with `fallback`.
  * `$float -> float`
  * `$int -> int`
  * `$not -> bool`: Returns `not value` or `!value`
  * `$set -> set`
  * `$string -> str`
  * `$ternary(if_true, if_false, strict=false) -> any`: Return `if_true` if the value is `truish`, otherwise,
  return `if_false`. Pass `true` for `strict` if the value must be `true` and not just `truish`.
  
Datetime 
  * `$parse_timestamp -> datetime or moment`: Take a Unix timestamp in seconds and return a corresponding datetime/moment object
  * `$strftime(fmt="%Y-%m-%dT%H:%M:%SZ" or "YYYY-MM-DD[T]HH:mm:ss[Z]") -> string`: Format a datetime/moment object as a string using `fmt`. Refer to [datetime](#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) or 
  [moment](#https://momentjs.com/docs/#/parsing/string-format/) for formatting instructions
  * `$strptime(fmt=null) -> datetime or moment`: Parse a datetime string and return a corresponding datetime/moment object.
  If `fmt=None`, then standard formats will be tried. Refer to [datetime](#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) or 
  [moment](#https://momentjs.com/docs/#/parsing/string-format/) for formatting instructions
  * `$timestamp -> int`: Dump a datetime/moment object to a UTC timestamp as the number of seconds since the Unix Epoch
  * `$time_part(part) -> int`: Take a `datetime` or `moment` value and get a specific part of
  the date. `part` can be:
    * `millisecond`
    * `second`
    * `minute`
    * `hour`
    * `day`
    * `month`
    * `year`
    * `dayOfWeek`
    * `dayOfYear`
  
Math / Numbers
  * `$abs(num) -> number`
  * `$add(num) -> number`
  * `$arith(op, arg_value) -> number`: Take the value and use it as the first operand of an
  expression with the specified math operator. `op` can be any of the [math operators](#math-operators).
  The expression will be `value op arg_value`. 
  * `$distance(other) -> float`: Euler distance in N-dimensions
  * `$divide(num) -> number`
  * `$math(attr, ...args) -> any`: Returns `math[attr](value, ...args)`, which can be used for
  operations like `floor`, `cos`, `sin`, `min`, etc. See the [Python Docs](#https://docs.python.org/3/library/math.html) 
  for valid `attr` values in Python and the [JavaScript Docs](#https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math) 
  for valid `attr` values in JavaScript.
  * `$multiply(num) -> number`
  * `$pow(num) -> number`
  * `$round(n=2) -> number`
  * `$subtract(num) -> number`
  
Strings
  * `$lowercase -> string`
  * `$prefix(prefix) -> string`: Prefix the value with the specified string
  * `$replace(old, new) -> string`: Replace all occurrences of a string 
  * `$split(on=" ") -> List[string]`: Split a string
  * `$strip -> string`: Strip leading and trailing whitespace
  * `$suffix(suffix) -> string`: Concatenate a string to the end of the value
  * `$titlecase -> string`
  * `$trim(length=50, suffix="...") -> string`: Trim the length of a string
  * `$wrap(prefix, suffix) -> string`: Wrap a string with a prefix and suffix. Combines features of above two specials.
  * `$uppercase -> string`
  
Lists
  * `$group_by(key="", count=false) -> Dict[any: any[] | int]`: Take an incoming list and group the values 
  by the specified key. Any valid JQL query or integer can be used for the key. `""` means the value itself. 
  The result by default will be keys to a list of values. However, if `count=true`, then the result will be keys 
  to the number of elements in that group.
  * `$index(key, fallback=null, extended=false) -> any`: Index the current piece of data either using
  a string or index key, or a full JQL query if `extended=true`. If the index is invalid, then `fallback` will
  be returned. If `extended=false` and `key` is an integer, then a negative key can be used to index from the
  end of the array.
  * `$join(sep=", ") -> string`: Join a list using the specified separator
  * `$join_arg(arg: List[any], sep=", ")`: Similar to `$join` except this operates on an argument instead of the query value.
  Essentially a shortened form of `$inject(arg).$join(sep)`.
  * `$map(special, *args, **kwargs) -> List[any]`: Apply `special` to every element in the 
  value. Arguments can be passed through to the special being used.
  * `$max -> number`: Find the max value in the list
  * `$min -> number`: Find the min value in the list
  * `$sum -> number`: Return the sum of the items in the value
  * `$range(start, end=null) -> List[any]`: Get a sublist. Defaults to `value.slice(start)` or `value[start:]`, 
  but an end value can be specified. Negative indices are allowed. 
  * `$remove_nulls -> List[any]`: Remove any values that are `None` if Python, or `null` and `undefined` if JavaScript
  * `$sort(key="", reverse=false) -> List[any]`: Sort an incoming list of values by a given key which can be any valid JQL query
  or an integer. By default, `key=""` means the top-level value will be sorted on.
  
 Attributes
  * `$attr(attr) -> any`: Access an attribute of the given object, implemented as `getattr(value, attr)` and `value[attr]`
  * `$call(func, *args, **kwargs) -> any`: Call a function that is on the current value, implemented as `getattr(value, func)(*args)` and `value[func](...args)`


## Filter
>`Filter` takes the power of `JQL` and combines it with 
>filtering conditions to allow lists of items to be filtered down to just those of 
>interest. The filters can be manually built, or the `Key` and `Condition` classes can 
>be used to simplify your code.

### `new Filter(filters, [convert_ints=true (if Python)], empty_filters_response=true, missing_field_response=false)`
 * `filters`: `Condition | List[dict]` The filters to apply to any data. If `List[dict]`, then the
 filters should be formatted as shown below.
```
[
    {"field": <field>, "operator": <op>, "value": <value>},

    OR

    {"or": <nested outer structure>},
    
    OR

    {"not": <nested outer structure>},

    ...
]
<field>: any valid `JQL` query
<op>: See list below
<value>: Any valid value for the operator, or 
    { "query": <JQL query> } to have a value which is a query
``` 
 * `convert_ints`: `bool` Corresponds with the argument with the same name in `Query`. Determines
 whether digit only fields are treated as integers or strings. Defaults to `true`.
 * `empty_filters_response`: `bool` Determines what gets returned when no filters are supplied.
 * `missing_field_response`: `bool` Determines the result of a filter where the field could not be found.
 
Filters are evaluated in order and short-cutting can be used to avoid executing filters.
For example, a `present` operator can be used before trying to access or manipulate a field.
Additionally, the `$fallback` special can be used to the same effect in certain cases.

#### `.single(item, context={})`
 * `context`: See [`Context`](#context) for more details
>Take a single item and determine whether it satisfies the filters or not
>
>`Filter(filters).single(...) -> boolean`

#### `.many(items, context={})`
 * `context`: See [`Context`](#context) for more details
>Take a list of items, and returns only those which satisfy the filters. Note, `Filter.many()` introduces `INDEX` into
the query namespace. Allowing items to be filtered by their 0-based index.
>
>`Filter(filters).many(...) -> [result, result, ...]`

### Notes
```
{"or": [ 
    [ {filter1}, {filter2} ], 
    {filter3} 
]} === (filter1 AND filter2) OR filter3
``` 
>Nesting in an `or` will cause those filters
>to be `AND'd` and then everything in the toplevel of that `or` will be `OR'd`.

Operators:
 * `>`
 * `<`
 * `>=`
 * `<=`
 * `==`
 * `!=`
 * `===`
 * `!==`
 * `in`: `<field> in <value>`
 * `!in`
 * `contains`: `<value> in <field>`
 * `!contains`
 * `subset`: `x in <value> for x in <field>`
 * `!subset`: `exists x in <field> such that x not in <value>`
 * `superset`: `x in <field> for x in <value>`
 * `!superser`: `exists x in <value> such that x not in <field>`
 * `interval`: `<field> in interval [value[0], value[1]]` (closed/inclusive interval)
 * `!interval`: `<field> not in interval [value[0], value[1]]` 
 * `startswith`
 * `endswith`
 * `present`
 * `!present`


#### Key
>Intended to simplify having to write `{"field": <field>, "operator": <operator>, "value": value}` 
>a lot. The basic usage is: `Key(<field>).<op>(<value>)`, or for the first six 
>operators, the actual Python operators can be used, so `Key(<field>) <op> <value>`.
>For example: `Key("meta.id").eq(12)` is the same as `Key("meta.id") == 12`,
>which is the same as `{"field": "meta.id", "operator": "==", "value": 12}`.

>To use a filter where the value is a query itself, use `Key(<field>)` as the value.
>For example: `Key("tags.tag1").gt(Key("tag.tag2"))`.

>The table below describes all of the functions which map to the underlying conditions. 
>Additionally, several other methods are provided to simplify certain aspects of 
>building filters and conditions:

* `Key(field).is_true()`: Same as `Key(field).seq(true)`
* `Key(field).is_false()`: Same as `Key(field).seq(false)`
* `Key(field).is_null()`: Same as `Key(field).seq(null)`
* `Key(field).op(operator).value(value)`: Same as `Key(field).<op>(value)`. Can be used for times when
you want to construct a filter and the operator is dynamic.

Operators: 

| underlying operator | `Key` function | `Python` operator |
| ------------------- | -------- | -------- |
| `>` | `gt` | `>` | 
| `<` | `lt` | `<` | 
| `<=` | `lte` | `<=` | 
| `>=` | `gte` | `>=` | 
| `==` | `eq` | `==` | 
| `!=` | `ne` | `!=` | 
| `===` | `seq` | N/A |
| `!==` | `sne` | N/A
| `in` | `in_` | N/A | 
| `!in` | `nin` | N/A | 
| `contains` | `contains` | N/A | 
| `!contains` | `not_contains` | N/A | 
| `subset` | `subset` | N/A | 
| `!subset` | `not_subset` | N/A | 
| `superset` | `superset` | N/A | 
| `!superset` | `not_superset` | N/A | 
| `interval` | `interval` | N/A |
| `!interval` | `not_interval` | N/A |
| `startswith` | `startswith` | N/A | 
| `endswith` | `endswith` | N/A | 
| `present` | `present` | N/A | 
| `!present` | `not_present` | N/A | 

#### Condition
>Intended to be used in combination with `Key` to make creating filters
>easier than manually creating the `JSON`. There are three conditions supported:
>`and`, `or`, and `not`. They can be manually accessed via `and_(...conditions)`, `or_(...conditions)`, and `not_()`.
>
>The conditions can also be accessed through the overloaded operators `&`, `|`, and `~`, respectively, if in Python. 
>**Caution: `&` and `|` bind tighter than the comparisons operators and `~` binds the tightest**
>
>`Key("first_name") == "John" | Key("first_name") == "Bill"` is actually
`(Key("first_name") == ("John" | Key("first_name"))) == "Bill"`, not
`(Key("first_name") == "John") | (Key("first_name") == "Bill")`

##### `Condition.ander(cond1, cond2, *conditions)`
>AND two or more conditions together

##### `Condition.orer(cond1, cond2, *conditions)`
>OR two or more conditions together

##### `.and_(*conditions)`
>AND the current condition with multiple other conditions

##### `.or_(*conditions)`
>OR the current condition with multiple other conditions

##### `.not_()`
>NOT the current condition

##### `.clone(deep=false)`
>Clone the current condition. If deep, then all aspects will be duplicated.

##### `.traverse(callback, on_duplicate=false) -> Condition`
>Traverse through all of the filters in the current condition, calling `callback(filter)` with each one.
>`on_duplicate` indicates whether the current condition is iterated over, or a duplicate.
>Whatever condition was iterated over will be returned.

##### `.to_list() -> list`
>Return a list of filters/conditions for this condition

##### `Condition.from_list(conditions) -> Condition`
>Take a list of filters/conditions and make a Condition object out of it

Examples
```python
# Python
Key("state").eq("Texas") | Key("city").eq("New York")

(Key("gender") == "male") & (Key("age") >= 18) & (Key("selective_service") == False)

Key('creation_time.$parse_timestamp.$attr("year")').lt(2005).or_(
    Key('creation_time.$parse_timestamp.$attr("year")').gt(2015)
).and_(
    Key("product_id") == 15
)
# (year < 2005 OR year > 2015) AND product_id == 15
```

```javascript
// JavaScript
Key('creation_time.$parse_timestamp.$call("year")').lt(2005).or_(
    Key('creation_time.$parse_timestamp.$call("year")').gt(2015)
).and_(
    Key("product_id").seq(15)
);
```

## Formatter
> `Formatter` allows fields to be queried from an object and then formatted
>into a string. Any queries in a format string should be prefixed with `@` and any valid `JQL` query can be used. For example, 
>`new Formatter('Name: @name}').single({"name": "John Smith"})` results in
>`Name: John Smith`.

### `Formatter(spec, fallback="<missing>", [convert_ints=true (if Python)])`
 * `spec`: `str` The format string
 * `fallback`: `str` The value that will be used in the formatted string if a query could not be performed. For example, if the field `missing` does exist, then the query `"Age: @missing"` will result in `"Age: <missing>"`
 * `convert_ints`: `bool` Whether digit-only fields get treated as integers or strings
 
#### `.single(item, context={})`
 * `context`: See [`Context`](#context) for more details
> Return a formatted string or the fallback value if the query fails

#### `.many(items, context={})`
 * `context`: See [`Context`](#context) for more details
> Return a list of formatted strings or the fallback value.

### Notes
>The differences between `Query` and `Formatter` are:
 * `Query` can return a value of any type, `Formatter` just returns strings
 * `Formatter` supports multiple queries, end-to-end, `Query` does not
 * All queries must be prefixed with `@` with `Formatter`, not just when used as an argument like with `Query`
 * Both support all the features of `JQL`
 * `Query` actually can theoretically do everything `Formatter` does by using `$prefix`, `$suffix`, and `$string`. 
 For example, `'@name @age'` -> `'name.$suffix(" ").$suffix(@age)'`. However, the latter is much longer than the former
 
Example (flattening operations):

```python
# Python
errors = {
    "errors": {
        "Process Error": "Could not communicate with the subprocess",
        "Connection Error": "Could not connect with the database instance"
    }
}

Formatter('Errors: \n@errors.$items.$map("join", ": \\n\\t").$join("\\n")').single(errors)
# Errors:
# Process Error: 
#   Could not communicate with the subprocess
# Connection Error: 
#   Could not connect with the database instance
```

```javascript
// JavaScript
const errors = {
    errors: {
        "Process Error": "Could not communicate with the subprocess",
        "Connection Error": "Could not connect with the database instance"
    }
};

new Formatter('Erros: @errors.$items.$map("join", ": \\n\\t").$join("\\n")}').single(errors);
// Errors: 
// Process Error: 
//   Could not communicate with the subprocess
// Connection Error: 
//   Could not connect with the database instance
```
>The above example shows a powerful usage of flattening `errors` into its items,
>then joining each item; splitting the error name and message between lines, then
>joining all the errors together.

Example (nested replacement):

```python
# Python
item = {
    "x1": 1,
    "y1": 1,
    "x2": 12,
    "y2": 54
}

Formatter(
    "Midpoint: [@x2.$subtract(@x1).$divide(2), @y2.$subtract(@y1).$divide(2)]"
)
# Midpoint: [5.5, 26.5]
```

```javascript
// JavaScript
const item = {
    x1: 1,
    y1: 1,
    x2: 12,
    y2: 54
};

new Formatter(
    "Midpoint: [@x2.$subtract(@x1).$divide(2), @y2.$subtract(@y1).$divide(2)]"
).single(item);
// Midpoint: [5.5, 26.5]
```


## Performance
>There are several ways to increase the performance of querying, filtering, and formatting. The performance gains can be had
>by limiting the amount of times a query string has to be parsed. This means that using a `Query`,
>`Filter`, or `Formatter` object multiple times will be faster then creating a new object every time. 

Examples:
```python
# Python
# slower
for item in items:
    f = Query("timestamp.$parse_timestamp").single(item)
    # do other stuff

# faster
query = Query("timestamp.$parse_timestamp")
for item in items:
    f = query.single(item)
    # do other stuff
```

```javascript
// JavaScript
// slower
items.forEach(item => {
  let f = new Query("timestamp.$parse_timestamp").single(item);
  // do other stuff
});

// faster
const query = new Query("timestamp.$parse_timestamp");
items.forEach(item => {
  let f = query.single(item);
  // do other stuff
});
```

>Across 10,000 runs:
* Python
   * reusing `Query` can improve performance by 302x
   * reusing `Filter` can improve performance by 132x
   * reusing `Formatter` can improve performance by 377x.
* JavaScript
   * reusing `Query` can improve performance by 192
   * reusing `Filter` can improve performance by 120x
   * reusing `Formatter` can improve performance by 210x.

## Changelog
 * `1.1.5`
   * Unify `README` between Python and JavaScript versions
   * Expand documentation

 * `1.1.4`
   * Added `$value_map`, which allows the values on an map/dict/object to be modified with a special, either in-place
   or on a duplicate
   * Exposed `context` so additional fields can manually be put into the current query space. This was already 
   being used by `$store_as`. `context` can be passed to any `.single()` or `.many()` call.
   * Additionally, `Filter.many()` is now placing `INDEX` into the query space to allow
   items to be filtered by their 0-based index
   * Exposed many of the internal TypeScript types
   
 * `1.1.3`
   * Changed the behavior of `new Query("")`, from returning the fallback value, to returning the source data element itself.
  For example, `new Query("").single(data) === data`.
   * Added `SpecialNotFoundError`, which is raised when an invalid special is queried. Can be imported as 
  `import { SpecialNotFoundError } from "@blending_jake/jtools";`
   * Added new specials
     * `$store_as(name)` Store the current query value in the current context for later use in the query. This does not 
   change the underlying data being queried.
     * `$group_by(key="", count=false)` Take an incoming list and group the values by the specified key.
   Any valid JQL query can be used for the key, so `""` means the value itself. The result by default will be
   keys to a list of values. However, if `count=true`, then the result will be keys to the number of elements with each 
   key.
     * `$sort(key="", reverse=false)` Sort an incoming list of values by a given key which can be any valid JQL query.
   By default, `key=""` means the top-level value will be sorted on.
     * `$dict` Take an incoming list of `(key, value)` pairs and make a dict out of them.
     * `$join_arg(arg, sep=', ')` Similar to `$join` except this operates on an argument instead of the query value.
   Essentially a shortened form of `$inject(arg).$join(sep)`.
   * Changed the underlying special function definition to now include the keyword argument `context`. This argument is 
  implemented to only be accessed by name to avoid collision if the user provides too many arguments in their query. 
  The purpose of the context is to support specials adding values temporarily to the data
  namespace of the query, like `$store_as` does.

 * `1.1.2`
   * Version `1.1.1` was skipped to keep on track with `JTools-Py`
   * Catch and handle `Extraneous Input Error`
   * Change `JQL` so that field and special names must only contain `[-a-zA-Z0-9_]`. `$index` can be used to get fields
   with prohibited characters. The change was to support more formatting use-cases, like `Age: @age, DOB: @dob`, which 
   previously would have failed because the `,` would have been considered part of the field name.
   * Change `Formatter` so that `fallback` is just a string that is substituted for invalid queries, instead of being
   the entire return value. Previously, `"Age: @missing"` would result in `None`, now it results in `"Age: <missing>"`.
   This change allows for better debugging as it becomes clear exactly which queries are failing.
   * Add function docstrings

 * `1.1.0`
   * Rename `Getter` to `Query` to more accurately describe what the class does
   * Migrate queries to use `JQL`
     * The migration opens the door to nested queries in `Query`, allowing queries, prefixed with `@` to be used
     as arguments to specials, or even as values in the supported argument data structures
     * Special arguments are no longer parsed as `JSON`, allowing features like sets, query nesting, and support
     for single and double quoted strings.
     * Formatter no longer uses `{{}}` to surround queries. Instead, all queries must be prefixed with `@`, so
     `"{{name}} {{age}}"` -> `"@name @age"`. `@@` must be used to get a literal `@` in a formatted string:
     `"bob@@gmail.com"` -> `"bob@gmail.com"`
     * Formatter got about a 2x performance boost
   * Added `$wrap(prefix, suffix)` to combine `$prefix` and `$suffix`
   * Added `$remove_nulls`
   * Added `$lookup(map, fallback=None)`
   * Added `$wildcard(next, just_value=True)`, which allows level of nesting to be "skipped", such that a list
   of sub-values where `next` is present
   * Added a `fallback` argument to `$index`
   * Added `$print` to display the current value in the query
   * Added `$inject` to allow any valid argument value to be injected into the query to be
  accessed and transformed by subsequent fields and specials

 * `1.0.6`
   * Migrate to TypeScript, so a declaration file is now included in the distribution
   * Add this `README`
   * Add `===` and `!==` filters for strict equality checking. The methods `seq` and `sne` have
   been added to `Key` to correspond with the new filters.
   * Rename `null` -> `!present` and `!null` -> `present`. Corresponding methods have been renamed
   to `not_present` and `present`. This filter will catch values that are `null` or `undefined`.
   * Make membership filters (`in`, `contains`, `!in` and `!contains`) work properly with 
   strings, arrays, associative arrays, and sets.
   * Remove `$datetime`. See below for replacement.
   * Add `$call` and `$attr` for calling a function and accessing an attribute. Can be used to replace
   `$datetime` functionality.
   * Remove `Formatter.format` and add `Formatter.single` and `Formatter.many` to be consistent across
   other classes and support formatting arrays of items.
   * Add more tests to increase coverage and do basic performance testing
