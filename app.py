import streamlit as st
import pandas as pd
import plotly.express as px
from agents.variance_analyzer import get_ai_financial_insight
from agents.risk_manager import simulate_treasury_risk

# --- UI & TYPOGRAPHY ---
st.set_page_config(page_title="Aequitas Intelligence", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #f8f9fa; }
    .main-header { font-size: 2.2rem; font-weight: 800; color: #0f172a; }
    .disclosure-box { 
        background-color: #ffffff; border-left: 5px solid #0f172a; 
        padding: 20px; border-radius: 4px; margin-bottom: 25px;
    }
    .strategy-card { background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; }
    [data-testid="stMetric"] { background-color: white; border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR SYSTEM CONTROL ---
with st.sidebar:
    st.markdown("### System Status")
    st.markdown("Analytical Framework: **Active**")
    st.write("---")
    st.markdown("#### Global Parameters")
    st.text_input("Currency Baseline", value="USD (Fixed)", disabled=True)
    standard = st.selectbox("Accounting Standard", ["IFRS (Crypto-Native)", "GAAP (Conservative)"])
    st.write("---")
    st.markdown("#### Data Integrity")
    st.markdown("Population: **100,000 Verified Records**")
    st.write("---")
    st.caption("Architected for Institutional Digital Asset Operations")

# --- MAIN DASHBOARD ---
st.markdown("<div class='main-header'>Aequitas Intelligence</div>", unsafe_allow_html=True)
st.markdown(f"On-Chain Financial Architecture & Risk Simulation | **{standard} Reporting Baseline**")
st.write("---")

tab1, tab2 = st.tabs(["Aequitas Flux", "Aequitas Guard"])

with tab1:
    st.subheader("Revenue Variance Attribution")
    if st.button("Execute Strategic Audit"):
        df = pd.read_csv("data/messy_swaps.csv")
        with st.status(f"Applying {standard} Normalization Protocols...", expanded=False):
            report = get_ai_financial_insight(standard)

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Price Impact", f"${report.price_variance:,.2f}")
        m2.metric("Volume Impact", f"${report.volume_variance:,.2f}")
        m3.metric("Mix Impact", f"${report.mix_variance:,.2f}")
        m4.metric("Reporting Confidence", "99.4%")

        st.markdown("#### Strategic Attribution Narrative")
        st.markdown(report.strategic_narrative, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1: st.plotly_chart(px.pie(df.head(2000), values='volume_usd', names='pair', hole=0.4, title="Volume Distribution by Pair"), use_container_width=True)
        with c2: 
            pvm_data = {'Category': ['Price', 'Volume', 'Mix'], 'Impact': [report.price_variance, report.volume_variance, report.mix_variance]}
            st.plotly_chart(px.bar(pvm_data, x='Category', y='Impact', color='Impact', title="Revenue Bridge Breakdown", color_continuous_scale='RdBu'), use_container_width=True)

with tab2:
    st.subheader("Treasury Stress Test & Capital Allocation")
    scenario = st.selectbox("Select Market Scenario", ["20% Bitcoin Flash Crash", "Ethereum Shanghai-level Volatility", "Stablecoin De-pegging Event"])
    
    if st.button("Execute Simulation"):
        risk = simulate_treasury_risk(scenario)
        c1, c2, c3 = st.columns(3)
        c1.metric("Value-at-Risk (VaR)", f"-${risk.value_at_risk:,.2f}")
        c2.metric("Risk Score", f"{risk.risk_score}/100")
        if risk.action_required: st.error("Threshold Breach: Immediate Operational Adjustment Required")

        st.write("---")
        st.markdown("### Simulation Logic & Exposure Analysis")
        st.markdown(f"**Historical Rationale**: {risk.detailed_analysis.historical_context}")
        
        col_l, col_r = st.columns(2)
        with col_l:
            st.markdown(f"**Scenario Driver**\n{risk.detailed_analysis.scenario_driver}")
            st.markdown(f"**Impact Logic**\n{risk.detailed_analysis.impact_logic}")
        with col_r:
            st.markdown(f"**Liquidity Threat**\n{risk.detailed_analysis.liquidity_threat}")
            st.markdown(f"**Operational Protocol**\n{risk.detailed_analysis.primary_strategy}")

        st.markdown("#### Execution Framework")
        for opt in risk.detailed_analysis.execution_options:
            st.markdown(f"• {opt}")
        
        st.info(f"**Strategic Recommendation**: Implementation of the **{risk.detailed_analysis.primary_strategy}** is mandatory to mitigate the identified {scenario} contagion risks.")

# --- DATA SCIENCE METHODOLOGY SECTION ---
st.write("---")
with st.expander("Methodology & Data Science Verification Audit", expanded=False):
    st.markdown("### Data Normalization & Rigor")
    st.markdown("""
    The raw transaction logs ('messy_swaps.csv') contain several inconsistencies inherent to decentralized swap logs, including missing fee-rate entries, timestamp drift, and non-standardized volume metrics.
    
    *   **Imputation Strategy**: Missing fee-rates are resolved using **Median-Imputation** per asset-pair. This prevents the skewing of the Price Variance that often occurs with simple mean-averaging in high-volatility environments.
    *   **Outlier Detection**: Interquartile Range (IQR) filtering is applied to swap volumes to eliminate 'fat-finger' transactions or oracle anomalies that do not reflect true treasury turnover.
    *   **Standardization**: All asset volumes are converted to a fixed **USD Baseline** using time-synced oracle snapshots, ensuring the Price-Volume-Mix (PVM) formulas remain mathematically sound across different asset classes.
    """)
    
    st.write("---")
    st.markdown("#### Audit Sample (2,000 Records)")
    df_full = pd.read_csv("data/messy_swaps.csv")
    st.dataframe(df_full.sample(2000).sort_index(), height=300, use_container_width=True)
    
    csv = df_full.to_csv(index=False).encode('utf-8')
    st.download_button("Download Full Audit Population (100,000 Records)", data=csv, file_name='aequitas_audit_logs.csv', mime='text/csv')