import sys
import json
from exectiming.exectiming import Timer
from random import randint

sys.path.append("../")

from jtools import Filter, Key

with open("./data/10000.json", "r") as file:
    large_data = json.loads(file.read())

if __name__ == "__main__":
    timer = Timer()

    timer.time_it(Filter(Key("age") > 40).filter, lambda: large_data[:randint(0, len(large_data))],
                  call_callable_args=True, runs=10, iterations_per_run=1, log_arguments=True,
                  split_label="Filter ('age')")

    timer.time_it(Filter(Key("friends.$length") > 3).filter, lambda: large_data[:randint(0, len(large_data))],
                  call_callable_args=True, runs=10, iterations_per_run=1, log_arguments=True,
                  split_label="Filter ('friends.$length')")

    timer.time_it(Filter(
        Key("latitude").gte(-45) & Key("latitude").lte(45) & Key("longitude").lte(0)
    ).filter, lambda: large_data[:randint(0, len(large_data))],
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
