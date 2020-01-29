 # JTools
>JTools is a robust library for interacting with JSON-like objects,
>focusing on providing an easy way to filter, 
>format, and extract fields from JSON-like data.

## Changelog
 * `1.0.3`
   * Rename `Getter.get` to `Getter.single`
   * Add `Getter.many`
   * Support getting multiple fields at once by changing `Getter` to allow
   `Getter(<field>)` and `Getter([<field>, <field>, ...])`
   * Change `Filter`'s before for when there are no filters. Now, by default,
   all items will be returned unless `Filter(..., empty_filters_response=False)`

## Glossary
 * [`Installation`](#install)
 * [`Getter`](#getter)
   * [`Specials`](#specials)
 * [`Formatter`](#formatter)
 * [`Filter`](#filter)
   * [`Key`](#key)
   * [`Condition`](#condition)
   
## <a name="install">Installation</a>
`pip install jtools`
```python
# import
from jtools import Getter, Filter, Key, Condition, Formatter
```

## <a name="getter">Getter</a>
>`Getter` one the surface is very simple: you give it a field query string (or several)
>and it returns the value (or values) at that path(s) from a given an item or list of items. 
>Example: `Getter("name").single({"name": "John"})` will return `"John"`.
>However, there are many more cool features, like supporting dot-notation,
>having the ability to transform values with specials, and even the ability 
>to drill down into lists. Below is a fuller list of the features.

 * `.single(item)` can be used to get field(s) from a single item, or 
 `.many(items)` can be used to get field(s) from a list of items
 * Multiple fields can be gotten at once by passing a list of query strings.
 `Getter(["name", "age"])`. Resulting values from `.single` and `.many` will be
 lists of corresponding length
 * Dot-notation is supported and can be used to access nested values. For
 example, `meta.id` can be used to get the `id` field from the item
 `{"meta": {"id": 1}}`, resulting in the value of `1`. 
 * Integer paths can be used to index lists as long as `Getter(..., convert_ints=True)`,
 which is set to `True` by default. This allows paths like `friends.0`.
 * Specials can be can be used to transform the queried valued, and multiple
 specials can be used back to back, with the output of one being used in the next. 
 Specials are included in the field path and prefixed with `$`. For example, 
 if you have `{"long_number": 3.1415926}`, you can use `long_number.$round`
 to round it to `2` decimal places, returning `3.14`. 
 * Arguments can be passed into these specials! For example, if you have
 `{"email": "john_doe@gmail.com"}` and you want to get just the 
 email provider, then `email.$split("@").$index(-1)` can be used, which will
 return `gmail.com`. Equally, `email.$split("@").1` could be used. 
 Arguments can be anything that can be represented in JSON. 
 **Note: JSON requires strings to be double-quoted, so 
 `email.$split('@')` would not work and `email.$split("@")` would have to be used instead.**
 * You don't have to use `()` at the end of a special if there aren't any 
 arguments, or the default arguments are acceptable.
 * More specials can be added! Use the class attribute `.register_special()` 
 like so: `Getter.register_special(<name>, <func>)`. The function should take
 at least one argument, which is the current value in the query string.
 
#### <a name="specials">Specials</a>
General
  * `$length -> int`
  
Maps
  * `$keys -> list`
  * `$values -> list`
  * `$items -> List[tuple]`
  
Type Conversions
  * `$set -> set`
  * `$float -> float`
  * `$string -> str`
  * `$int -> int`
  * `$not -> bool`: Returns `!value`
  * `$fallback(fallback) -> value or fallback`: If the value is None, then it will be replaced with `fallback`.
  * `$ternary(if_true, if_false, strict=False) -> Any`: Return `if_true` if the value is `truish`, otherwise,
  return `if_false`. Pass `True` for `strict` if the value must be `True` and not just `truish`.
  
Datetime 
  * `$parse_timestamp -> datetime`: Take a Unix timestamp in seconds and return a corresponding datetime object
  * `$datetime(attr) -> int`: Get a specific attribute of a datetime object. For example. `'dt.$parse_timestamp.$datetime("year")'`
  The options are
    * year
    * month
    * day
    * hour
    * minute
    * second
    * microsecond
  * `$strptime(fmt=None) -> datetime`: Parse a datetime string and return a corresponding datetime object.
  If `fmt=None`, then common formats will be tried. Refer to 
  https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior for formatting instructions
  * `$timestamp -> float`: Dump a datetime object to a UTC timestamp as a float
  * `$strftime(fmt="%Y-%m-%dT%H:%M:%SZ":) -> str`: Format a datetime object as a string using `fmt`.
  Refer to https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior for formatting instructions
  
Math / Numbers
  * `$add(num) -> Union[int, float]`
  * `$subtract(num) -> Union[int, float]`
  * `$multiply(num) -> Union[int, float]`
  * `$divide(num) -> float`
  * `$pow(num) -> Union[int, float]`
  * `$abs(num) -> Union[int, float]`
  * `$distance(other) -> float`: Euler distance in N-dimensions
  * `$math(attr) -> Any`: Returns `math.<attr>(value)`, which can be used for
  operations like `floor`, `cos`, `sin`, etc.
  * `$round(n=2) -> float`
  
Strings
  * `$prefix(prefix) -> str`: Prefix the value with the specified string
  * `$suffix(suffix) -> str`: Concatenate a string to the end of the value
  * `$strip -> str`: Strip leading and trailing whitespace
  * `$replace(old, new) -> str`: Replace all occurrences of a string 
  * `$trim(length=50, suffix="...") -> str`: Trim the length of a string
  * `$split(on=" ") -> List[str]`: Split a string
  
Lists
  * `$sum -> Union[float, int]`: Return the sum of the items in the value
  * `$join(sep=", ") -> str`: Join a list using the specified separator
  * `$index(index) -> Any`: Index a list. Negative indices are allowed.
  * `$range(start, end=None) -> `: Get a sublist. Defaults to `value[start:]`, 
  but an end value can be specified. Negative indices are allowed. 
  * `$map(special, *args) -> list`: Apply `special` to every element in the 
  value. Arguments can be passed through to the special being used.
  
## <a name="formatter">Formatter</a>
> `Formatter` allows fields to be taken from an object and then formatted
>into a string. The basic usage is `Formatter(<spec>).format(<item>)`.
>Fields to be replaced should be wrapped in `{{}}` and any valid
>field query string for `Getter` can be used. For example, 
>`Formatter('Name: {{name}}').format({"name": "John Smith"})` results in
>`Name: John Smith`. Below are some specific details.

 * The field specifications from `Getter` are valid here, so the above example
 could instead be `'First Name: [{name.$split(" ").0]}'` to get `First Name: John`
 instead.
 * **Field paths can be nested!!!!** - this allows values from one field to be 
 passed as the arguments in another, complex queries to be made and formatted. For example,
 `Formatter("Balance: ${{balance.$subtract({{pending_charges}})}}").format({"balance": 1000, "pending_charges": 250})`
 which results in `Balance: $750`.
 * Whitespace is allowed inside of the curly braces before and after the field query string. 
 `{{   a  }}` is just as valid as `{{a}}`. 
 * **IMPORTANT:** Nested fields that return strings which are then used as arguments 
must be manually double-quoted. For example, lets say we want to replace the domain `gmail`
with `<domain>` in `item = {"email": "john_doe@gmail.com"}`. We want to determine the 
current domain, which we can do with `email.$split("@").1.$split(".").0`, and then
we want to pass that as an argument into `$replace`. To do so, we need to surround the nested
field with double-quotes so it will be properly recognized as an argument in the `replace` special.
`Formatter('Generic Email: {{  email.$replace("{{  email.$split("@").1.$split(".").0  }}", "<domain>")  }}').format(item)"`
 
Example (flattening operations):
```python
errors = {
    "errors": {
        "Process Error": "Could not communicate with the subprocess",
        "Connection Error": "Could not connect with the database instance"
    }
}

Formatter('{errors.$items.$map("join", ": \\n\\t").$join("\\n")}').format(errors)
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
    "Midpoint: [{{x2.$subtract({{x1}}).$divide(2)}}, {y2.$subtract({{y1}}).$divide(2)}}]"
)
# Midpoint: [5.5, 26.5]
```
>Additionally, the speed of formatting is very quick. The above statement 
>can be preformed 10,000 times in around 0.75 seconds.

## <a name="filter">Filter</a>
>`Filter` takes the field querying capabilities of `Getter` and combines them with 
>filtering conditions to allow lists of items to be filtered down to just those of 
>interest. The basic usage is: `Filter(<filters>).filter(<list of items>)`.
>The filters can be manually built, or the `Key` and `Condition` classes can 
>be used to simplify your code.

Filter Schema:
```
[
    {"field": <field>, "operator": <op>, "value": <value>},

    OR

    {"or": <nested outer structure>},

    ...
]
<field>: anything Getter accepts
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
 * `in`: `<field> in <value>`
 * `!in`
 * `contains`: `<value> in <field>`
 * `!contains`
 * `startswith`
 * `endswith`
 * `null`
 * `!null`

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
| `in` | `in_` | N/A | 
| `!in` | `nin` | N/A | 
| `contains` | `contains` | N/A | 
| `!contains` | `not_contains` | N/A | 
| `startswith` | `startswith` | N/A | 
| `endswith` | `endswith` | N/A | 
| `null` | `none` | N/A | 
| `!null` | `not_none` | N/A | 

#### <a name="condition">Condition</a>
>Intended to be used in combination with `Key` to make creating filters
>easier than manually creating the `JSON`. There are two conditions supported:
>`and` and `or`. They can be manually accessed via `and_()`, `or_()`, 
>or the overloaded operators `&` and `|` can be used, respectively.

**Caution: `&` and `|` bind tighter than the comparisons operators**
`Key("first_name") == "John" | Key("first_name") == "Bill"` is actually
`(Key("first_name") == ("John" | Key("first_name"))) == "Bill"`, not
`(Key("first_name") == "John") | (Key("first_name") == "Bill")`