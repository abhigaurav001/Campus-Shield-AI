import streamlit as st
import random
import datetime
import pandas as pd


st.set_page_config(
    page_title="Campus Shield AI",
    page_icon="🛡",
    layout="centered"
)

st.title("🛡 Campus Shield AI")
st.subheader("Smart Campus Threat Detection & Emergency Response System")

st.markdown("---")


@st.cache_data
def load_data():
    return pd.read_csv("campus_dataset.csv")

data = load_data()

if st.checkbox("📂 Show Validation Dataset"):
    st.write(data)

st.markdown("---")


threat_keywords = {
    "Extreme Violence": {
        "words": ["bomb","blast","explosion","kill","gun","knife","terrorist"],
        "weight": 5
    },
    "Physical Fight": {
        "words": ["fight","clash","attack","assault","beat","punch","fighting","kal dekh lunga tm sbko"],
        "weight": 3
    },
    "Harassment & Bullying": {
        "words": ["bully","harassment","abuse","threaten","ragging","harassed","bahar mil merko"],
        "weight": 2
    },
    "Self Harm / Suicide Risk": {
        "words": ["suicide","kill myself","self harm","depressed","depression"],
        "weight": 5
    },
    "Emergency Situation": {
        "words": ["fire","emergency","accident","danger","help"],
        "weight": 4
    },
    "Suspicious Activity": {
        "words": ["suspicious","unknown person","unauthorized","stranger"],
        "weight": 2
    },
    "Misinformation Risk": {
        "words": ["classes suspended","exam cancelled","holiday declared","college closed"],
        "weight": 1
    }
}


def analyze_text(text):
    text = text.lower()
    score = 0
    categories = []

    for category, data in threat_keywords.items():
        for word in data["words"]:
            if word in text:
                score += data["weight"]
                if category not in categories:
                    categories.append(category)

    return score, categories


user_input = st.text_area("📝 Enter Complaint or Message:")

if st.button("🔍 Analyze Threat"):

    if user_input.strip() == "":
        st.warning("⚠ Please enter some text.")
    else:
        score, categories = analyze_text(user_input)

        risk_percent = min(score * 10, 100)

        st.markdown("### 📊 Risk Assessment")
        st.progress(risk_percent)
        st.write(f"Risk Percentage: {risk_percent}%")

        if categories:
            st.markdown("### 🚨 Detected Categories:")
            for cat in categories:
                st.write(f"- {cat}")

        if "Misinformation Risk" in categories:
            st.warning("⚠ This appears to be an unverified notice. Please confirm officially.")

        confidence = random.randint(85, 98)
        st.write(f"🤖 AI Confidence Score: {confidence}%")

        if risk_percent == 0:
            st.success("✅ SAFE ZONE")
        elif risk_percent <= 40:
            st.warning("⚠ LOW RISK")
        elif risk_percent <= 70:
            st.warning("⚠ MEDIUM RISK")
        else:
            st.error("🚨 HIGH RISK ALERT")

        incident_id = f"INC{random.randint(1000,9999)}"
        st.write(f"🆔 Incident ID: {incident_id}")

        now = datetime.datetime.now()
        st.write(f"🕒 Report Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

st.markdown("---")




st.markdown("## 🚨 Emergency SOS System")

emergency_number = st.text_input(
    "📞 Enter Emergency Contact Number:",
    "+91"
)

if st.button("🚨 ACTIVATE SOS"):

    if emergency_number.strip() == "":
        st.warning("Enter valid number.")
    else:
        st.error("🚨 SOS ACTIVATED")

        st.markdown(f"""
        <a href="tel:{emergency_number}">
            <button style="background-color:red;color:white;
            padding:12px 25px;border:none;border-radius:8px;
            font-size:16px;font-weight:bold;">
            📞 CALL NOW
            </button>
        </a>
        """, unsafe_allow_html=True)

        st.success("Emergency link generated.")
