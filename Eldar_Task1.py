# TODO решите задачу
import json

filename = 'input.json'


def task() -> float:
    
    with open(filename, 'r') as f:
        file = json.load(f)
        sum_file = sum([item["score"] * item["weight"] for item in file])
    return round(sum_file,3)

print(task())
