 # JTools
>JTools is a robust library for interacting with JSON-like objects:
>providing the ability to quickly query, format, and filter JSON-like data.
>
>There are three main components:
 * `Query`: Extract and transform the value of nested fields.
   * `Query("data.timestamp.$parse_timestamp.$attr('year')").many(items)`
 * `Filter`: Combine the querying capabilities of `Query` with the ability
 to define filtering conditions to find just the elements you want.
   * `Filter(Key("data.timestamp.$parse_timestamp.$attr('year')") > 2015).many(data)`
 * `Formatter`: Take multiple queries and format them into a string
   * `Formatter("Item @data.id was released in @data.timestamp.$parse_timestamp.$attr('year')").single(data[0])`
>
>A companion to the JavaScript version of this package: [@blending_jake/jtools](#https://www.npmjs.com/package/@blending_jake/jtools).
>The JavaScript version supports almost the exact same specials, filters, and formatting specification, with the
>goal of making it a seamless experience to go from querying/filtering/formatting in JavaScript to Python and back.

## Recent Changes
 * `1.1.3`
  * Changed the behavior of `Query("")`, from returning the fallback value, to returning the source data element itself.
  For example, `Query("").single(data) == data`.
  * Added `SpecialNotFoundError`, which is raised when an invalid special is queried. Can be imported as 
  `from jtools import SpecialNotFoundError`
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
   
## Glossary
 * [`Installation`](#install)
 * [`JQL`](#jql)
 * [`Query`](#query)
   * [`Specials`](#specials)
 * [`Filter`](#filter)
   * [`Key`](#key)
   * [`Condition`](#condition)
 * [`Formatter`](#formatter)
 * [`Performance`](#performance)
 * [`Changelog`](#changelog)
   
## <a name="install">Installation</a>
`pip install jtools`
```python
# import
from jtools import Query, Filter, Key, Condition, Formatter
```

## <a name="jql">`JQL`</a>
>`JQL` or the `JSON Query Language` is a custom built query language for `JTools` which supports powerful features
>like accessing nested fields, transforming values, and even using nested queries as arguments. 
>The basic format of the language is: 
```
(<field> | $<special>) (. (<field> | $<special>))*
EX: 'data', 'data.timestamp', 'data.$split', '$split.0'
```
#### field
A field is just a value that can be used as an index, like a string or integer key for a map/dict, or an integer for an
array. By default, any field that can be treated as an integer will be. However, this assumes that any field containing 
only digits was intended to be an integer index, which isn't always the desired behavior. To stop digit-only 
strings from becoming integers, set `convert_ints=False` when creating the query/filter/formatter.

Fields can only contain the following characters: `[-a-zA-Z0-9_]`. However, fields with prohibited characters can still
be indexed by using the `$index` special, so to index `range[0]` use `$index("range[0]")`.

#### $special
A special is a function that is applied to the value that has been queried so far. There is a complete list of specials
[here](#specials). These specials can be passed arguments, which is one of the most powerful features
of `JQL`. The syntax is similar to most programming languages: `$<special>(<value>(, <value>)*)`. Just to note, `$<special>()`
is valid, as is `$<special>`. Many of the specials don't require any arguments, or have default values, allowing
the parenthesis to be left off.

##### value
A `<value>` can be:
```
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

<key>:
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

## <a name="query">Query</a>
>`Query` takes the power of `JQL` and puts it into practice querying and transforming values
>in JSON-like data. 

### `Query(query, convert_ints=True, fallback=None)`
* `query`: `str | List[str]` The field or fields to query
* `convert_ints`: Whether or not to convert any valid fields to integers
* `fallback`: The value that will result if a non-existent field is queried

#### `.single(item)`
>Take a single item and query it using the query(ies) provided
>
>`Query(field).single(...) -> result`
>
>`Query([field, field, ...]).single(...) -> [result, result, ...]`

#### `.many(items)`
>Take a list of items, and query each item using the query(ies) provided
>
>`Query(field).many(...) -> [result, result, ...]`
>
>`Query([field, field, ...]).many(...) -> [[result, result, ...], [result, result, ...], ...]`

### Notes
 * Lists can be indexed as long as `Query(..., convert_ints=True)`,
 which is set to `True` by default. This allows paths like `friends.0`. However, `convert_ints=False`
 should be used if trying to access fields whose keys are strings containing digits, like
 `{"index": {"0": ...}}`. Use `$index` if you have mixed data where there are some cases where you need to use
 an integer and other times where the digits-only string needs to stay as a string, like in:
 `Query("item.0.$index(0)").single({"item": {"0": ["tag"])}) -> 'tag'`
 
 * Fields can be indexed after specials, so `$split.0` is completely valid
 
 * You don't have to use `()` at the end of a special if there aren't any 
 arguments, or the default arguments are acceptable.
 
 * More specials can be added by using the class attribute `.register_special()` 
 like so: `Query.register_special(<name>, <func>)`. The function should take
 at least one argument positional argument, which is the current value in the query string,
 and the keyword argument 'context' at the end: `lambda value, *args, context: ...`
 
### <a name="specials">Specials</a>
>Below is a list of all of the specials that can be used. Additionally, more can be added
>as discussed above. 

General
  * `$length -> int`
  * `$lookup(map: dict, fallback=None) -> any`: Lookup the current value in the provided map/dict 
  * `$inject(value: any) -> any`: Inject a value into the query
  * `$print -> any`: Print the current query value before continuing to pass that value along
  * `store_as(name: str) -> any`: Store the current query value in the current context for later use in the query. This does not 
   change the underlying data being queried.
  * `group_by(key="", count=false) -> Dict[any, Union[List[any], int]]`: Take an incoming list and group the values 
  by the specified key. Any valid JQL query can be used for the key, so `""` means the value itself. 
  The result by default will be keys to a list of values. However, if `count=true`, then the result will be keys 
  to the number of elements with each key.
  
Maps
  * `$keys -> list`
  * `$values -> list`
  * `$items -> List[tuple]`
  * `$wildcard(next, just_value=true) -> List[any]`: On a given map or list, go through all values and see if `next` is
  a defined field. If it is, then return just the value of `next` on that item, if `just_value=true`, or the entire 
  item otherwise. This special allows a nested field to be extracted across multiple items where it it present. 
  For example: 
```python
data = {
    "a": {"tag": "run"},
    "b": {"tag": "to-do", "other": "task"},
    "meta": None
}
Query('$wildcard("tag")').single(data)  # => ["run", "to-do"]
Query('$wildcard("tag", false)').single(data) # => [{"tag": "run"}, {"tag": "to-do", "other": "task"}]
```
  
Type Conversions
  * `$set -> set`
  * `$float -> float`
  * `$string -> str`
  * `$dict -> dict`: Take an incoming list of `(key, value)` pairs and make a dict out of them.
  * `$int -> int`
  * `$not -> bool`: Returns `!value`
  * `$fallback(fallback) -> value or fallback`: If the value is None, then it will be replaced with `fallback`.
  * `$ternary(if_true, if_false, strict=false) -> any`: Return `if_true` if the value is `truish`, otherwise,
  return `if_false`. Pass `true` for `strict` if the value must be `True` and not just `truish`.
  
Datetime 
  * `$parse_timestamp -> datetime`: Take a Unix timestamp in seconds and return a corresponding datetime object
  * `$strptime(fmt=null) -> datetime`: Parse a datetime string and return a corresponding datetime object.
  If `fmt=null`, then common formats will be tried. Refer to 
  https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior for formatting instructions
  * `$timestamp -> float`: Dump a datetime object to a UTC timestamp as a float
  * `$strftime(fmt="%Y-%m-%dT%H:%M:%SZ") -> str`: Format a datetime object as a string using `fmt`.
  Refer to https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior for formatting instructions
  
Math / Numbers
  * `$add(num) -> Union[int, float]`
  * `$subtract(num) -> Union[int, float]`
  * `$multiply(num) -> Union[int, float]`
  * `$divide(num) -> float`
  * `$pow(num) -> Union[int, float]`
  * `$abs(num) -> Union[int, float]`
  * `$distance(other) -> float`: Euler distance in N-dimensions
  * `$math(attr) -> any`: Returns `math.<attr>(value)`, which can be used for
  operations like `floor`, `cos`, `sin`, etc.
  * `$round(n=2) -> float`
  
Strings
  * `$prefix(prefix) -> str`: Prefix the value with the specified string
  * `$suffix(suffix) -> str`: Concatenate a string to the end of the value
  * `$wrap(prefix, suffix) -> str`: Wrap a string with a prefix and suffix. Combines features of above two specials.
  * `$strip -> str`: Strip leading and trailing whitespace
  * `$replace(old, new) -> str`: Replace all occurrences of a string 
  * `$trim(length=50, suffix="...") -> str`: Trim the length of a string
  * `$split(on=" ") -> List[str]`: Split a string
  
Lists
  * `$sum -> Union[float, int]`: Return the sum of the items in the value
  * `$join(sep=", ") -> str`: Join a list using the specified separator
  * `$join_arg(arg: list, sep=", ")`: Similar to `$join` except this operates on an argument instead of the query value.
  Essentially a shortened form of `$inject(arg).$join(sep)`.
  * `$index(index, fallback=null) -> any`: Index a list. Negative indices are allowed.
  * `$range(start, end=null) -> `: Get a sublist. Defaults to `value[start:]`, 
  but an end value can be specified. Negative indices are allowed.
  * `$remove_nulls -> List[any]`: Remove any values that are `None`
  * `$sort(key="", reverse=false)`: Sort an incoming list of values by a given key which can be any valid JQL query.
  By default, `key=""` means the top-level value will be sorted on.
  * `$map(special, *args) -> list`: Apply `special` to every element in the 
  value. Arguments can be passed through to the special being used, like `$map("index", "name")`
  
Attributes
  * `$call(func, *args) -> any`: Call a function that is on the current value, implemented as `getattr(value, func)(*args)`
  * `$attr(attr) -> any`: Access an attribute of the given object, implemented as `getattr(value, attr)`

## <a name="filter">Filter</a>
>`Filter` takes the power of `JQL` and combines it with 
>filtering conditions to allow lists of items to be filtered down to just those of 
>interest. The filters can be manually built, or the `Key` and `Condition` classes can 
>be used to simplify your code.

### `Filter(filters, convert_ints=True, empty_filters_response=True, missing_field_response=False)`
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
<value>: Anything that makes sense for the operator
``` 
 * `convert_ints`: `bool` Corresponds with the argument with the same name in `Query`. Determines
 whether digit only fields are treated as integers or strings. Defaults to `True`.
 * `empty_filters_response`: `bool` Determines what gets returned when no filters are supplied.
 * `missing_field_response`: `bool` Determines the result of a filter where the field could not be found.

#### `.single(item)`
>Take a single item and determine whether it satisfies the filters or not
>
>`Filter(filters).single(...) -> True/False`

#### `.many(items)`
>Take a list of items, and returns only those which satisfy the filters
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
 * `===`: same as `==` in Python
 * `!==`: same as `!=` in Python
 * `in`: `<field> in <value>`
 * `!in`
 * `contains`: `<value> in <field>`
 * `!contains`
 * `interval`: `<field> in interval [value[0], value[1]]` (closed/inclusive interval)
 * `!interval`: `<field> not in interval [value[0], value[1]]` 
 * `startswith`
 * `endswith`
 * `present`
 * `!present`

#### <a name="key">Key</a>
>Intended to simplify having to write `{"field": <field>, "operator": <operator>, "value": value}` 
>a lot. The basic usage is: `Key(<field>).<op>(<value>)`, or for the first six 
>operators, the actual Python operators can be used, so `Key(<field>) <op> <value>`.
>For example: `Key("meta.id").eq(12)` is the same as `Key("meta.id") == 12`,
>which is the same as `{"field": "meta.id", "operator": "==", "value": 12}`.

>The table below describes all of the functions which map to the underlying conditions, but, in
>addition, there is the `.operator(op: str)` function which can be use to build a filter.
>For example: `Key(<field>).operator(<op>).value(<value>)` is the same as 
>`{"field": <field>, "operator": <op>, "value": <value>}`

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
| `interval` | `interval` | N/A |
| `!interval` | `not_interval` | N/A |
| `startswith` | `startswith` | N/A | 
| `endswith` | `endswith` | N/A | 
| `present` | `present` | N/A | 
| `!present` | `not_present` | N/A | 

#### <a name="condition">Condition</a>
>Intended to be used in combination with `Key` to make creating filters
>easier than manually creating the `JSON`. There are three conditions supported:
>`and`, `or`, and `not`. They can be manually accessed via `and_(*args)`, `or_(*args)`, and `not_()`, 
>or through the overloaded operators `&`, `|`, and `~`, respectively.

**Caution: `&` and `|` bind tighter than the comparisons operators and `~` binds the tightest**
`Key("first_name") == "John" | Key("first_name") == "Bill"` is actually
`(Key("first_name") == ("John" | Key("first_name"))) == "Bill"`, not
`(Key("first_name") == "John") | (Key("first_name") == "Bill")`

> Examples
```python
Key("state").eq("Texas") | Key("city").eq("New York")

(Key("gender") == "male") & (Key("age") >= 18) & (Key("selective_service") == False)

Key('creation_time.$parse_timestamp.$attr("year")').lt(2005).or_(
    Key('creation_time.$parse_timestamp.$attr("year")').gt(2015)
).and_(
    Key("product_id") == 15
)
# (year < 2005 OR year > 2015) AND product_id == 15
```

## <a name="formatter">Formatter</a>
> `Formatter` allows fields to be queried from an object and then formatted into a string. 
>Any JQL queries in a format string should be prefixed with `@`. For example, 
>`Formatter('Name: @name}').single({"name": "John Smith"})` results in
>`Name: John Smith`.

### `Formatter(spec, fallback="<missing>", convert_ints=True)`
 * `spec`: `str` The format string
 * `fallback`: `str` The value that will be used in the formatted string if a query could not be performed.
 For example, if the field `missing` does exist, then the query `"Age: @missing"` will result in `"Age: <missing>"`
 * `convert_ints`: `bool` Whether digit-only fields get treated as integers or strings
 
#### `.single(item)`
> Return a formatted string or the fallback value if the query fails

#### `.many(items)`
> Return a list of formatted strings or the fallback value.

### Notes
>The differences between `Query` and `Formatter` are:
 * `Query` can return a value of any type, `Formatter` just returns strings
 * `Formatter` supports multiple queries, end-to-end, `Query` does not
 * All queries must be prefixed with `@` with `Formatter`, not just when used as an argument like with `Query`
 * Both support all the features of `JQL`
 * `Query` actually can theoretically do everything `Formatter` does by using `$prefix`, `$suffix`, and `$string`. 
 For example, `'@name @age'` -> `'name.$suffix(" ").$suffix(@age)'`. However, the latter is much longer than the former.
 
Example (flattening operations):
```python
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
>The above example shows a powerful usage of flattening `errors` into its items,
>then joining each item; splitting the error name and message between lines, then
>joining all the errors together.

Example (nested replacement):
```python
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
>Additionally, the speed of formatting is very quick. The above statement 
>can be preformed 10,000 times in around 0.36 seconds.

## <a name="performance">Performance</a>
>There are several ways to increase the performance of querying, filtering, and formatting. The performance gains can be had
>by limiting the amount of times a query string has to be parsed. This means that using a `Query`,
>`Filter`, or `Formatter` object multiple times will be faster then creating a new object every time. 
>
>For example:
```python
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

>Across 10,000 runs:
 * reusing `Query` can improve performance by 302x
 * reusing `Filter` can improve performance by 132x
 * reusing `Formatter` can improve performance by 377x.

## <a name="changelog">Changelog</a>  
 * `1.1.2`
    * Minor changes to documentation
    * Mostly just to get version back on track with repository 
    
 * `1.1.1`
   * Add `antlr4-python3` requirement to `setup.py` so that installation will get the needed dependencies
   * Change `JQL` so that field and special names must only contain `[-a-zA-Z0-9_]`. `$index` can be used to get fields
   with prohibited characters. The change was to support more formatting use-cases, like `Age: @age, DOB: @dob`, which 
   previously would have failed because the `,` would have been considered part of the field name.
   * Change `Formatter` so that `fallback` is just a string that is substituted for invalid queries, instead of being
   the entire return value. Previously, `"Age: @missing"` would result in `None`, not it results in `"Age: <missing>"`.
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
   * Add `===` and `!==` to match the strict equality checking needed in the JS version. 
   The methods `seq` and `sne` have been added to `Key` to correspond with the new filters.
   `===` is the same as `==` and `!==` in the same as `!=` in the Python version.
   * Rename `null` -> `!present` and `!null` -> `present`. Corresponding methods have been renamed
   to `not_present` and `present`. This filter will catch values that are `null` or `undefined`.
   * Make membership filters (`in`, `contains`, `!in` and `!contains`) work properly with 
   strings, lists, dicts, and sets.
   * Remove `$datetime`. See below for replacement.
   * Add `$call` and `$attr` for calling a function and accessing an attribute. Can be used to replace
   `$datetime` functionality.
   * Remove `Formatter.format` and add `Formatter.single` and `Formatter.many` to be consistent across
   other classes and support formatting arrays of items.
   * Add more tests to increase coverage and do basic performance testing
   
 * `1.0.5`
   * Query strings can now start with specials to allow operations on the entire
   object being passed.
   * Bug fixes and more unit tests
   
 * `1.0.4`
   * Added new specials, mostly relating to time
     * `$parse_timestamp`
     * `$datetime`
     * `$strptime`
     * `$strftime`
   * Added `not` filtering and the `interval` and `!interval` operators
   * Made `Filter` consistent with `Query` by removing `.filter()` and adding
   `.single()` and `.many()`
   * Added `fallback` to `Getter`
   * added numerous unit tests
   
 * `1.0.3`
   * Rename `Getter.get` to `Getter.single`
   * Add `Getter.many`
   * Support getting multiple fields at once by changing `Getter` to allow
   `Getter(<field>)` and `Getter([<field>, <field>, ...])`
   * Change `Filter`'s before for when there are no filters. Now, by default,
   all items will be returned unless `Filter(..., empty_filters_response=False)`