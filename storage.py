#
#
#
#
###############################################################################

import json
from typing import Any

def load_notes()-> list[dict[str, Any]]:
    try:
        with open("data/notes.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_notes(notes: list[dict[str, Any]])-> None:
    with open("data/notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)
