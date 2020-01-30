import unittest
import sys
import json

sys.path.append("../")

from jtools import Filter, Key

with open("./data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open("./data/20.json", "r") as file:
    small_data = json.loads(file.read())


# TODO: test multiple ands and ors together
# TODO: test interval and !interval
class TestFilter(unittest.TestCase):
    def test_nested(self):
        items = Filter(Key("friends.0.name") == "Webster Green").filter(small_data)
        self.assertEqual(1, len(items))
        self.assertEqual("5e2797c05aa0585816ce8b8c", items[0]["_id"])

    def test_eye_color(self):
        items = Filter(Key("eyeColor").eq("brown")).filter(small_data)
        self.assertEqual(6, len(items))

    def test_split_convert(self):
        items = Filter(Key('balance.$range(1).$replace(",", "").$float') > 3800).filter(small_data)
        not_items = Filter(Key('balance.$range(1).$replace(",", "").$float') < 3800).filter(small_data)
        self.assertEqual(2, len(items))
        self.assertEqual(18, len(not_items))

    def test_nested_map(self):
        items = Filter(Key("favoriteFruit.strawberry") == 0.4242).filter(small_data)
        self.assertEqual(1, len(items))
        self.assertEqual("5e2797c0efc296e33c198e4c", items[0]["_id"])

    def test_or(self):
        items = Filter(Key("address").contains("Texas") | Key("address").contains("West Virginia")).filter(small_data)
        self.assertEqual(2, len(items))

    def test_or_and(self):
        items = Filter(
            Key("address").contains("Texas").or_(Key("address").contains("West Virginia")).and_(
                Key("company") == "XYLAR"
            )).filter(small_data)
        self.assertEqual(1, len(items))
        self.assertEqual("5e2797c05aa0585816ce8b8c", items[0]["_id"])

    def test_basic_not(self):
        items = Filter(~Key("company").eq("XYLAR")).filter(small_data)
        self.assertEqual(len(small_data) - 1, len(items))

    def test_not_or(self):
        items = Filter(
            ~(Key("address").contains("Texas").or_(Key("address").contains("West Virginia")))
        ).filter(small_data)
        self.assertEqual(len(small_data) - 2, len(items))

    def test_multiple_specials_datetime(self):
        items = Filter(Key('registered.$strptime.$strftime("%Y").$int') >= 2017).filter(small_data)
        items2 = Filter(Key('registered.$split("-").0.$int') > 2017).filter(small_data)
        items3 = Filter(Key('registered.$strptime.$datetime("year")') >= 2016).filter(small_data)

        self.assertEqual(9, len(items))
        self.assertEqual(6, len(items2))
        self.assertEqual(13, len(items3))


if __name__ == "__main__":
    unittest.main()
