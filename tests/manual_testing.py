import sys
import json
from exectiming.exectiming import Timer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import jtools

with open("./data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open("./data/20.json", "r") as file:
    small_data = json.loads(file.read())

if __name__ == "__main__":
    t = Timer(split=True, start=True, label=f'Query: {jtools.__version__}')
    data = {'data': {'meta': {'timestamp': 12}}}
    reps = 1000
    ipr = 10

    for i in range(reps):
        for j in range(ipr):
            d = jtools.Query('data.meta.timestamp').single(data)
        t.log(iterations_per_run=ipr)

    print(d)
    t.statistics()
