 # JTools
>JTools is a robust library for interacting with JSON-like objects,
>focusing on providing an easy way to filter, 
>format, and extract fields from JSON-like data.
>
>A companion to the JavaScript version of this package: @blending_jake/jtools (https://www.npmjs.com/package/@blending_jake/jtools).
>The JavaScript version supports almost the exact same specials, filters, and formatting specification, with the
>goal of making it a seamless experience to go from accessing/filtering/formatting in JavaScript to Python and back.
>The goal is to make the two versions work as identically as possible.

## Changelog
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
   * Added `$wildcard(next, just_value=True)` which allows all values of an item to be collected if they contain
   the specified field
   
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

## Glossary
 * [`Installation`](#install)
 * [`JQL`](#jql)
 * [`Query`](#query)
   * [`Specials`](#specials)
 * [`Formatter`](#formatter)
 * [`Filter`](#filter)
   * [`Key`](#key)
   * [`Condition`](#condition)
 * [`Performance`](#performance)
   
## <a name="install">Installation</a>
`pip install jtools`
```python
# import
from jtools import Query, Filter, Key, Condition, Formatter
```

## <a name="jql">`JQL`</a>
>`JQL` or the `JSON Query Language` is a custom built query language for `JTools` which supports powerful features
>like nesting, complex data types, and value transformers. The basic format of the language is: 
```
(<field> | $<special>) (. (<field> | $<special>))*
EX: 'data', 'data.timestamp', 'data.$split', '$split.0'
```
#### field
A field is just a value that can be used as an index, like a string or integer key for a map/dict or an integer for an
array. By default, all fields are treated as strings, but that behavior can be customized in each of the classes provided
so that integers can be using properly. Fields cannot contain ' ', '.', or '('. `$index(<field>)` can be used
to access fields with those prohibited characters. 

#### $special
A special is a function that is applied the value that has been queried so far. There is a complete list of specials
[here](#specials). These specials can be passed arguments, which is one of the most powerful features
of `JQL`. The syntax is similar to most programming languages: `$<special>(<value>(, <value>)*)`. Just to note, `$<special>()`
is valid, as is `$<special>`. Many of the specials don't require any arguments, or have default values.

##### value
An argument can be:
```
[] or [<value>(, <value>)*] - List
{} or {<value>(, <value>)*} - Set
{:} or {<key>: <value>(, <key>: <value>)*} - Map/Dict/Object
Integer
Float
String w/ '' or ""
true
false
null
@<query> - Yep! Nested queries!

<key>:
    @<query>
    String
    Integer/Float
    True
    False
    None/Null
``` 
As denoted, values and queries can be nested, so `[[1, 2], ["bob"], {"Ann", 'Ralph'}, {'key': 4, 23: 5}]`
is valid. Additionally, the support for nesting queries is extremely powerful and allows for queries like:
`item.tag.$lookup(@table.colors)`, which, for `{"item": {"tag": "product"}, "table": {"colors": {"product": "red"}}}`
results in `"red"`

## <a name="query">Query</a>
>`Query` on the surface is very simple: you give it a field query string (or several)
>and it returns the value (or values) that result for the query(ies). 
>Example: `Query("name").single({"name": "John"})` will return `"John"`.
>However, the power and flexibility of `JQL` allows for some very useful queries!

 * `.single(item)` can be used to get field(s) from a single item, or 
 `.many(items)` can be used to get field(s) from a list of items
 
 * Multiple fields can be retrieved at once by passing a list of query strings, like
 `Query(["name", "age"])`. Resulting values from `.single` and `.many` will be
 lists of the corresponding length.
 
 * If a field does not exist, then a fallback value will result. By default, this is `None`, but the value can
 be changed by setting `Query(..., fallback=None)`. 
 
 * Lists can be indexed as long as `Query(..., convert_ints=True)`,
 which is set to `True` by default. This allows paths like `friends.0`. However, `convert_ints=False`
 should be used if trying to access fields whose keys are strings containing digits, like
 `{"index": {"0": ...}}`. If it is unacceptable for all digit containing strings to be converted to
 integers, then the `.$index` special can be used.
 `Query("item.0.$index(0)").single({"item": {"0": ["tag"])}) -> 'tag'`
 
 * Fields can be indexed after specials, so `$split.0` is completely valid
 
 * You don't have to use `()` at the end of a special if there aren't any 
 arguments, or the default arguments are acceptable.
 
 * More specials can be added by using the class attribute `.register_special()` 
 like so: `Query.register_special(<name>, <func>)`. The function should take
 at least one argument, which is the current value in the query string: `lambda value, *args: ...`
 
#### <a name="specials">Specials</a>
General
  * `$length -> int`
  * `$lookup(map: dict, fallback=None) -> any`: Lookup the current value in the provided map/dict 
  * `$inject(value: any) -> any`: Inject a value into the query
  * `$print -> any`: Print the current query value before continuing to pass that value along
  
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
  * `$int -> int`
  * `$not -> bool`: Returns `!value`
  * `$fallback(fallback) -> value or fallback`: If the value is None, then it will be replaced with `fallback`.
  * `$ternary(if_true, if_false, strict=false) -> any`: Return `if_true` if the value is `truish`, otherwise,
  return `if_false`. Pass `true` for `strict` if the value must be `True` and not just `truish`.
  
Datetime 
  * `$parse_timestamp -> datetime`: Take a Unix timestamp in seconds and return a corresponding datetime object
  * `$strptime(fmt=None) -> datetime`: Parse a datetime string and return a corresponding datetime object.
  If `fmt=None`, then common formats will be tried. Refer to 
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
  * `$wrap(prefix, suffix) -> str`: Wrap a string with a prefix and suffix. Combines features of above to specials.
  * `$strip -> str`: Strip leading and trailing whitespace
  * `$replace(old, new) -> str`: Replace all occurrences of a string 
  * `$trim(length=50, suffix="...") -> str`: Trim the length of a string
  * `$split(on=" ") -> List[str]`: Split a string
  
Lists
  * `$sum -> Union[float, int]`: Return the sum of the items in the value
  * `$join(sep=", ") -> str`: Join a list using the specified separator
  * `$index(index) -> any`: Index a list. Negative indices are allowed.
  * `$range(start, end=None) -> `: Get a sublist. Defaults to `value[start:]`, 
  but an end value can be specified. Negative indices are allowed.
    * `$remove_nulls -> List[any]`: Remove any values that are `None`
  * `$map(special, *args) -> list`: Apply `special` to every element in the 
  value. Arguments can be passed through to the special being used.
  
Attributes
  * `$call(func, *args) -> any`: Call a function that is on the current value, implemented as `getattr(value, func)(*args)`
  * `$attr(attr) -> any`: Access an attribute of the given object, implemented as `getattr(value, attr)`
  
## <a name="formatter">Formatter</a>
> `Formatter` allows fields to be taken from an object and then formatted
>into a string. The basic usage is `Formatter(<spec>).single(<item>)`, although
>`.many` exists as well.
>Any queries in a format string should be prefixed with `@` and any valid `JQL` query can be used. For example, 
>`Formatter('Name: @name}').format({"name": "John Smith"})` results in
>`Name: John Smith`.
>The differences between `Query` and `Formatter` are:
 * `Query` can return a value of any type, `Formatter` just returns strings
 * `Formatter` supports multiple queries, end-to-end, `Query` does not
 * All queries must be prefixed with `@` with `Formatter`, not just when used as an argument like with `Query`
 * Both support all the features of `JQL`
 
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

## <a name="filter">Filter</a>
>`Filter` takes the power of `JQL` and combines it with 
>filtering conditions to allow lists of items to be filtered down to just those of 
>interest. The basic usage is: `Filter(<filters>).many(<list of items>)`, although
>`.single` can also be used to get a boolean answer of whether an item matches the filter or not.
>The filters can be manually built, or the `Key` and `Condition` classes can 
>be used to simplify your code.

Filter Schema:
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

> Note on `or`:
```
{"or": [ 
    [ {filter1}, {filter2} ], 
    {filter3} 
]}
``` 
>is the same as `(filter1 AND filter2) OR filter3`. Nesting in an `or` will cause those filters
>to be `AND'd` and then everything in the toplevel of that `or` will be `OR'd`.

Operators:
 * `>`
 * `<`
 * `>=`
 * `<=`
 * `==`
 * `!=`
 * `===`: same as `==`
 * `!==`: same as `!=`
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
>or the overloaded operators `&`, `|`, and `~` can be used, respectively.

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

## <a name="performance">Performance</a>
>There are several ways to increase the performance of filtering and getting. The query strings within filters
>or those being passed directly to a `Query` are parsed when the object is created. This means that using a `Query`
>or `Filter` object multiple times will be faster then creating a new object every time. 
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

>Specifically, reusing a `Query` can improve performance by 7-8x and reusing a `Filter` can improve
>by 5-6x.