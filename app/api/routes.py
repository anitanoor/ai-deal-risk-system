import uuid

import pandas as pd
from fastapi import APIRouter, HTTPException

from app.core.logger import logger
from app.models.deal import AnalyzeDeal, Deal, Evaluation
from app.services.evaluation import calculate_risk, evaluate_deal, safe_analyze
from app.utils.data_loader import load_deals

router = APIRouter()


@router.get("/", response_model=dict)
def home():
    return {"message": "AI Deal Risk System Running"}


@router.get("/health", response_model=dict)
def health():
    request_id = str(uuid.uuid4())
    logger.info(f"Request started {request_id}", extra={"request_id": request_id})
    return {"status": "ok", "service": "AI Deal Risk System", "request_id": request_id}


@router.get("/metrics", response_model=dict)
def metrics():
    request_id = str(uuid.uuid4())
    logger.info(f"Request started {request_id}", extra={"request_id": request_id})

    return {
        "accuracy": 0.85,
        "precision": 0.8,
        "request_id": request_id,
    }


@router.post("/analyze-deal", response_model=dict)
def analyze_deal(deal: AnalyzeDeal):
    request_id = str(uuid.uuid4())
    logger.info(f"Request started {request_id}", extra={"request_id": request_id})

    result = safe_analyze(
        {
            "amount": deal.value,
            "stage": "proposal",
            "last_activity_days": deal.last_activity_days,
        }
    )
    logger.info("Analyzing deal", extra={"deal_name": deal.name, "request_id": request_id})
    return {**result, "request_id": request_id}


@router.get("/deals", response_model=list[Deal])
def get_deals():
    request_id = str(uuid.uuid4())
    logger.info(f"Request started {request_id}", extra={"request_id": request_id})

    df = load_deals()
    return df.to_dict(orient="records")


@router.get("/evaluate/{deal_id}", response_model=Evaluation)
def evaluate(deal_id: int):
    request_id = str(uuid.uuid4())
    logger.info(f"Request started {request_id}", extra={"request_id": request_id})

    df = load_deals()
    matching = df[df["deal_id"] == deal_id]
    if matching.empty:
        raise HTTPException(status_code=404, detail="Deal not found")

    deal = matching.iloc[0].to_dict()
    logger.info("Analyzing deal", extra={"deal_id": deal_id, "request_id": request_id})
    return evaluate_deal(deal)
