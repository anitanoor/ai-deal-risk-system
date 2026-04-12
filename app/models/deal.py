from typing import Optional

from pydantic import BaseModel


class Deal(BaseModel):
    deal_id: int
    amount: float
    stage: str
    last_activity_days: int
    notes: Optional[str] = None


class AnalyzeDeal(BaseModel):
    name: str
    value: float
    last_activity_days: int


class Evaluation(BaseModel):
    risk_score: float
    risk_level: str
    reason: str
