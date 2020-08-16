import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from jtools import Formatter, __version__

folder = Path(__file__).parent
with open(folder / "data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open(folder / "data/20.json", "r") as file:
    small_data = json.loads(file.read())


class TestFormatter(unittest.TestCase):
    def test_nested_capital_prefix(self):
        data = {"env": {"VERSION": "1.0.0"}}
        prefix = "build/"
        self.assertEqual(
            prefix + data["env"]["VERSION"],
            Formatter(prefix+"@env.VERSION").single(data)
        )

    def test_nested_capital(self):
        data = {"env": {"VERSION": "1.0.0"}}
        self.assertEqual(
            data["env"]["VERSION"],
            Formatter("@env.VERSION").single(data)
        )

    def test_format_missing(self):
        self.assertEqual(
            "<missing>",
            Formatter("@missing").single({})
        )

    def test_format_missing_nested(self):
        self.assertEqual(
            "N/A",
            Formatter("@found.missing", "N/A").single({"found": {}})
        )

    def test_format_missing_nested_field(self):
        self.assertEqual(
            "<missing>",
            Formatter("@a.$index(@index, '<missing>')").single({"a": [1, 2]})
        )

    def test_nested_fallback(self):
        self.assertEqual("5", Formatter("@missing.something.$fallback(5)").single({}))

    def test_nested_number(self):
        self.assertEqual(
            "Balance: $750",
            Formatter("Balance: $@balance.$subtract(@pending_charges)").single(
                {"balance": 1000, "pending_charges": 250}),
        )

    def test_multiple(self):
        self.assertEqual(
            f"{small_data[0]['name']} {small_data[0]['gender']}",
            Formatter("@name @gender").single(small_data[0])
        )

    def test_join(self):
        self.assertEqual(
            f"Tags: [{'], ['.join(small_data[0]['tags'])}]",
            Formatter('Tags: [@tags.$join("], [")]').single(small_data[0])
        )

    def test_complex_field_as_argument(self):
        self.assertEqual(
            "5.0", Formatter("@a.$distance(@b)").single({"a": [1, 1], "b": [4, 5]})
        )

    def test_many(self):
        self.assertEqual(
            [f"Name: {item['name']}" for item in small_data[:3]],
            Formatter("Name: @name").many(small_data[:3])
        )

    def test_at_at(self):
        self.assertEqual(
            f"<redacted>@{small_data[0]['email'].split('@')[1]}",
            Formatter("<redacted>@@@email.$split('@').1").single(small_data[0])
        )

    def test_surrounded_query(self):
        self.assertEqual(
            f'<p class="lead">{small_data[0]["email"]}</p>',
            Formatter('<p class="lead">@email</p>').single(small_data[0])
        )

    def test_one_missing_out_of_several(self):
        self.assertEqual(
            f"Name: {small_data[0]['name']}, Missing: <missing>",
            Formatter("Name: @name, Missing: @missing").single(small_data[0])
        )

    def test_special_surrounded(self):
        x = 5
        y = 5.6
        self.assertEqual(
            f"{x}+{y}={x + y}={y + x}",
            Formatter("@x+@y=@x.$add(@y)=@y.$add(@x)").single({"x": x, "y": y})
        )


if __name__ == "__main__":
    print(__version__)
    unittest.main()
