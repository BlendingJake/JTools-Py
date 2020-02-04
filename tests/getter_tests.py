import unittest
import sys
import json
import datetime

sys.path.append("../")

from jtools import Getter

with open("./data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open("./data/20.json", "r") as file:
    small_data = json.loads(file.read())


class TestGetter(unittest.TestCase):
    def test_single_field_single(self):
        self.assertEqual(
            small_data[0]["guid"],
            Getter("guid").single(small_data[0])
        )

    def test_capital_single(self):
        data = {"outer": {"INNER": "test"}}
        self.assertEqual(
            data["outer"]["INNER"],
            Getter("outer.INNER").single(data)
        )

    def test_fallback_single_field_single(self):
        self.assertEqual(
            "MISSING",
            Getter("null", fallback="MISSING").single(small_data[0])
        )

    def test_fallback_single_field_many(self):
        self.assertEqual(
            ["MISSING"]*3,
            Getter("null", fallback="MISSING").many(small_data[:3])
        )

    def test_fallback_multiple_fields_single(self):
        self.assertEqual(
            ["MISSING", "MISSING"],
            Getter(["null", "missing"], fallback="MISSING").single(small_data[0])
        )

    def test_fallback_multiple_fields_many(self):
        self.assertEqual(
            [["MISSING", "MISSING"] for _ in range(3)],
            Getter(["null", "missing"], fallback="MISSING").many(small_data[:3])
        )

    def test_fallback_multiple_fields_some_missing_single(self):
        self.assertEqual(
            ["MISSING", small_data[2]["balance"]],
            Getter(["isactive", "balance"], fallback="MISSING").single(small_data[2])
        )

    def test_fallback_multiple_fields_some_missing_many(self):
        self.assertEqual(
            [["MISSING", i["balance"]] for i in small_data[:3]],
            Getter(["isactive", "balance"], fallback="MISSING").many(small_data[:3])
        )

    def test_fallback_single_field_single_nested_single(self):
        self.assertEqual(
            "MISSING",
            Getter("null.null", fallback="MISSING").single(small_data[0])
        )

    def test_fallback_single_field_single_nested_many(self):
        self.assertEqual(
            ["MISSING"]*3,
            Getter("null.null", fallback="MISSING").many(small_data[:3])
        )

    def test_single_field_many(self):
        self.assertEqual(
            [i["age"] for i in small_data[:3]],
            Getter("age").many(small_data[:3])
        )

    def test_multiple_fields_single(self):
        self.assertEqual(
            [small_data[1]["name"], small_data[1]["email"]],
            Getter(["name", "email"]).single(small_data[1])
        )

    def test_multiple_fields_many(self):
        self.assertEqual(
            [[i["eyeColor"], i["gender"]] for i in small_data[1:3]],
            Getter(["eyeColor", "gender"]).many(small_data[1:3])
        )

    def test_list_map(self):
        self.assertEqual(
            small_data[0]["friends"][0]["name"],
            Getter("friends.0.name").single(small_data[0])
        )

    def test_split_replace_convert(self):
        self.assertEqual(
            float(small_data[0]["balance"].split("$")[1].replace(",", "")),
            Getter('balance.$split("$").1.$replace(",", "").$float').single(small_data[0])
        )

    def test_range_replace_convert(self):
        self.assertEqual(
            float(small_data[0]["balance"][1:].replace(",", "")),
            Getter('balance.$range(1).$replace(",", "").$float').single(small_data[0])
        )

    # GENERAL
    def test_special_length_string(self):
        self.assertEqual(
            len(small_data[0]["_id"]),
            Getter("_id.$length").single(small_data[0])
        )

    def test_special_length_array(self):
        self.assertEqual(
            len(small_data[0]["friends"]),
            Getter("friends.$length").single(small_data[0])
        )

    def test_special_length_map(self):
        self.assertEqual(
            len(small_data[0]["favoriteFruit"]),
            Getter("favoriteFruit.$length").single(small_data[0])
        )

    # DICT
    def test_special_keys(self):
        self.assertEqual(
            list(small_data[0]["favoriteFruit"].keys()),
            Getter("favoriteFruit.$keys").single(small_data[0])
        )

    def test_special_values(self):
        self.assertEqual(
            list(small_data[1]["favoriteFruit"].values()),
            Getter("favoriteFruit.$values").single(small_data[1])
        )

    def test_special_items(self):
        self.assertEqual(
            list(small_data[2]["favoriteFruit"].items()),
            Getter("favoriteFruit.$items").single(small_data[2])
        )

    # TYPE CONVERSIONS
    def test_special_fallback(self):
        self.assertEqual(
            "NOT ACTIVE",
            Getter('isActive.$fallback("NOT ACTIVE")').single(small_data[0])
        )

    def test_special_ternary_false(self):
        self.assertEqual(
            "FALSE",
            Getter('isActive.$ternary("TRUE", "FALSE")').single(small_data[0])
        )

    def test_special_ternary_true(self):
        self.assertEqual(
            "TRUE",
            Getter('isActive.$not.$ternary("TRUE", "FALSE")').single(small_data[0])
        )

    def test_special_ternary_true_strict(self):
        self.assertEqual(
            "FALSE",
            Getter('index.$ternary("TRUE", "FALSE", true)').single(small_data[1])
        )

    def test_special_ternary_true_not_strict(self):
        self.assertEqual(
            "TRUE",
            Getter('index.$ternary("TRUE", "FALSE", false)').single(small_data[1])
        )

    def test_special_parse_timestamp(self):
        self.assertEqual(
            datetime.datetime(year=2020, month=1, day=25, hour=16, minute=14, second=53),
            Getter("t.$parse_timestamp").single({"t": 1579968893})
        )

    def test_special_parse_timestamp_fractional_seconds(self):
        self.assertEqual(
            datetime.datetime(year=2020, month=1, day=25, hour=15, minute=51, second=58, microsecond=232609),
            Getter("t.$parse_timestamp").single({"t": 1579967518.2326086})
        )

    def test_special_strptime_default_date(self):
        self.assertEqual(
            datetime.datetime(year=1978, month=4, day=3),
            Getter("dt.$strptime").single({"dt": "4/3/1978"})
        )

    def test_special_strptime_default_time(self):
        self.assertEqual(
            datetime.datetime(year=1978, month=4, day=3, hour=17, minute=25),
            Getter("dt.$strptime").single({"dt": "4/3/1978 5:25 PM"})
        )

    def test_special_timestamp(self):
        self.assertEqual(
            260472300.0,
            Getter("dt.$strptime.$timestamp").single({"dt": "4/3/1978 5:25 PM"})
        )

    def test_special_strftime_default(self):
        self.assertEqual(
            "1978-04-03T17:25:00Z",
            Getter("dt.$strptime.$strftime").single({"dt": "4/3/1978 5:25 PM"})
        )

    def test_special_strftime_custom(self):
        self.assertEqual(
            "05:25 PM on April 03, 1978",
            Getter('dt.$strptime.$strftime("%I:%M %p on %B %d, %Y")').single({"dt": "4/3/1978 5:25 PM"})
        )

    def test_special_arithmetic(self):
        data = {"a": 4, "b": -4, "c": 2.5, "d": [3, 4], "e": 0, "pi": 3.1415926}
        self.assertEqual(6, Getter("a.$add(2)").single(data))
        self.assertEqual(0, Getter("b.$add(4)").single(data))
        self.assertEqual(5.0, Getter("c.$subtract(-2.5)").single(data))
        self.assertEqual(16, Getter("a.$multiply(4)").single(data))
        self.assertEqual(-2.0, Getter("b.$divide(2)").single(data))
        self.assertEqual(16.0, Getter("a.$pow(2)").single(data))
        self.assertEqual(16.0, Getter("b.$pow(2)").single(data))
        self.assertEqual(5.0, Getter("d.$distance([0, 0])").single(data))
        self.assertEqual(1.0, Getter('e.$math("cos")').single(data))
        self.assertEqual(3.14, Getter('pi.$round').single(data))
        self.assertEqual(3.1416, Getter('pi.$round(4)').single(data))

    def test_special_string(self):
        self.assertEqual(
            f"Age: {small_data[0]['age']}",
            Getter('age.$prefix("Age: ")').single(small_data[0])
        )
        self.assertEqual(
            f"{len(small_data[0]['tags'])} tags found",
            Getter('tags.$length.$suffix(" tags found")').single(small_data[0])
        )
        self.assertEqual("test", Getter("a.$strip").single({"a": "     test            "}))
        self.assertEqual(
            small_data[10]["balance"].replace(",", ""),
            Getter('balance.$replace(",", "")').single(small_data[10])
        )
        self.assertEqual(
            small_data[0]["about"][:47] + "...",
            Getter("about.$trim").single(small_data[0])
        )
        self.assertEqual(
            small_data[0]["about"][:25],
            Getter('about.$trim(25, "")').single(small_data[0])
        )
        self.assertEqual(
            small_data[0]["guid"].split("-"),
            Getter('guid.$split("-")').single(small_data[0])
        )

    def test_special_list(self):
        data = {"a": [43.2, -34, 54.2]}
        self.assertEqual(sum(data["a"]), Getter("a.$sum").single(data))
        self.assertEqual(", ".join(str(i) for i in data["a"]), Getter("a.$join").single(data))
        self.assertEqual(data["a"][2], Getter("a.$index(2)").single(data))
        self.assertEqual(data["a"][1:], Getter("a.$range(1)").single(data))
        self.assertEqual(data["a"][1:-1], Getter("a.$range(1, -1)").single(data))

    def test_special_map(self):
        self.assertEqual(
            "\n".join([f"{i['id']}: {i['name']}" for i in small_data[0]["friends"]]),
            Getter('friends.$map("values").$map("join", ": ").$join("\\n")').single(small_data[0])
        )


if __name__ == "__main__":
    unittest.main()
