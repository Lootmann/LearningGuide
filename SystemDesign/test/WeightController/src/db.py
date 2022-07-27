# src/db.py
import json
from datetime import datetime
from pathlib import Path


class DB:
    FILENAME = "weight.json"

    def __init__(self) -> None:
        self.current = Path(".").expanduser() / self.FILENAME

        if not self.current.exists():
            self.current.write_text("{}")

        with self.current.open("r", encoding="utf-8") as f:
            self.json = json.load(f)

        # NOTE: more good id PRIMARY KEY
        idx = "0"
        for key in self.json.keys():
            idx = key

        self.idx = int(idx) + 1

    def increment(self):
        self.idx += 1

    def insert(self, weight: float, fat_rate: float):
        current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.json[self.idx] = {
            "weight": weight,
            "fat_rate": fat_rate,
            "created_at": current,
            "updated_at": current,
        }
        self.increment()

    def dump(self):
        with self.current.open("w", encoding="utf8") as j:
            json.dump(self.json, j, ensure_ascii=True)
