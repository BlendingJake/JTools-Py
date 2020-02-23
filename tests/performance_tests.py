import sys
import json
import unittest
from pathlib import Path
from exectiming.exectiming import StaticTimer, Timer
from random import randint

sys.path.append("../")

from jtools import Filter, Key, Getter

folder = Path(__file__).parent
with open(folder / "data/10000.json", "r") as file:
    large_data = json.loads(file.read())


class PerformanceTesting(unittest.TestCase):
    def test_getter_reuse(self):
        runs = 15

        recreate_time = StaticTimer.time_it(
            lambda: [Getter('email.$split("@").1.$split(".").0').single(item) for item in large_data],
            runs=runs, iterations_per_run=1, display=False, log_arguments=False
        )[1]

        getter = Getter('email.$split("@").1.$split(".").0')
        reuse_time = StaticTimer.time_it(
            lambda: [getter.single(item) for item in large_data],
            runs=runs, iterations_per_run=1, display=False, log_arguments=False
        )[1]

        print(recreate_time / reuse_time, "x faster to reuse Getter then recreate")
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


if __name__ == "__main__":
    timer = Timer()

    timer.time_it(Filter(Key("age") > 40).many, lambda: large_data[:randint(0, len(large_data))],
                  call_callable_args=True, runs=10, iterations_per_run=1, log_arguments=True,
                  split_label="Filter ('age')")

    timer.time_it(Filter(Key("friends.$length") > 3).many, lambda: large_data[:randint(0, len(large_data))],
                  call_callable_args=True, runs=10, iterations_per_run=1, log_arguments=True,
                  split_label="Filter ('friends.$length')")

    timer.time_it(Filter(
        Key("latitude").gte(-45) & Key("latitude").lte(45) & Key("longitude").lte(0)
    ).many, lambda: large_data[:randint(0, len(large_data))],
                  call_callable_args=True, runs=10, iterations_per_run=1, log_arguments=True,
                  split_label="Filter (lat/lon)")

    timer.plot(split_index=0, transformer=len, multiple=True, plot_curve=True,
               curve=timer.best_fit_curve(0, curve_type="Linear", transformers=len),
               equation_rounding=4)
    timer.plot(split_index=1, transformer=len, multiple=True, plot_curve=True,
               curve=timer.best_fit_curve(1, curve_type="Linear", transformers=len),
               equation_rounding=4)
    timer.plot(split_index=2, transformer=len, plot_curve=True,
               curve=timer.best_fit_curve(2, curve_type="Linear", transformers=len),
               equation_rounding=4)

    timer.statistics()