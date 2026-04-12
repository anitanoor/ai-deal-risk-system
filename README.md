# AI Deal Risk System

A lightweight AI-assisted deal risk scoring system that helps sales teams detect risky deals early, reduce lost revenue, and automate follow-up actions.

## 🔥 Problem

Sales teams lose revenue when deals slip through the cracks. Poor activity tracking, stale pipeline stages, and missing risk signals make it hard to identify bad deals before they turn into losses.

## 💡 Solution

This system applies AI risk scoring and automation to every deal:

- `GET /evaluate/{deal_id}` scores real deals from a dataset
- `POST /analyze-deal` accepts new deal data and returns a risk score
- AI explanation and routing are simulated through scoring logic and logging

## 🧠 Architecture

```
Client
  ├─> /health
  ├─> /metrics
  ├─> /deals
  ├─> /evaluate/{deal_id}
  └─> /analyze-deal

FastAPI app
  ├── app/main.py
  ├── app/api/routes.py
  ├── app/services/evaluation.py
  ├── app/models/deal.py
  ├── app/core/config.py
  └── app/utils/data_loader.py

Data + config
  ├── data/deals.csv
  └── configs/settings.json
```

> The API routes request traffic through FastAPI, risk logic in `app/services`, and sample config via JSON settings.

## ⚙️ API Usage

### Health check

```bash
curl http://localhost:8000/health
```

### Metrics

```bash
curl http://localhost:8000/metrics
```

### List deals

```bash
curl http://localhost:8000/deals
```

### Evaluate a deal

```bash
curl http://localhost:8000/evaluate/1
```

### Analyze a new deal

```bash
curl -X POST http://localhost:8000/analyze-deal \
  -H "Content-Type: application/json" \
  -d '{"name": "Deal A", "value": 12000, "last_activity_days": 20}'
```

## 📊 Sample output

### `/metrics`

```json
{
  "accuracy": 0.85,
  "precision": 0.8,
  "request_id": "..."
}
```

### `/analyze-deal`

```json
{
  "risk_score": 0.4,
  "request_id": "..."
}
```

### `/health`

```json
{
  "status": "ok",
  "service": "AI Deal Risk System",
  "request_id": "..."
}
```

## 🚀 How to run (Docker)

Build the Docker image:

```bash
docker build -t ai-deal-risk-system .
```

Run the container:

```bash
docker run -p 8000:8000 ai-deal-risk-system
```

Open the API in your browser or use curl at:

```bash
http://localhost:8000
```

## 🧪 Testing

```bash
pytest
```
