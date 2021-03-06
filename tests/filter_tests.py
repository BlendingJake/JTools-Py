import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from jtools import Filter, Key, Condition, __version__

folder = Path(__file__).parent
with open(folder / "data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open(folder / "data/20.json", "r") as file:
    small_data = json.loads(file.read())


class TestFilter(unittest.TestCase):
    def test_missing_fields(self):
        self.assertFalse(Filter(Key("missing") == "John", missing_field_response=False).single(small_data[0]))
        self.assertTrue(Filter(Key("missing") == "John", missing_field_response=True).single(small_data[0]))

        data = [
            {"a": 5},
            {"b": 4},
            {"a": 4},
            {"a": 2}
        ]
        self.assertEqual(
            2,
            len(Filter(Key("a") >= 4).many(data))
        )

        self.assertEqual(
            3,
            len(Filter(Key("a") >= 4, missing_field_response=True).many(data))
        )

    def test_nested(self):
        items = Filter(Key("friends.0.name") == "Webster Green").many(small_data)
        items1 = Filter(Key("friends.0.name").operator("==").value("Webster Green")).many(small_data)
        self.assertEqual(1, len(items))
        self.assertEqual(1, len(items1))
        self.assertEqual("5e2797c05aa0585816ce8b8c", items[0]["_id"])
        self.assertEqual("5e2797c05aa0585816ce8b8c", items1[0]["_id"])

    def test_eye_color(self):
        items = Filter(Key("eyeColor").eq("brown")).many(small_data)
        self.assertEqual(6, len(items))

    def test_split_convert(self):
        items = Filter(Key('balance.$range(1).$replace(",", "").$float') > 3800).many(small_data)
        not_items = Filter(Key('balance.$range(1).$replace(",", "").$float') < 3800).many(small_data)
        self.assertEqual(2, len(items))
        self.assertEqual(18, len(not_items))

    def test_nested_map(self):
        items = Filter(Key("favoriteFruit.strawberry") == 0.4242).many(small_data)
        self.assertEqual(1, len(items))
        self.assertEqual("5e2797c0efc296e33c198e4c", items[0]["_id"])

    def test_or(self):
        items = Filter(Key("address").contains("Texas") | Key("address").contains("West Virginia")).many(small_data)
        self.assertEqual(2, len(items))

    def test_or_and(self):
        items = Filter(
            Key("address").contains("Texas").or_(Key("address").contains("West Virginia")).and_(
                Key("company") == "XYLAR"
            )).many(small_data)
        items2 = Filter([
            {"or": [
                {"field": "address", "operator": "contains", "value": "Texas"},
                {"field": "address", "operator": "contains", "value": "West Virginia"}
            ]},
            [{"field": "company", "operator": "==", "value": "XYLAR"}]
        ]).many(small_data)

        self.assertEqual(1, len(items))
        self.assertEqual(len(items), len(items2))
        self.assertEqual("5e2797c05aa0585816ce8b8c", items[0]["_id"])
        self.assertEqual("5e2797c05aa0585816ce8b8c", items2[0]["_id"])

    def test_basic_not(self):
        items = Filter(~Key("company").eq("XYLAR")).many(small_data)
        items2 = Filter(Key("company").eq("XYLAR").not_()).many(small_data)
        self.assertEqual(len(small_data) - 1, len(items))
        self.assertEqual(len(items), len(items2))

    def test_not_or(self):
        items = Filter(
            ~(Key("address").contains("Texas").or_(Key("address").contains("West Virginia")))
        ).many(small_data)
        self.assertEqual(len(small_data) - 2, len(items))

    def test_multiple_specials_datetime(self):
        items = Filter(Key('registered.$strptime.$strftime("%Y").$int') >= 2017).many(small_data)
        items2 = Filter(Key('registered.$split("-").0.$int').gt(2017)).many(small_data)
        items3 = Filter(Key('registered.$strptime.$attr("year")').gte(2016)).many(small_data)

        self.assertEqual(9, len(items))
        self.assertEqual(6, len(items2))
        self.assertEqual(13, len(items3))

    def test_interval(self):
        key = Key('registered.$strptime.$attr("year")')
        items = Filter(key.interval([2016, 2017])).many(small_data)
        items2 = Filter(
            (key >= 2016) & (key.lte(2017))
        ).many(small_data)

        self.assertEqual(7, len(items))
        self.assertEqual(len(items), len(items2))

    def test_not_interval(self):
        key = Key('registered.$strptime.$attr("year")')
        items = Filter(key.not_interval([2016, 2017])).many(small_data)
        items2 = Filter(
            (key.lt(2016)) | (key > 2017)
        ).many(small_data)

        self.assertEqual(13, len(items))
        self.assertEqual(len(items), len(items2))

    def test_membership_set(self):
        data = {
            "set": {1, 2, 3},
            "value": 5
        }

        self.assertTrue(Filter(Key("set").contains(2)).single(data))
        self.assertFalse(Filter(Key("set").contains(5)).single(data))

        self.assertTrue(Filter(Key("set").not_contains(5)).single(data))
        self.assertFalse(Filter(Key("set").not_contains(2)).single(data))

        self.assertTrue(Filter(Key("value").in_({5, 6, 7})).single(data))
        self.assertFalse(Filter(Key("value").in_({6, 7})).single(data))

        self.assertFalse(Filter(Key("value").nin({5, 6, 7})).single(data))
        self.assertTrue(Filter(Key("value").nin({6, 7})).single(data))

    def test_membership_list(self):
        data = {
            "list": [1, 2, 3],
            "value": 5
        }

        self.assertTrue(Filter(Key("list").contains(2)).single(data))
        self.assertFalse(Filter(Key("list").contains(5)).single(data))

        self.assertTrue(Filter(Key("list").not_contains(5)).single(data))
        self.assertFalse(Filter(Key("list").not_contains(2)).single(data))

        self.assertTrue(Filter(Key("value").in_([5, 6, 7])).single(data))
        self.assertFalse(Filter(Key("value").in_([6, 7])).single(data))

        self.assertFalse(Filter(Key("value").nin([5, 6, 7])).single(data))
        self.assertTrue(Filter(Key("value").nin([6, 7])).single(data))

    def test_membership_dict(self):
        data = {
            "dict": {1: "1", 2: "2", 3: "3"},
            "value": 5
        }

        self.assertTrue(Filter(Key("dict").contains(2)).single(data))
        self.assertFalse(Filter(Key("dict").contains(5)).single(data))

        self.assertTrue(Filter(Key("dict").not_contains(5)).single(data))
        self.assertFalse(Filter(Key("dict").not_contains(2)).single(data))

        self.assertTrue(Filter(Key("value").in_({5: "5", 6: "6", 7: "7"})).single(data))
        self.assertFalse(Filter(Key("value").in_({6: "6", 7: "7"})).single(data))

        self.assertFalse(Filter(Key("value").nin({5: "5", 6: "6", 7: "7"})).single(data))
        self.assertTrue(Filter(Key("value").nin({6: "6", 7: "7"})).single(data))

    def test_membership_str(self):
        data = {
            "str": "123",
            "value": "5"
        }

        self.assertTrue(Filter(Key("str").contains("2")).single(data))
        self.assertFalse(Filter(Key("str").contains("5")).single(data))

        self.assertTrue(Filter(Key("str").not_contains("5")).single(data))
        self.assertFalse(Filter(Key("str").not_contains("2")).single(data))

        self.assertTrue(Filter(Key("value").in_("5, 6, 7")).single(data))
        self.assertFalse(Filter(Key("value").in_("6, 7")).single(data))

        self.assertFalse(Filter(Key("value").nin("5, 6, 7")).single(data))
        self.assertTrue(Filter(Key("value").nin("6, 7")).single(data))

    def test_subset(self):
        item = {
            'a': [1, 'test', True, None, 3.45]
        }
        self.assertTrue(Filter(Key('a').subset({1, True, None, 3.45, 'test', 'missing'})).single(item))
        self.assertTrue(Filter(Key('a').subset({1, True, None, 3.45, 'test'})).single(item))
        self.assertFalse(Filter(Key('a').subset({1, True, None, 3.45})).single(item))

    def test_not_subset(self):
        item = {
            'a': [1, 'test', True, None, 3.45]
        }
        self.assertTrue(Filter(Key('a').not_subset({1, True, None, 3.45})).single(item))
        self.assertTrue(Filter(Key('a').not_subset([])).single(item))
        self.assertFalse(Filter(Key('a').not_subset({1, True, None, 3.45, 'test', 'missing'})).single(item))

    def test_superset(self):
        item = {
            'a': [1, 'test', True, None, 3.45]
        }
        self.assertTrue(Filter(Key('a').superset([1, None])).single(item))
        self.assertTrue(Filter(Key('a').superset([])).single(item))

        self.assertFalse(Filter(Key('a').superset([1, 3.45, False])).single(item))
        self.assertFalse(Filter(Key('a').superset(['missing'])).single(item))

    def test_not_superset(self):
        item = {
            'a': [1, 'test', True, None, 3.45]
        }
        self.assertFalse(
            Filter([{'field': 'a', 'operator': '!superset', 'value': [1, True]}]).single(item)
        )
        self.assertTrue(
            Filter(Key('a').not_superset([1, True, 'bill'])).single(item)
        )
        self.assertFalse(
            Filter([{'field': 'a', 'operator': '!superset', 'value': []}]).single(item)
        )

    def test_starts_and_endswith(self):
        self.assertTrue(
            Filter([{"field": "name", "operator": "endswith", "value": "Weiss"}]).single(small_data[2])
        )
        self.assertTrue(
            Filter(Key("name").endswith("Weiss")).single(small_data[2])
        )
        self.assertTrue(
            Filter(Key("name").startswith("Dotson")).single(small_data[2])
        )

    def test_present(self):
        self.assertTrue(
            Filter(Key("name").present()).single(small_data[0])
        )
        self.assertFalse(
            Filter(Key("name2").present()).single(small_data[0])
        )

        self.assertTrue(
            Filter(Key("not_present").not_present()).single(small_data[0])
        )
        self.assertFalse(
            Filter(Key("name").not_present()).single(small_data[0])
        )

    def test_equality(self):
        self.assertEqual(1, len(Filter(Key("company") == "XYLAR").many(small_data)))
        self.assertEqual(1, len(Filter(Key("company").eq("XYLAR")).many(small_data)))
        self.assertEqual(1, len(Filter(Key("company").seq("XYLAR")).many(small_data)))

        self.assertEqual(19, len(Filter(Key("company") != "XYLAR").many(small_data)))
        self.assertEqual(19, len(Filter(Key("company").ne("XYLAR")).many(small_data)))
        self.assertEqual(19, len(Filter(Key("company").sne("XYLAR")).many(small_data)))

    def test_filter_by_index(self):
        self.assertEqual(
            small_data[5:7],
            Filter(Condition.ander(
                Key("INDEX") >= 5, Key("INDEX") < 7
            )).many(small_data)
        )

        self.assertEqual(
            small_data[1:6],
            Filter(Key("INDEX").interval(1, 5)).many(small_data)
        )

    def test_filter_by_index_with_context(self):
        self.assertEqual(
            [small_data[3]],
            Filter(
                Key("INDEX").eq(3) & Key("age.$arith('//', @a)").eq(small_data[3]["age"] // 2)
            ).many(small_data, {"a": 2})
        )

    def test_filter_traversal(self):
        filters = [
            {"field": "blah", "operator": "===", "value": "blah"},
            {"field": "blah2", "operator": "===", "value": "blah2"},
            {"field": "blah3", "operator": "===", "value": "blah3"},
            {"field": "blah4", "operator": "===", "value": "blah4"},
            {"field": "blah5", "operator": "===", "value": "blah5"}
        ]

        condition = Condition.from_list([
            {"or": filters[:2]},
            {"not": [filters[2]]},
            {"not": [{"or": filters[3:]}]}
        ])

        for index, filter_ in enumerate(filters):
            self.assertEqual(filter_, filters[index])

        condition.traverse(lambda f: self.assertEqual(filters.pop(0), f))

    def test_filter_shortcutting(self):
        self.assertFalse(
            Filter(Key("not").present() & Key("not.available").eq(4)).single(small_data[0])
        )
        self.assertTrue(
            Filter(Key("gender").eq("male") | Key("not.available").eq(4)).single(small_data[0])
        )

    def test_filter_fallback(self):
        self.assertTrue(
            Filter(Key("not.available.$fallback(1)").eq(1)).single(small_data[0])
        )

    def test_first(self):
        first_female = None
        for item in small_data:
            if item["gender"] == "female":
                first_female = item
                break

        self.assertEqual(first_female, Filter(Key("gender") == "female").first(small_data))
        self.assertIsNone(Filter(Key("gender") == "not_found").first(small_data))

    def test_last(self):
        last_female = None
        for item in reversed(small_data):
            if item["gender"] == "female":
                last_female = item
                break

        self.assertEqual(last_female, Filter(Key("gender") == "female").last(small_data))

    def test_large_filter(self):
        cond = Condition.orer(
            Condition.ander(Key("age") == 34, Key("name") == "Chang Pollard", Key("isActive").is_true()),
            Condition.ander(Key("isActive").is_false(), Key("email").startswith("woodard")),
            Condition.ander(Key("friends.$length") == 7, Key("friends.0.name") == "Katrina Crane"),
            Condition.ander(Key("name") == "Castro Wood", Key("age") == -10)
        )

        self.assertEqual(
            [small_data[i] for i in [1, 3, 8]],
            Filter(cond).many(small_data)
        )

    def test_is_null(self):
        items = [
            {"a": None},
            {"a": False},
            {"a": None},
            {"a": 4}
        ]

        self.assertEqual(
            [items[0], items[2]],
            Filter(Key("a").is_null()).many(items)
        )

    def test_deep_clone(self):
        cond = Condition.orer(
            Condition.ander(Key("age") == 34, Key("name") == "Chang Pollard", Key("isActive").is_true()),
            Condition.ander(Key("isActive").is_false(), Key("email").startswith("woodard")),
            Condition.ander(Key("friends.$length") == 7, Key("friends.0.name") == "Katrina Crane"),
            ~Condition.ander(Key("name") == "Castro Wood", Key("age") == -10)
        )
        cond2 = cond.clone(True)
        self.assertEqual(cond, cond2)
        cond.output[0]["or"][0][0]["value"] = "test"
        self.assertNotEqual(cond, cond2)

    def test_filter_value_query_loc(self):
        items = []
        for i in small_data:
            if i['latitude'] < i['longitude']:
                items.append(i)

        self.assertEqual(
            items, Filter(Key("latitude") < Key("longitude")).many(small_data)
        )

    def test_filter_value_query_fruit(self):
        items = []
        for i in small_data:
            if i['favoriteFruit']['strawberry'] * 5 >= i['favoriteFruit']['cherry'] / 2:
                items.append(i)

        self.assertEqual(
            items,
            Filter(Key('favoriteFruit.strawberry.$multiply(5)') >= Key('favoriteFruit.cherry.$divide(2)')).many(small_data)
        )

    def test_filter_value_query_advanced(self):
        items = []
        for i in small_data:
            if len(i['friends']) == int(i['greeting'].split(' unread')[0].split('have ')[1]):
                items.append(i)

        self.assertEqual(
            items,
            Filter(Key('friends.$length') == Key('greeting.$split(" unread").0.$split("have ").1.$int')).many(small_data)
        )

        self.assertEqual(
            items,
            Filter(
                Key('friends.$length').operator('==').value(
                    Key('greeting.$split(" unread").0.$split("have ").1.$int')
                )).many(small_data)
        )

    def test_register_filter(self):
        self.assertTrue(Filter.register_filter('isMultiple', lambda field, value: field % value == 0))
        self.assertTrue(Filter(Key('').operator('isMultiple').value(3)).single(27))
        self.assertFalse(Filter(Key('').operator('isMultiple').value(3)).single(28))
        self.assertFalse(Filter.register_filter('isMultiple', lambda field, value: False))


if __name__ == "__main__":
    print(__version__)
    unittest.main()
