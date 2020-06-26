import unittest
import sys
import json
import datetime
from io import StringIO
from pathlib import Path
from ezdict import EZDict
from random import randint
from contextlib import redirect_stdout

sys.path.append("../")

from jtools import Query, SpecialNotFoundError

folder = Path(__file__).parent
with open(folder / "data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open(folder / "data/20.json", "r") as file:
    small_data = json.loads(file.read())


class TestGetter(unittest.TestCase):
    def test_single_field_single(self):
        self.assertEqual(
            small_data[0]["guid"],
            Query("guid").single(small_data[0])
        )

    def test_capital_single(self):
        data = {"outer": {"INNER": "test"}}
        self.assertEqual(
            data["outer"]["INNER"],
            Query("outer.INNER").single(data)
        )

    def test_fallback_single_field_single(self):
        self.assertEqual(
            "MISSING",
            Query("null", fallback="MISSING").single(small_data[0])
        )

    def test_fallback_single_field_many(self):
        self.assertEqual(
            ["MISSING"]*3,
            Query("null", fallback="MISSING").many(small_data[:3])
        )

    def test_fallback_multiple_fields_single(self):
        self.assertEqual(
            ["MISSING", "MISSING"],
            Query(["null", "missing"], fallback="MISSING").single(small_data[0])
        )

    def test_fallback_multiple_fields_many(self):
        self.assertEqual(
            [["MISSING", "MISSING"] for _ in range(3)],
            Query(["null", "missing"], fallback="MISSING").many(small_data[:3])
        )

    def test_fallback_multiple_fields_some_missing_single(self):
        self.assertEqual(
            ["MISSING", small_data[2]["balance"]],
            Query(["isactive", "balance"], fallback="MISSING").single(small_data[2])
        )

    def test_fallback_multiple_fields_some_missing_many(self):
        self.assertEqual(
            [["MISSING", i["balance"]] for i in small_data[:3]],
            Query(["isactive", "balance"], fallback="MISSING").many(small_data[:3])
        )

    def test_fallback_single_field_single_nested_single(self):
        self.assertEqual(
            "MISSING",
            Query("null.null", fallback="MISSING").single(small_data[0])
        )

    def test_fallback_single_field_single_nested_single_number(self):
        self.assertEqual(
            "MISSING",
            Query("null.3", fallback="MISSING").single({"null": [0, 1]})
        )

    def test_fallback_single_field_single_nested_many(self):
        self.assertEqual(
            ["MISSING"]*3,
            Query("null.null", fallback="MISSING").many(small_data[:3])
        )

    def test_single_field_many(self):
        self.assertEqual(
            [i["age"] for i in small_data[:3]],
            Query("age").many(small_data[:3])
        )

    def test_multiple_fields_single(self):
        self.assertEqual(
            [small_data[1]["name"], small_data[1]["email"]],
            Query(["name", "email"]).single(small_data[1])
        )

    def test_multiple_fields_many(self):
        self.assertEqual(
            [[i["eyeColor"], i["gender"]] for i in small_data[1:3]],
            Query(["eyeColor", "gender"]).many(small_data[1:3])
        )

    def test_starting_with_special_keys(self):
        self.assertEqual(
            len(small_data[0]),
            Query("$keys.$length").single(small_data[0])
        )

    def test_stating_with_special_then_field(self):
        self.assertEqual(
            small_data[0]["_id"],
            Query("$values.0").single(small_data[0])
        )

    def test_list_map(self):
        self.assertEqual(
            small_data[0]["friends"][0]["name"],
            Query("friends.0.name").single(small_data[0])
        )

    def test_split_replace_convert(self):
        self.assertEqual(
            float(small_data[0]["balance"].split("$")[1].replace(",", "")),
            Query('balance.$split("$").1.$replace(",", "").$float').single(small_data[0])
        )

    def test_range_replace_convert(self):
        self.assertEqual(
            float(small_data[0]["balance"][1:].replace(",", "")),
            Query('balance.$range(1).$replace(",", "").$float').single(small_data[0])
        )

    def test_math_args(self):
        data = EZDict({"a": 4, "b": -4, "c": 2.5, "d": [3, 4], "e": 0, "pi": 3.1415926})
        self.assertEqual(data.a / (data.b + data.c) - data.pi, Query("$inject(@a / (@b + @c) - @pi)").single(data))
        self.assertEqual(data.a + data.b * data.c ** data.e, Query("$inject(@a + @b * @c ** @e)").single(data))
        self.assertEqual((data.a + data.b) * data.c ** data.e, Query("$inject((@a + @b) * @c ** @e)").single(data))

    # GENERAL
    def test_special_length_string(self):
        self.assertEqual(
            len(small_data[0]["_id"]),
            Query("_id.$length").single(small_data[0])
        )

    def test_special_length_array(self):
        self.assertEqual(
            len(small_data[0]["friends"]),
            Query("friends.$length").single(small_data[0])
        )

    def test_special_length_map(self):
        self.assertEqual(
            len(small_data[0]["favoriteFruit"]),
            Query("favoriteFruit.$length").single(small_data[0])
        )

    def test_special_lookup(self):
        data = {
            "a": "query",
            "b": "filter"
        }
        self.assertEqual(
            data["a"],
            Query(f"field.$lookup({json.dumps(data)})").single({"field": "a"})
        )
        self.assertEqual(
            "missing",
            Query(f'field.$lookup({json.dumps(data)}, "missing")').single({"field": "c"})
        )

    def test_print(self):
        buffer = StringIO()
        with redirect_stdout(buffer):
            Query("$inject('message').$print").single({})

        self.assertEqual("message", buffer.getvalue().strip())

    def test_keyword_args(self):
        data = small_data[0]
        self.assertEqual(data["balance"], Query("$index('balance')").single(data))
        self.assertEqual(None, Query("$index('nope')").single(data))
        self.assertEqual('nope', Query("$index('nope', 'nope')").single(data))
        self.assertEqual('nope', Query("$index('nope', fallback='nope')").single(data))
        self.assertEqual(data["tags"][0], Query("$index('tags.0', extended=true, fallback='nope')").single(data))
        # Do again to check caching
        self.assertEqual(data["tags"][0], Query("$index('tags.0', extended=true, fallback='nope')").single(data))

    # DICT
    def test_special_keys(self):
        self.assertEqual(
            list(small_data[0]["favoriteFruit"].keys()),
            Query("favoriteFruit.$keys").single(small_data[0])
        )

    def test_special_values(self):
        self.assertEqual(
            list(small_data[1]["favoriteFruit"].values()),
            Query("favoriteFruit.$values").single(small_data[1])
        )

    def test_special_items(self):
        self.assertEqual(
            list(small_data[2]["favoriteFruit"].items()),
            Query("favoriteFruit.$items").single(small_data[2])
        )

    def test_special_wildcard(self):
        data = {
            "a": {"key": 8, "other": 8},
            "b": {"key": 4},
            "c": {"value": 5},
            "d": 0,
            "e": "daf",
            "f": None,
            "g": ["john", "susan", "carl"],
            "h": True
        }

        self.assertEqual(
            [data["a"]["key"], data["b"]["key"]],
            Query('$wildcard("key")').single(data)
        )
        self.assertEqual(
            [data["a"], data["b"]],
            Query('$wildcard("key", false)').single(data)
        )

        self.assertEqual(
            [data["e"][0], data["g"][0]],
            Query('$wildcard(0)').single(data)
        )
        self.assertEqual(
            [data["e"], data["g"]],
            Query('$wildcard(0, false)').single(data)
        )

    def test_key_of(self):
        data = {randint(0, 100): i for i in range(10)}
        min_, max_ = None, None
        for k, v in data.items():
            if min_ is None:
                min_ = k
            elif data[k] < data[min_]:
                min_ = k

            if max_ is None:
                max_ = k
            elif data[k] > data[max_]:
                max_ = k

        self.assertEqual(max_, Query("$key_of_max_value").single(data))
        self.assertEqual((max_, data[max_]), Query("$key_of_max_value(just_key=false)").single(data))
        self.assertEqual(min_, Query("$key_of_min_value").single(data))
        self.assertEqual((min_, data[min_]), Query("$key_of_min_value(just_key=false)").single(data))

    # TYPE CONVERSIONS
    def test_special_fallback(self):
        self.assertEqual(
            "NOT ACTIVE",
            Query('isActive.$fallback("NOT ACTIVE")').single(small_data[0])
        )

    def test_special_ternary_false(self):
        self.assertEqual(
            "FALSE",
            Query('isActive.$ternary("TRUE", "FALSE")').single(small_data[0])
        )

    def test_special_ternary_true(self):
        self.assertEqual(
            "TRUE",
            Query('isActive.$not.$ternary("TRUE", "FALSE")').single(small_data[0])
        )

    def test_special_ternary_true_strict(self):
        self.assertEqual(
            "FALSE",
            Query('index.$ternary("TRUE", "FALSE", true)').single(small_data[1])
        )

    def test_special_ternary_true_not_strict(self):
        self.assertEqual(
            "TRUE",
            Query('index.$ternary("TRUE", "FALSE", false)').single(small_data[1])
        )

    def test_special_parse_timestamp(self):
        self.assertEqual(
            datetime.datetime(year=2020, month=1, day=25, hour=16, minute=14, second=53),
            Query("t.$parse_timestamp").single({"t": 1579968893})
        )

    def test_special_parse_timestamp_fractional_seconds(self):
        self.assertEqual(
            datetime.datetime(year=2020, month=1, day=25, hour=15, minute=51, second=58, microsecond=232609),
            Query("t.$parse_timestamp").single({"t": 1579967518.2326086})
        )

    def test_special_parse_timestamp_twice(self):
        t = 1579968893
        self.assertEqual(
            t,
            Query("t.$parse_timestamp.$timestamp.$parse_timestamp.$timestamp").single({"t": t})
        )

    def test_special_strptime_default_date(self):
        self.assertEqual(
            datetime.datetime(year=1978, month=4, day=3),
            Query("dt.$strptime").single({"dt": "4/3/1978"})
        )

    def test_special_strptime_default_time(self):
        self.assertEqual(
            datetime.datetime(year=1978, month=4, day=3, hour=17, minute=25),
            Query("dt.$strptime").single({"dt": "4/3/1978 5:25 PM"})
        )

    def test_special_strptime_custom(self):
        self.assertEqual(
            datetime.datetime(year=2020, month=8, day=6),
            Query('dt.$strptime("%d%Y%m")').single({"dt": "06202008"})
        )

    def test_special_timestamp(self):
        self.assertEqual(
            260472300.0,
            Query("dt.$strptime.$timestamp").single({"dt": "4/3/1978 5:25 PM"})
        )

    def test_special_strftime_default(self):
        self.assertEqual(
            "1978-04-03T17:25:00Z",
            Query("dt.$strptime.$strftime").single({"dt": "4/3/1978 5:25 PM"})
        )

    def test_special_strftime_custom(self):
        self.assertEqual(
            "05:25 PM on April 03, 1978",
            Query('dt.$strptime.$strftime("%I:%M %p on %B %d, %Y")').single({"dt": "4/3/1978 5:25 PM"})
        )

    def test_time_part(self):
        dt = "2020-05-23T10:11:12.123+00:00"
        self.assertEqual(2020, Query("$strptime.$time_part('year')").single(dt))
        self.assertEqual(5, Query("$strptime.$time_part('month')").single(dt))
        self.assertEqual(23, Query("$strptime.$time_part('day')").single(dt))
        self.assertEqual(10, Query("$strptime.$time_part('hour')").single(dt))
        self.assertEqual(11, Query("$strptime.$time_part('minute')").single(dt))
        self.assertEqual(12, Query("$strptime.$time_part('second')").single(dt))
        self.assertEqual(123, Query("$strptime.$time_part('millisecond')").single(dt))
        self.assertEqual(5, Query("$strptime.$time_part('dayOfWeek')").single(dt))
        self.assertEqual(144, Query("$strptime.$time_part('dayOfYear')").single(dt))

    def test_special_arithmetic(self):
        data = {"a": 4, "b": -4, "c": 2.5, "d": [3, 4], "e": 0, "pi": 3.1415926}
        self.assertEqual(6, Query("a.$add(2)").single(data))
        self.assertEqual(0, Query("b.$add(4)").single(data))
        self.assertEqual(5.0, Query("c.$subtract(-2.5)").single(data))
        self.assertEqual(16, Query("a.$multiply(4)").single(data))
        self.assertEqual(-2.0, Query("b.$divide(2)").single(data))
        self.assertEqual(16.0, Query("a.$pow(2)").single(data))
        self.assertEqual(16.0, Query("b.$pow(2)").single(data))
        self.assertEqual(5.0, Query("d.$distance([0, 0])").single(data))
        self.assertEqual(1.0, Query('e.$math("cos")').single(data))
        self.assertEqual(3.14, Query('pi.$round').single(data))
        self.assertEqual(3.1416, Query('pi.$round(4)').single(data))

    def test_arith_basic(self):
        data = EZDict({"a": 4, "b": -4, "c": 2.5, "d": [3, 4], "e": 0, "pi": 3.1415926})
        self.assertEqual(data.a + data.b + data.c, Query("a.$arith('+', @b + @c)").single(data))
        self.assertEqual(data.a + data.b - data.c, Query("a.$arith('+', @b - @c)").single(data))
        self.assertEqual(data.a + data.b * data.c, Query("a.$arith('+', @b * @c)").single(data))
        self.assertEqual(data.a + data.b / data.c, Query("a.$arith('+', @b / @c)").single(data))
        self.assertEqual(data.a + data.b ** data.c, Query("a.$arith('+', @b ** @c)").single(data))
        self.assertEqual(data.a + data.b // data.c, Query("a.$arith('+', @b // @c)").single(data))
        self.assertEqual(data.a + data.b % data.c, Query("a.$arith('+', @b % @c)").single(data))

    def test_min_max(self):
        data = [randint(0, 100) for _ in range(100)]
        self.assertEqual(min(data), Query("$min").single(data))
        self.assertEqual(max(data), Query("$max").single(data))

    def test_special_string(self):
        self.assertEqual(
            f"Age: {small_data[0]['age']}",
            Query('age.$prefix("Age: ")').single(small_data[0])
        )
        self.assertEqual(
            f"{len(small_data[0]['tags'])} tags found",
            Query('tags.$length.$suffix(" tags found")').single(small_data[0])
        )
        self.assertEqual(
            "Name: John Smith M.D.",
            Query('name.$wrap("Name: ", " M.D.")').single({"name": "John Smith"})
        )

        self.assertEqual("test", Query("a.$strip").single({"a": "     test            "}))
        self.assertEqual(
            small_data[10]["balance"].replace(",", ""),
            Query('balance.$replace(",", "")').single(small_data[10])
        )
        self.assertEqual(
            small_data[0]["about"][:47] + "...",
            Query("about.$trim").single(small_data[0])
        )
        self.assertEqual(
            small_data[0]["about"][:25],
            Query('about.$trim(25, "")').single(small_data[0])
        )
        self.assertEqual(
            small_data[0]["guid"].split("-"),
            Query('guid.$split("-")').single(small_data[0])
        )

    def test_string_cases(self):
        item = "here IS sOmEtHiNg"
        self.assertEqual(item.upper(), Query("$uppercase").single(item))
        self.assertEqual(item.lower(), Query("$lowercase").single(item))
        self.assertEqual(item.title(), Query("$titlecase").single(item))

    def test_special_list(self):
        data = {
            "a": [43.2, -34, 54.2],
            "b": [3, None, 1, 0, False]
        }
        self.assertEqual(sum(data["a"]), Query("a.$sum").single(data))
        self.assertEqual(", ".join(str(i) for i in data["a"]), Query("a.$join").single(data))
        self.assertEqual(", ".join(str(i) for i in data["a"]), Query("$join_arg(@a)").single(data))
        self.assertEqual(data["a"][2], Query("a.$index(2)").single(data))
        self.assertEqual("nope", Query("a.$index(5, fallback='nope')").single(data))
        self.assertEqual(data["a"][1:], Query("a.$range(1)").single(data))
        self.assertEqual(data["a"][1:-1], Query("a.$range(1, -1)").single(data))
        self.assertEqual([d for d in data["b"] if d is not None], Query("b.$remove_nulls").single(data))

    def test_value_map(self):
        data = {"a": [1, 2, 3], "b": [1, 2], "c": [3, 5, 3], "d": [1, 2, 5, 3, 4]}
        self.assertEqual(
            [len(i) for i in data.values()],
            Query("$value_map('length').$values").single(data)
        )

    def test_special_map(self):
        self.assertEqual(
            "\n".join([f"{i['id']}: {i['name']}" for i in small_data[0]["friends"]]),
            Query('friends.$map("values").$map("join", ": ").$join("\n")').single(small_data[0])
        )

    def test_register_special(self):
        self.assertTrue(Query.register_special("cube", lambda value, *, context: value ** 3))
        self.assertEqual(8, Query("a.$cube").single({"a": 2}))
        self.assertFalse(Query.register_special("cube", lambda value, *, context: value ** 3))

    def test_complex_argument(self):
        self.assertEqual(
            5, Query("a.$distance([0, 0])").single({"a": [3, 4]})
        )

    def test_no_convert_ints(self):
        self.assertEqual(5, Query("data.2").single({"data": [0, 1, 5]}))
        self.assertIsNone(Query("data.2", convert_ints=False).single({"data": [0, 1, 5]}))
        self.assertEqual(5, Query("data.2", convert_ints=False).single({"data": {"2": 5}}))

    def test_nested_query(self):
        params = {
            "index": "name",
            "origin": [0, 0],
            "name": small_data[0]["name"],
            "company": small_data[0]["company"],
            "lookup": {
                small_data[0]["name"]: small_data[0]["company"],
            }
        }
        self.assertEqual(
            [e["name"] for e in small_data[0]["friends"]],
            Query("data.friends.$map('index', @params.index)").single({"data": small_data[0], "params": params})
        )

        lat = small_data[0]["latitude"]
        lon = small_data[0]["longitude"]
        self.assertEqual(
            round(sum([(params["origin"][0] - lat)**2, (params["origin"][1] - lon)**2]) ** 0.5, 2),
            Query("params.origin.$distance([@data.latitude, @data.longitude]).$round").single(
                {"data": small_data[0], "params": params}
            )
        )

        self.assertEqual(
            params["lookup"][small_data[0]["name"]],
            Query("data.name.$lookup(@params.lookup)").single({"data": small_data[0], "params": params})
        )

        self.assertEqual(
            params["lookup"][small_data[0]["name"]],
            Query("data.name.$lookup({@params.name: @params.company})").single(
                {"data": small_data[0], "params": params}
            )
        )

        self.assertEqual(
            f"Lat={small_data[0]['latitude']} & Lon={small_data[0]['longitude']}",
            Query('latitude.$wrap("Lat=", @longitude.$prefix(" & Lon="))').single(small_data[0])
        )

    def test_triple_nested(self):
        data = {
            "data": "test",

            "keys": {
                "key1": "data"
            },

            "key1": "key1"
        }

        self.assertEqual(
            data["data"],
            Query("$index(@keys.$index(@key1))").single(data)
        )

    def test_argument_types_with_inject(self):
        self.assertEqual(3.14, Query("$inject(3.14)").single({}))
        self.assertEqual(type(3.14), type(Query("$inject(3.14)").single({})))
        self.assertEqual(3, Query("$inject(3)").single({}))
        self.assertEqual(type(3), type(Query("$inject(3)").single({})))

        self.assertEqual("test", Query("$inject('test')").single({}))
        self.assertEqual("test", Query('$inject("test")').single({}))

        self.assertTrue(Query('$inject( true )').single({}))
        self.assertFalse(Query('$inject(false)').single({}))
        self.assertIsNone(Query('$inject(null)').single({}))

        self.assertEqual([1, 2], Query("$inject([ 1,  2 ])").single({}))
        self.assertEqual([], Query("$inject([ ])").single({}))
        self.assertEqual({1, 2}, Query("$inject({1, 2})").single({}))
        self.assertEqual(set(), Query("$inject({  })").single({}))
        self.assertEqual({1: 4, '5': False}, Query("$inject({ 1 : 4, '5' : false })").single({}))
        self.assertEqual({}, Query("$inject({:})").single({}))

        value = "missing"
        self.assertEqual(value, Query("$inject(@value)").single({"value": value}))

    def test_valid_names(self):
        keys = ["_", "-", "23", "123asdf", "bill_1234_asdf-24234"]
        value = [1, 2]
        for key in keys:
            self.assertEqual(value, Query(key, convert_ints=False).single({key: value}))

    def test_empty_query(self):
        data = {"bill": 54}
        self.assertEqual(data, Query("").single(data))

    def test_missing_fields(self):
        self.assertEqual(None, Query("a").single({"b": [1, 2]}))
        self.assertEqual(None, Query("b.3").single({"b": [1, 2]}))
        self.assertEqual('MISSING', Query("b.3", fallback="MISSING").single({"b": [1, 2]}))
        self.assertEqual(2, Query("b.2.$fallback(4).$divide(2)").single({"b": [1, 2]}))
        self.assertEqual(3, Query("b.1.$fallback(4).$divide(2)").single({"b": [1, 6]}))

    def test_store_as_int(self):
        raw = {"value": 5}
        self.assertEqual(
            raw["value"], Query("value.$store_as('temp').$inject(@temp)").single(raw)
        )

    def test_store_as_dict(self):
        store = {'field': 'value'}
        self.assertEqual(
            store, Query("$inject({'field': 'value'}).$store_as('temp').$inject(@temp)").single({})
        )

    def test_store_as_with_later_use(self):
        d = small_data[0]
        self.assertEqual(
            f"{d['name']} is {d['age']} and has 5 messages",
            Query(
                "greeting.$split('You have ').1.$split(' unread').0.$int.$store_as('unread')" +
                ".$join_arg([@name, 'is', @age, 'and has', @unread, 'messages'], ' ')"
            ).single(small_data[0])
        )

    def test_group_by_flat(self):
        l = [i % 3 for i in range(12)]
        ez = EZDict()
        for item in l:
            ez.appender(item, item)

        self.assertEqual(ez, Query("$group_by").single(l))

    def test_group_by_number(self):
        data = [[i, i] for i in range(10)]
        ez = EZDict()
        for item in data:
            ez.appender(item[0], item)

        self.assertEqual(
            ez,
            Query("$group_by(0)").single(data)
        )

    def test_group_by_nested(self):
        ez = EZDict()
        for item in small_data:
            ez.appender(round(EZDict(item).favoriteFruit.apple, 1), item)

        self.assertEqual(ez, Query("$group_by('favoriteFruit.apple.$round(1)')").single(small_data))

    def test_group_by_nested_count(self):
        ez = EZDict()
        for item in small_data:
            ez.incrementer(round(EZDict(item).favoriteFruit.apple, 1))

        self.assertEqual(ez, Query("$group_by('favoriteFruit.apple.$round(1)', true)").single(small_data))

    def test_sort_flat(self):
        items = [randint(0, 100) for i in range(10)]
        self.assertEqual(sorted(items), Query("$sort").single(items))

    def test_sort_number(self):
        data = {randint(0, 100): i for i in range(10)}
        self.assertEqual(
            sorted(data.items(), key=lambda x: x[0]),
            Query("$sort(0)").single(list(data.items()))
        )

    def test_sort_age(self):
        self.assertEqual(
            sorted(small_data, key=lambda x: x["age"]),
            Query("$sort('age')").single(small_data)
        )

    def test_sort_nested(self):
        self.assertEqual(
            sorted(small_data, key=lambda x: EZDict(x).favoriteFruit.banana * -0.5),
            Query("$sort('favoriteFruit.banana.$multiply(-0.5)')").single(small_data)
        )

    def test_sort_nested_reverse(self):
        self.assertEqual(
            sorted(small_data, key=lambda x: EZDict(x).favoriteFruit.banana * -0.5, reverse=True),
            Query("$sort('favoriteFruit.banana.$multiply(-0.5)', true)").single(small_data)
        )

    def test_special_not_found_error(self):
        self.assertRaises(
            SpecialNotFoundError,
            lambda: Query("age.$mixedup").single(small_data[0])
        )

    def test_dict(self):
        self.assertEqual(
            small_data[0]["favoriteFruit"],
            Query("favoriteFruit.$items.$dict").single(small_data[0])
        )

    def test_context(self):
        self.assertEqual(
            5,
            Query("context").single({}, {"context": 5})
        )

        self.assertEqual(
            5,
            Query("context.nested").single({}, {"context": {"nested": 5}})
        )

        self.assertEqual(
            5,
            Query("overlapping").single({"overlapping": 5}, {"overlapping": "nope"})
        )

    def test_pipeline(self):
        min_ = min([float(item["balance"][1:].replace(",", "")) for item in small_data])
        self.assertEqual(
            min_,
            Query("""
                $map(
                    'pipeline',
                    [
                        ['index', 'balance'],
                        ['range', 1],
                        ['replace', {'old': ',', 'new': ''}],
                        ['float']
                    ]
                ).$min
            """).single(small_data)
        )

    def test_bad_query(self):
        result = Query("$length(4*5").single({})
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
