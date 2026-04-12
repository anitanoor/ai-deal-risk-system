import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "deals.csv"
SETTINGS_PATH = BASE_DIR / "configs" / "settings.json"

with open(SETTINGS_PATH, "r") as f:
    settings = json.load(f)

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
RISK_THRESHOLD = settings.get("risk_threshold", 0.7)
INACTIVE_DAYS_LIMIT = settings.get("inactive_days_limit", 14)
ALERT_ENABLED = settings.get("alert_enabled", True)
