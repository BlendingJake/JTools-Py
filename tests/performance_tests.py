import sys
import json
import unittest
from pathlib import Path
from exectiming.exectiming import StaticTimer, Timer
from random import randint

sys.path.append("../")

from jtools import Filter, Key, Query

folder = Path(__file__).parent
with open(folder / "data/10000.json", "r") as file:
    large_data = json.loads(file.read())


class PerformanceTesting(unittest.TestCase):
    def test_query_reuse(self):
        runs = 15

        recreate_time = StaticTimer.time_it(
            lambda: [Query('email.$split("@").1.$split(".").0').single(item) for item in large_data],
            runs=runs, iterations_per_run=1, display=False, log_arguments=False
        )[1]

        getter = Query('email.$split("@").1.$split(".").0')
        reuse_time = StaticTimer.time_it(
            lambda: [getter.single(item) for item in large_data],
            runs=runs, iterations_per_run=1, display=False, log_arguments=False
        )[1]

        print(recreate_time / reuse_time, "x faster to reuse Query then recreate")
        self.assertGreater(recreate_time / reuse_time, 5)

    def test_filter_reuse(self):
        runs = 15

        recreate_time = StaticTimer.time_it(
            lambda: [
                Filter(Key("gender").eq("male").and_(Key("friends.$length").gte(3))).single(item) for item in large_data
            ],
            runs=runs, iterations_per_run=1, display=False, log_arguments=False
        )[1]

        f = Filter(Key("gender").eq("male").and_(Key("friends.$length").gte(3)))
        reuse_time = StaticTimer.time_it(
            lambda: [f.single(item) for item in large_data],
            runs=runs, iterations_per_run=1, display=False, log_arguments=False
        )[1]

        print(recreate_time / reuse_time, "x faster to reuse Filter then recreate")
        self.assertGreater(recreate_time / reuse_time, 5)
