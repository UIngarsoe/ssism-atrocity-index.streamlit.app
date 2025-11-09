# streamlit_app.py — AUTO-TEST MODE
import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="SSISM Atrocity Index", layout="wide")
st.markdown("# SSISM Atrocity Index")
st.markdown("### **TEST FIRE: VETO EXPOSED**")

# Auto-load sample data
@st.cache_data
def load_samples():
    ground = pd.read_csv("data/ground.csv")
    osint = pd.read_csv("data/osint.csv")
    return ground, osint

if st.button("TEST FIRE: Compute HCV (Sample Data)", type="primary"):
    ground, osint = load_samples()
    
    # Dummy real computation
    s = 0.75  # Satellite: village destruction
    o = osint['confidence'].mean()  # OSINT avg
    g = np.tanh(ground.mean().mean() / 10000)  # Normalized ground
    
    h = 0.5 * s + 0.25 * o + 0.25 * g
    phi = 1 / (1 + np.exp(-(2.5 * h - 1.0)))
    
    st.success("HCV COMPUTED — VETO QUANTIFIED")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Atrocity Index (H)", f"{h:.2f}", delta="High Risk")
    with col2:
        st.metric("Accountability Likelihood (Φ_A)", f"{phi:.2%}", delta="Strong Case")
    
    st.bar_chart({"If Action Taken": [0.2], "Vetoed Reality": [h]})
    st.balloons()
else:
    st.info("Click **TEST FIRE** to run the Index on Myanmar sample data.")
    st.code("""
deaths: 5,800+
displaced: 3.1M
aid blocked: $6.4B
OSINT: Telegram reports
Satellite: Village burns
    """)
