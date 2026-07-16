import json
import models

with open("configs/test-process.json") as f:
    config = json.load(f)

    models.ServerConfig(**config)