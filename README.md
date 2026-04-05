# 💰 AI Deal Risk Intelligence System

An AI-powered system that evaluates and scores deal risk using behavioral signals, business logic, and data-driven insights.

---

## 🚀 Overview

This project simulates a real-world **AI-driven sales intelligence system** used by revenue and operations teams to identify risky deals early and take proactive action.

It combines backend APIs, data processing, and an interactive dashboard to deliver actionable insights.

---

## 🧠 Key Capabilities

* 📊 Analyze deal data (amount, stage, inactivity)
* ⚠️ Generate risk scores (LOW / MEDIUM / HIGH)
* 🧾 Provide reasoning behind each risk score
* 📈 Visualize insights through an interactive dashboard
* 🛡 Handle messy or inconsistent real-world data

---

## 🛠 Tech Stack

* **Python** — core programming language
* **FastAPI** — backend API for risk scoring
* **Streamlit** — interactive dashboard UI
* **Pandas** — data processing and analysis

---

## 📊 Features

* Real-time deal risk evaluation
* Rule-based + AI-inspired scoring logic
* Clean and interactive dashboard
* Data visualization (deal stages, inactivity trends)
* Error handling for malformed CSV data

---

## 🗂 Project Structure

```
ai-deal-risk-system/
│
├── app.py              # FastAPI backend
├── dashboard.py       # Streamlit dashboard
├── data/
│   └── deals.csv      # Sample dataset
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/anitanoor/ai-deal-risk-system.git
cd ai-deal-risk-system
```

---

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run backend API

```bash
python3 -m uvicorn app:app --reload
```

API will be available at:
👉 http://127.0.0.1:8000

---

### 5. Run dashboard

```bash
streamlit run dashboard.py
```

Dashboard will open automatically in your browser.

---

## 📌 Example API Response

```json
{
  "risk_score": 0.7,
  "risk_level": "HIGH",
  "reason": "Client inactive for extended period"
}
```

---

## 💡 Use Cases

* Sales teams identifying at-risk deals
* Revenue operations prioritizing pipeline
* AI experimentation for decision systems
* Portfolio project demonstrating full-stack + AI thinking

---

## 🔥 What This Project Demonstrates

* End-to-end system design (data → API → UI)
* Real-world debugging and data handling
* Applied AI logic (risk scoring + reasoning)
* Ability to ship functional, production-style projects

---

## 👤 Author

**Anita Noor**

---

## 🚀 Next Steps

* Deploy backend (Render / Railway)
* Deploy dashboard (Streamlit Cloud)
* Integrate real CRM data
* Add ML-based risk prediction

---

## ⭐ If you found this useful

Give it a star on GitHub — it helps visibility!
