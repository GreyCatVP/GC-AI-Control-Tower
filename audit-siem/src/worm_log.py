import hashlib
import json
import time
from pathlib import Path

WORM_FILE = Path("logs/worm.log")
WORM_FILE.parent.mkdir(exist_ok=True)

def log_worm(event: dict) -> str:
    event["timestamp"] = time.time()
    line = json.dumps(event, sort_keys=True)
    h = hashlib.sha256(line.encode()).hexdigest()
    with WORM_FILE.open("a") as f:
        f.write(f"{line}###{h}\n")
    return h
