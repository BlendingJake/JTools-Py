import unittest
import sys
import json

sys.path.append("../")

from jtools import Formatter

with open("./data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open("./data/20.json", "r") as file:
    small_data = json.loads(file.read())


class TestFormatter(unittest.TestCase):
    def test_nested_number(self):
        self.assertEqual(
            "Balance: $750",
            Formatter("Balance: ${{balance.$subtract({{pending_charges}})}}").format(
                {"balance": 1000, "pending_charges": 250}),
        )

    def test_multiple(self):
        self.assertEqual(
            f"{small_data[0]['name']} {small_data[0]['gender']}",
            Formatter("{{name}} {{gender}}").format(small_data[0])
        )

    def test_join(self):
        self.assertEqual(
            f"Tags: [{'], ['.join(small_data[0]['tags'])}]",
            Formatter('Tags: [{{tags.$join("], [")}}]').format(small_data[0])
        )


if __name__ == "__main__":
    unittest.main()
