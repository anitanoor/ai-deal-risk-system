import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Deal Risk Dashboard", layout="wide")

st.markdown("# 💰 AI Deal Risk Intelligence System")
st.caption("Real-time AI-powered deal risk analysis")

@st.cache_data
def load_deals():
    try:
        response = requests.get(f"{API_URL}/deals")
        data = response.json()
        df = pd.DataFrame(data)
        if "deal_id" not in df.columns:
            df["deal_id"] = df.index + 1
        return df
    except Exception as exc:
        st.error(f"Error loading data: {exc}")
        return pd.DataFrame()


df = load_deals()
if df.empty:
    st.stop()

st.sidebar.header("⚙️ Controls")
selected_id = st.sidebar.selectbox("Select Deal ID", df["deal_id"])

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Deals Overview")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("📊 Insights")
    if "stage" in df.columns:
        st.write("Deals by Stage")
        st.bar_chart(df["stage"].value_counts())
    else:
        st.warning("No 'stage' column found")

    activity_col = next(
        (col for col in df.columns if "activity" in col.lower() or "day" in col.lower()),
        None,
    )

    if activity_col:
        st.write(f"{activity_col} Distribution")
        st.line_chart(df[activity_col])
    else:
        st.warning("No activity-related column found")

st.subheader("🔍 Evaluate Deal")

if st.button("Run AI Risk Analysis"):
    try:
        response = requests.get(f"{API_URL}/evaluate/{selected_id}")
        result = response.json()
        score = result.get("risk_score", 0)
        level = result.get("risk_level", "UNKNOWN")
        color = "green"
        if level == "HIGH":
            color = "red"
        elif level == "MEDIUM":
            color = "orange"

        st.markdown("### 📈 Risk Result")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Risk Score", f"{score:.2f}")
        with col2:
            st.markdown(
                f"<h3 style='color:{color}'>{level}</h3>",
                unsafe_allow_html=True,
            )

        st.progress(min(max(score, 0), 1))
        st.write("🧠 AI Explanation")
        st.info(result.get("reason", "No explanation available"))
    except Exception as exc:
        st.error(f"Error connecting to API: {exc}")
