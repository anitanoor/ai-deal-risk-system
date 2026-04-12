from app.services.evaluation import calculate_risk, evaluate_deal, safe_analyze


def test_risk_score():
    deal = {"value": 1000, "last_activity_days": 30}
    result = calculate_risk(deal)
    assert result > 0


def test_safe_analyze_handles_errors():
    deal = {"amount": "invalid", "last_activity_days": "bad"}
    result = safe_analyze(deal)
    assert result == {"error": "analysis failed"}


def test_evaluate_deal_high_risk():
    deal = {
        "deal_id": 1,
        "amount": 25000,
        "stage": "proposal",
        "last_activity_days": 45,
        "notes": "Important prospect",
    }

    result = evaluate_deal(deal)

    assert result["risk_score"] == 1.0
    assert result["risk_level"] == "HIGH"
    assert "reason" in result


def test_evaluate_deal_low_risk():
    deal = {
        "deal_id": 2,
        "amount": 500,
        "stage": "discovery",
        "last_activity_days": 3,
        "notes": "Warm lead",
    }

    result = evaluate_deal(deal)

    assert result["risk_score"] == 0.3
    assert result["risk_level"] == "LOW"
    assert "reason" in result
