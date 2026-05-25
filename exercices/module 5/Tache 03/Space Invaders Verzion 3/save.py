import json
import os

FILE = "save.json"

def load_save():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)

    return {"best_score": 0}

def save_game(data):
    with open(FILE, "w") as f:
        json.dump(data, f)