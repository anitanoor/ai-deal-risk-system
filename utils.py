import json
from datetime import datetime

def log_event(event):
    with open("logs.txt", "a") as f:
        f.write(json.dumps({
            "timestamp": str(datetime.now()),
            "event": event
        }) + "\n")