import json
from pathlib import Path


def export_json(data: dict):
    Path("output").mkdir(exist_ok=True)

    with open("output/report.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)