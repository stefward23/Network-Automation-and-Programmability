
import json

with open("portfolio.json", "r") as f:
    data = json.load(f)


with open("data2.json", "w") as f:
    json.dump(data,f)