import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_event(event: str, path: str = "logs.txt") -> None:
    with open(path, "a") as f:
        f.write(
            json.dumps({"timestamp": str(datetime.now()), "event": event}) + "\n"
        )
