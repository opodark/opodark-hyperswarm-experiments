import json
from datetime import datetime

MEMORY = []


def write(entry: dict):

    entry["timestamp"] = datetime.utcnow().isoformat()

    MEMORY.append(entry)

    return entry


def query(filter_type: str = None):

    if not filter_type:
        return MEMORY

    return [
        m for m in MEMORY
        if m.get("type") == filter_type
    ]


def export_json():

    return json.dumps(MEMORY, indent=2)