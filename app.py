from fastapi import FastAPI
import pandas as pd
from risk_engine import evaluate_deal

app = FastAPI()

df = pd.read_csv(
    "data/deals.csv",
    quotechar='"',
    skipinitialspace=True,
    on_bad_lines='skip'
)


@app.get("/")
def home():
    return {"message": "AI Deal Risk System Running"}


@app.get("/deals")
def get_deals():
    return df.to_dict(orient="records")


@app.get("/evaluate/{deal_id}")
def evaluate(deal_id: int):
    deal = df[df["deal_id"] == deal_id].iloc[0].to_dict()
    result = evaluate_deal(deal)

    return {
        "deal": deal,
        "evaluation": result
    }
