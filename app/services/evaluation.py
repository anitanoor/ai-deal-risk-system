import os
from typing import Dict

from openai import OpenAI

from app.core.config import OPENAI_API_KEY, OPENAI_MODEL
from app.core.logger import log_event, logger


client = None
if OPENAI_API_KEY:
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
    except Exception as exc:
        log_event(f"Failed to initialize OpenAI client: {exc}")


def calculate_risk(deal: Dict) -> float:
    score = 0.0

    if int(deal.get("last_activity_days", 0)) > 10:
        score += 0.4

    stage = str(deal.get("stage", "")).lower()
    if stage in {"discovery", "proposal"}:
        score += 0.3

    if float(deal.get("amount", 0)) > 10000:
        score += 0.3

    return min(score, 1.0)


def safe_analyze(deal: Dict):
    try:
        return {"risk_score": calculate_risk(deal)}
    except Exception as exc:
        logger.error("Error analyzing deal", exc_info=True)
        return {"error": "analysis failed"}


def get_ai_reason(deal: Dict) -> str:
    if client is None:
        return "AI explanation unavailable"

    prompt = f"""
Analyze this sales deal and explain if it's risky.

Deal:
Amount: {deal.get('amount')}
Stage: {deal.get('stage')}
Last Activity Days: {deal.get('last_activity_days')}
Notes: {deal.get('notes')}

Return:
- Risk level (low/medium/high)
- Reason
- Suggested action
"""

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as exc:
        log_event(f"AI reason call failed: {exc}")
        return "AI explanation unavailable"


def route_action(result: Dict) -> None:
    if result["risk_score"] > 0.6:
        print("🚨 Alert sent: High-risk deal!")
    elif result["risk_score"] > 0.3:
        print("⚠️ Monitoring deal")
    else:
        print("✅ Healthy deal")


def evaluate_deal(deal: Dict) -> Dict:
    logger.info("Analyzing deal", extra={"deal_id": deal.get("deal_id")})
    score = calculate_risk(deal)

    risk_level = "LOW"
    if score > 0.7:
        risk_level = "HIGH"
    elif score > 0.4:
        risk_level = "MEDIUM"

    reason = get_ai_reason(deal)
    result = {
        "risk_score": min(score, 1.0),
        "risk_level": risk_level,
        "reason": reason,
    }

    route_action(result)
    return result
