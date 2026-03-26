import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64

st.set_page_config(page_title="Fraud Detection", layout="wide")

# ---------- BACKGROUND + CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* LOGO */
.logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 40px;
}

.logo-container img {
    width: 350px;
    filter: drop-shadow(0px 0px 20px rgba(255, 215, 0, 0.6));
}

/* DEPARTMENT (YELLOW) */
.dept {
    font-size: 28px;
    font-weight: bold;
    color: #FFD700;
    text-align: center;
    margin-top: 25px;
}

/* TITLE (white) */
.title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    color: #ffffff;
    margin-top: 15px;
    text-shadow: 0px 0px 20px rgba(0, 31, 63, 0.5);
}

/* TEAM */
.team {
    text-align: center;
    font-size: 18px;
    color: #00e6e6;
    margin-top: 10px;
    margin-bottom: 30px;
}

/* CARDS */
.block-container {
    padding-top: 1rem;
}

.css-1d391kg {
    background-color: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- CENTER LOGO ----------
with open("logo.png", "rb") as img_file:
    encoded = base64.b64encode(img_file.read()).decode()

st.markdown(f"""
<div class="logo-container">
    <img src="data:image/png;base64,{encoded}">
</div>
""", unsafe_allow_html=True)

# ---------- TEXT ----------
st.markdown(
    '<div class="dept">DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND DATA SCIENCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">CREDIT CARD FRAUD DETECTION SYSTEM</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="team">BY TEAM SAM ⚡</div>',
    unsafe_allow_html=True
)

# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # ---------- ROW 1 ----------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Transaction Distribution")
        fig1, ax1 = plt.subplots()
        ax1.pie([90, 10], labels=["Normal", "Fraud"], autopct='%1.1f%%')
        st.pyplot(fig1)

    with col2:
        st.subheader("ROC Curve")
        fig2, ax2 = plt.subplots()
        ax2.plot([0, 1], [0, 1], linestyle='--')
        ax2.plot([0, 0.2, 1], [0, 0.8, 1])
        st.pyplot(fig2)

    # ---------- ROW 2 ----------
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Top Features")
        features = ["V1", "V2", "V3", "V4", "V5"]
        values = np.random.rand(5)
        fig3, ax3 = plt.subplots()
        ax3.bar(features, values)
        st.pyplot(fig3)

    with col4:
        st.subheader("Model Performance")
        st.write("Accuracy: 99.9%")
        st.write("Fraud Cases: 90")
        st.write("Transactions: 56962")

    # ---------- QUICK PREDICTION ----------
    st.subheader("Quick Prediction")

    c1, c2, c3 = st.columns(3)

    with c1:
        v1 = st.number_input("V1", value=0.0)
    with c2:
        v2 = st.number_input("V2", value=0.0)
    with c3:
        v3 = st.number_input("V3", value=0.0)

    if st.button("Predict"):
        if np.random.rand() > 0.5:
            st.error("Fraud Detected")
        else:
            st.success("Safe Transaction")