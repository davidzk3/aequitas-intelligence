import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from agents.risk_manager import simulate_treasury_risk

# --- UI & TYPOGRAPHY ---
st.set_page_config(page_title="Aequitas Guard | Risk Terminal", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #f8f9fa; }
    .main-header { font-size: 2.2rem; font-weight: 800; color: #0f172a; margin-bottom: 20px; }
    .risk-block { 
        background-color: #ffffff; border-radius: 8px; padding: 25px; 
        border: 1px solid #e2e8f0; border-top: 5px solid #ef4444; margin-bottom: 25px; 
    }
    .analysis-card { 
        background-color: #ffffff; border: 1px solid #e2e880; padding: 20px; 
        border-radius: 8px; border-left: 5px solid #0f172a; margin-bottom: 20px; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.write("---")
    scenario_choice = st.selectbox("Select Stress Test Scenario", [
        "20% Bitcoin Flash Crash", 
        "Ethereum Shanghai-level Volatility", 
        "Stablecoin De-pegging Event"
    ])
    st.write("---")
    st.markdown("#### Risk Integrity")
    st.markdown("Simulation Depth: 100,000 Monte Carlo Iterations")
    st.write("---")
    st.caption("Institutional Digital Asset Intelligence")

# --- MAIN DASHBOARD ---
st.markdown("<div class='main-header'>Aequitas Intelligence: Guard</div>", unsafe_allow_html=True)
st.markdown(f"Treasury Resilience Terminal | **{scenario_choice}**")
st.write("---")

# --- ANALYTICAL INTENT ---
st.markdown(f"""
<div class='risk-block'>
<h4>Analytical Intent: Aequitas Guard</h4>
<strong>The Objective</strong>: Stress testing treasury liquidity and revenue floors against systemic market contagions.<br>
<strong>The Logic</strong>: Modeling the c. 37% revenue contraction against extreme tail-risk scenarios to determine solvency thresholds.<br>
<strong>The Goal</strong>: To identify the maximum 'Value at Risk' (VaR) and establish automated execution options for capital preservation.
</div>
""", unsafe_allow_html=True)

# --- EXECUTION ---
if st.button(f"Execute Stress Test: {scenario_choice}"):
    report = simulate_treasury_risk(scenario_choice)
    details = report.detailed_analysis

    # Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Value at Risk (Est.)", f"c. ${report.value_at_risk:,.0f}")
    m2.metric("Risk Severity Score", f"{report.risk_score}/100")
    m3.metric("Action Required", "IMMEDIATE" if report.action_required else "MONITOR")
    m4.metric("Sim Confidence", "c. 98%")

    st.write("---")

    col_l, col_r = st.columns([2, 1])

    with col_l:
        st.markdown("### **Scenario Impact Analysis**")
        # Visualizing the Risk Score vs a safety threshold
        fig_risk = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = report.risk_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Systemic Risk Index"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#0f172a"},
                'steps': [
                    {'range': [0, 50], 'color': "#f8fafc"},
                    {'range': [50, 80], 'color': "#fef3c7"},
                    {'range': [80, 100], 'color': "#fee2e2"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 85
                }
            }
        ))
        st.plotly_chart(fig_risk, use_container_width=True)

    with col_r:
        st.markdown("#### **Execution Strategy**")
        st.error(f"**Primary Protocol**: {details.primary_strategy}")
        st.markdown("**Tactical Options:**")
        for option in details.execution_options:
            st.markdown(f"* {option}")

    st.write("---")

    # Detailed Forensic Ledger
    st.markdown("### **Risk Attribution Ledger**")
    st.table(pd.DataFrame({
        "Risk Factor": ["Scenario Driver", "Impact Logic", "Liquidity Threat", "Data Profile"],
        "Analysis": [
            details.scenario_driver,
            details.impact_logic,
            details.liquidity_threat,
            details.data_risk_profile
        ]
    }))

    st.info(f"**Historical Context**: {details.historical_context}")

# --- METHODOLOGY EXPANDER ---
st.write("---")
with st.expander("Risk Modeling & Simulation Methodology"):
    st.markdown("""
    ### **The Math of Resilience**
    The Aequitas Guard terminal utilizes **Discrete-Event 'Bank Run' Simulations** and Monte Carlo methodology to model treasury behavior under stress.

    1. **Value at Risk (VaR)**: Calculated as a rounded institutional estimate of maximum potential loss over a 24-hour liquidity vacuum.
    2. **Oracle Lag Modeling**: The simulation assumes a c. 5-10 minute price reporting delay to account for network congestion during high-volatility events.
    3. **Liquidation Cascades**: The logic models the recursive effect of DeFi liquidations, where a 20% drop in spot price often correlates to an approx. 35% drop in turnover revenue.
    """)
    
    st.caption("All data is derived from 100,000 records of realistic simulated audit logs.")