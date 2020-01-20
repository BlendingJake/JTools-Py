 # JTools
>JTools is a robust library for interacting with JSON-like objects.
>Specifically, JTools focuses on providing an easy way to filter, 
>format, and extract fields from JSON-like data.

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

## <a name="getter">Getter</a>
>`Getter` one the surface is very simple: you give it a field path
>and it returns the value at that path from a given an idea. Example:
>`Getter("name").get({"name": "John", ...})` will return `"John"`.
>Here is an overview of some of the cools features:

 * Dot-notation is supported and can be used to access nested values. For
 example. `meta.id` can be used to get the `id` field from 
 `{"meta": {"id": 1}}`. 
 * Integer paths can be used to index lists as long as `Getter(..., convert_ints=True)`
 which is set to `True` by default. This allows paths like `friends.0`.
 * Specials can be specified which can transform the value gotten so far. 
 Specials are included in the field path and prefixed with `$`. For example, 
 if you have `{"long_number": 3.1415926}`, you can use `long_number.$round`
 to round it to `2` decimal places, returning `3.14`. 
 * Arguments can be passed into these specials! For example, 
 `{"email": "john_doe@gmail.com"}` and you just can to get the 
 email provider, then `email.$split("@").$index(-1)` can be used, which will
 return `gmail.com`. These specials take the value from the previous part of
 the field path, and uses it in the next transformation. Equally, 
 `email.$split("@").1` could be used. Arguments can be anything that can be
 represented in JSON. Note: JSON requires strings to have double-quotes, so 
 `email.$split('@')` would not work.
 * You don't have to use `()` at the end of a special if there aren't any 
 arguments, or the default arguments are acceptable.
 * More specials can be added! Use the class attribute `register_special` 
 like so: `Getter.register_special(<name>, <func>)`. The function should take
 at least one argument, which is the value from the previous parts.
 
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
  * `$fallback(fallback) -> value or fallback`: If the value 
  is None, then it will be replaced with `fallback`
  * `$timestamp(fmt="%Y-%m-%dT%H:%M:%SZ") -> str`: Take a Unix
  timestamp in seconds and return the value with the specified time format.
  
Math / Numbers
  * `$add(num) -> Union[int, float]`
  * `$subtract(num) -> Union[int, float]`
  * `$multiply(num) -> Union[int, float]`
  * `$divide(num) -> float`
  * `$pow(num) -> Union[int, float]`
  * `$abs(num) -> Union[int, float]`
  * `$distance(other) -> float`: Euler distance in N-dimensions
  * `$math(attr) -> Any`: Returns `math.<attr>(value)`, can be used for
  operations like `floor`, `cos`, `sin`, etc.
  * `$round(n=2) -> float`
  
Strings
  * `$prefix(prefix) -> str`: Prefix the value with the specified string
  * `$suffix(suffix) -> str`: Concatenate a string to the end of the value
  * `$strip -> str`: Strip leading an trailing whitespace
  * `$replace(old, new) -> str`: Replace all occurrences of a string 
  * `$trim(length=50, suffix="...") -> str`: Trim the length of a string
  * `$split(on=" ") -> List[str]`: Split a string
  
Lists
  * `$sum -> Union[float, int]`
  * `$join(sep=", ") -> str`: Join a list using the specified separator
  * `$index(index) -> Any`: Index a list. Negative indices are allowed.
  * `$range(start, end=None) -> `: Get a sublist. Defaults to `[start:]`, 
  but an end value can be specified. Negative indices are allowed. 
  * `$map(special, *args) -> list`: Apply `special` to every element in the 
  value. Arguments can be passed through to the special being used.
  
## <a name="formatter">Formatter</a>
> `Formatter` allows fields to be taken from an object and then formatted
>into a string. The basic usage is `Formatter(<spec>).format(<item>)`.
>Fields to be replaced should be wrapped in `{{}}` and the
>field options listed above for `Getter` are all valid. For example, 
>`Formatter('Name: {{name}}').format({"name": "John Smith"})` results in
>`Name: John Smith`. 

 * The field specification from `Getter` is valid here, so the above example
 could instead be `'First Name: {name.$split(" ").0}'` to get `First Name: John`
 instead.
 * **Field paths can be nested!!!!**
 * Whitespace is allowed inside of the curly braces before and after the field query string. 
 `{{   a  }}` is just as valid as `{{a}}`. 
 
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
>then joining each item, splitting the error name and message between lines, then
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

**IMPORTANT:** Nested fields that return strings which are then used as arguments 
must be manually double-quoted. For example, lets say we want to replace the domain `gmail`
with `<domain>` in `item = {"email": "john_doe@gmail.com"}`. We want to determine the 
current domain, which we can do with `email.$split("@").1.$split(".").0`, and then
we want to pass that as an argument into `$replace`. To do so, we need surround the nested
field with double-quotes so it will be properly recognized as an argument in the replace special.
`Formatter('Generic Email: {{  email.$replace("{{  email.$split("@").1.$split(".").0  }}", "<domain>")  }}').format(item)"`

## <a name="filter">Filter</a>
>`Filter` takes the field extraction capabilities of `Getter` and combines them with 
>filtering conditions to allow lists of objects to be filtered down to just items of 
>interest. The basic usage is: `Filter(<filters>).filter(<list of items>)`.
>The filters can be manually built, or the `Key` and `Condition` classes can 
>be used to simplify your code.

Filter Schema:
```
[
    {"field": <field>, "operator": <op>, "value": <value>},

    OR

    {"or": <nested outer structure>}
]
<field>: anything Getter accepts
<op>: See below list
<value>: Anything that makes sense for the operator
``` 

> Note on `or`:
>`{"or": [ [{...filter1...}, {...filter2...} ], {...filter3...} ]}` is the same
>as `(filter1 AND filter2) OR filter3`. Nesting in an `or` will cause those filters
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
>Intended to simplify having to write `{"field": <field>, ...}` a lot. The
>basic usage is: `Key(<field>).<op>(<value>)` or for certain or the first six 
>operators, the actual operators can be used, so `Key(<field>) <op> <value>`.
>For example: `Key("meta.id").eq(12)` is the same as `Key("meta.id") == 12`,
>which is the same as `{"field": "meta.id", "operator": "==", "value": 12}`.

Operators: 

| underlying operator | function | operator |
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
>`and` and `or`. They can be manually accessed (`and_()`, `or_()`), 
>or the overloaded operators `&` and `|` can be used, respectively.

**Caution: `&` and `|` bind tighter than the comparisons operators**
`Key("first_name") == "John" | Key("first_name") == "Bill"` is actually
`(Key("first_name") == ("John" | Key("first_name"))) == "Bill"`, not
`(Key("first_name") == "John") | (Key("first_name") == "Bill")`