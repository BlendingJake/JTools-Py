import unittest
import sys
import json

# sys.path.append("../jtools")

from jtools import __version__, Formatter, Filter, Key, Condition, Getter

with open("./data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open("./data/20.json", "r") as file:
    small_data = json.loads(file.read())


class TestGetterBasic(unittest.TestCase):
    def test_list_map(self):
        self.assertEqual(
            Getter("friends.0.name").get(small_data[0]),
            "Webster Green"
        )

    def test_split_replace_convert(self):
        self.assertEqual(
            Getter('balance.$split("$").1.$replace(",", "").$float').get(small_data[0]),
            3247.13
        )

    def test_range_replace_convert(self):
        self.assertEqual(
            Getter('balance.$range(1).$replace(",", "").$float').get(small_data[0]),
            3247.13
        )


class TestFormatterBasic(unittest.TestCase):
    def test_nested_number(self):
        self.assertEqual(
            Formatter("Balance: ${{balance.$subtract({{pending_charges}})}}").format(
                {"balance": 1000, "pending_charges": 250}),
            "Balance: $750"
        )


class TestFilterBasic(unittest.TestCase):
    def test_nested(self):
        items = Filter(Key("friends.0.name") == "Webster Green").filter(small_data)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["_id"], "5e2797c05aa0585816ce8b8c")

    def test_eye_color(self):
        items = Filter(Key("eyeColor").eq("brown")).filter(small_data)
        self.assertEqual(len(items), 6)

    def test_split_convert(self):
        items = Filter(Key('balance.$range(1).$replace(",", "").$float') > 3800).filter(small_data)
        not_items = Filter(Key('balance.$range(1).$replace(",", "").$float') < 3800).filter(small_data)
        self.assertEqual(len(items), 2)
        self.assertEqual(len(not_items), 18)

    def test_nested_map(self):
        items = Filter(Key("favoriteFruit.strawberry") == 0.4242).filter(small_data)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["_id"], "5e2797c0efc296e33c198e4c")

    def test_or(self):
        items = Filter(Key("address").contains("Texas") | Key("address").contains("West Virginia")).filter(small_data)
        self.assertEqual(len(items), 2)

    def test_or_and(self):
        items = Filter(
            Key("address").contains("Texas").or_(Key("address").contains("West Virginia")).and_(
                Key("company") == "XYLAR"
            )).filter(small_data)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["_id"], "5e2797c05aa0585816ce8b8c")


if __name__ == "__main__":
    print(f"Using version {__version__}")

    unittest.main()
