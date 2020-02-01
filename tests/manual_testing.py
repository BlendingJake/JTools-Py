import sys
import json

sys.path.append("../")

from jtools import Filter, Key

with open("./data/10000.json", "r") as file:
    large_data = json.loads(file.read())

with open("./data/20.json", "r") as file:
    small_data = json.loads(file.read())

if __name__ == "__main__":
    test = [{"value": i} for i in range(10)]
    print(test)

    print(Filter(Key("value") < 5).many(test))
    print(Filter(~Key("value").lt(5)).many(test))

    print(Filter(Key("value").lt(3) | Key("value").gt(7)).many(test))
    print(Filter(~(Key("value").lt(3) | Key("value").gt(7))).many(test))
