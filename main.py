import json

with open("configs/test-process.json") as f:
    config = json.load(f)

    print(config["id"])
    print(config["ressources"]["memory"])