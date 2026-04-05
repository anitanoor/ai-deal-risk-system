import os
from openai import OpenAI
from dotenv import load_dotenv
from utils import log_event

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def calculate_risk(deal):
    risk = 0

    if int(deal["last_activity_days"]) > 10:
        risk += 0.4

    if deal["stage"] == "discovery":
        risk += 0.3

    if int(deal["amount"]) > 100000:
        risk += 0.2

    return min(risk, 1.0)


def get_ai_reason(deal):
    prompt = f"""
    Analyze this sales deal and explain if it's risky.

    Deal:
    Amount: {deal['amount']}
    Stage: {deal['stage']}
    Last Activity Days: {deal['last_activity_days']}
    Notes: {deal['notes']}

    Return:
    - Risk level (low/medium/high)
    - Reason
    - Suggested action
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content


def route_action(result):
    if result["risk_score"] > 0.6:
        print("🚨 Alert sent: High-risk deal!")
    elif result["risk_score"] > 0.3:
        print("⚠️ Monitoring deal")
    else:
        print("✅ Healthy deal")


def evaluate_deal(deal):
    score = 0

    if deal["last_activity_days"] > 30:
        score += 0.4
    if deal["stage"] == "proposal":
        score += 0.3
    if deal["amount"] > 10000:
        score += 0.3

    risk_level = "LOW"
    if score > 0.7:
        risk_level = "HIGH"
    elif score > 0.4:
        risk_level = "MEDIUM"

    # 🔥 AI explanation layer
    try:
        from utils import get_ai_reason
        reason = get_ai_reason(deal)
    except:
        reason = "AI explanation unavailable"

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "reason": reason
    }