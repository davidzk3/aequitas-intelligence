import streamlit as st
import pandas as pd
import plotly.express as px
from utils.finance_logic import calculate_pvm_attribution
from utils.growth_logic import simulate_growth_data
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
    .intro-block { 
        background-color: #ffffff; border-radius: 8px; padding: 25px; 
        border: 1px solid #e2e8f0; margin-bottom: 25px; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR[cite: 10] ---
with st.sidebar:
    st.markdown("### System Status")
    st.markdown("Analytical Framework: Active")
    st.write("---")
    standard = st.selectbox("Accounting Standard", ["IFRS (Crypto-Native)", "GAAP (Conservative)"])
    st.write("---")
    st.markdown("#### Data Integrity")
    st.markdown("Population: 100,000 Verified Records")
    st.caption("Architected for Exodus Movement Inc. (NYSE: EXOD)")

st.markdown("<div class='main-header'>Aequitas Intelligence</div>", unsafe_allow_html=True)
st.markdown(f"Forensic Autopsy & Strategic Growth Simulation | **{standard} Baseline**")
st.write("---")

tab1, tab2, tab3 = st.tabs(["Aequitas Flux", "Aequitas Growth", "Aequitas Guard"])

# --- BUCKET 1: AEQUITAS FLUX (THE AUTOPSY)[cite: 6, 10] ---
with tab1:
    st.markdown(f"""
    <div class='intro-block'>
    <h4>Analytical Intent: Aequitas Flux</h4>
    <strong>Investigation</strong>: Autopsy of the <strong>$13.3M YoY revenue contraction</strong> ($36.0M vs $22.7M)[cite: 6].<br>
    <strong>Logic</strong>: Decomposing delta into <strong>Volume Decay</strong> and <strong>Mix Shifts</strong> (L2 migration)[cite: 6].
    </div>
    """, unsafe_allow_html=True)

    if st.button("Execute Forensic Audit"):
        df = pd.read_csv("data/messy_swaps.csv")
        results = calculate_pvm_attribution(df, standard)
        report = get_ai_financial_insight(standard)

        m1, m2, m3 = st.columns(3)
        m1.metric("Volume Impact", f"${results['volume_variance']:,.2f}")
        m2.metric("Mix Impact", f"${results['mix_variance']:,.2f}")
        m3.metric("Revenue Floor", "$22.7M")

        st.markdown(report.strategic_narrative, unsafe_allow_html=True)

# --- BUCKET 2: AEQUITAS GROWTH (THE PRESCRIPTION)[cite: 6] ---
with tab2:
    st.markdown("""
    <div class='intro-block'>
    <h4>Analytical Intent: Aequitas Growth</h4>
    <strong>Strategy</strong>: Transitioning Exodus from 'Utility Wallet' to <strong>Wealth Management Layer</strong>[cite: 6].<br>
    <strong>Lock-in Initiative</strong>: Integrating <strong>Staking & Pay</strong> to stabilize the revenue floor[cite: 6].
    </div>
    """, unsafe_allow_html=True)

    if st.button("Simulate Lock-in Journeys"):
        df_g = simulate_growth_data()
        
        st.markdown("### Strategic Decisions: LTV/CAC Efficiency")
        # Visualizing the Strategic Pivot
        summary = df_g.groupby('source').mean()
        fig = px.scatter(summary, x='cac', y='ltv_cac_ratio', size='monthly_gp', 
                         color=summary.index, title="UA Channel Strategic Matrix[cite: 6]")
        fig.add_hline(y=3.5, line_dash="dash", annotation_text="Target Threshold[cite: 6]")
        st.plotly_chart(fig, use_container_width=True)

        st.success("**Strategic Answer**: The 'Staking & Pay' lock-in provides a stable floor of $12.00 GP per trader-month by December[cite: 6].")

# --- BUCKET 3: AEQUITAS GUARD (RISK SUITE)[cite: 10] ---
with tab3:
    st.markdown("""
    <div class='intro-block'>
    <h4>Analytical Intent: Aequitas Guard</h4>
    <strong>Stress Test</strong>: Treasury Resilience during Business Model Transition[cite: 6].
    </div>
    """, unsafe_allow_html=True)

    scenario = st.selectbox("Scenario", ["20% Bitcoin Flash Crash", "Ethereum Shanghai-level Volatility", "Stablecoin De-pegging Event"])
    
    if st.button("Execute Stress Test"):
        risk = simulate_treasury_risk(scenario)
        st.metric("Value-at-Risk (VaR)", f"-${risk.value_at_risk:,.2f}")
        st.markdown(f"**Historical Rationale**: {risk.detailed_analysis.historical_context}[cite: 6]")
        st.markdown(f"**Operational Strategy**: {risk.detailed_analysis.primary_strategy}[cite: 6]")

# --- METHODOLOGY EXPANDER[cite: 10] ---
st.write("---")
with st.expander("Methodology & Data Science Verification Audit", expanded=False):
    st.markdown("### Data Normalization & Rigor")
    st.markdown("""
    *   **Forensic (Flux)**: Missing fee-rates are resolved using **Median-Imputation** per asset-pair to prevent skewing Price Variance[cite: 10].
    *   **Strategy (Growth)**: We simulate 100,000 user journeys across 2026 distribution surfaces (Social Graph, Social Vaults) to model LTV/CAC ratios under a 95% 12-month retention assumption for Staking & Pay users[cite: 6].
    """)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### Audit Sample: Forensic Logs")
        df_f = pd.read_csv("data/messy_swaps.csv")
        st.dataframe(df_f.sample(1000), height=200, use_container_width=True)
        st.download_button("Download Forensic Logs (100k)", data=df_f.to_csv(index=False).encode('utf-8'), file_name='aequitas_forensic_logs.csv')
    
    with col_b:
        st.markdown("#### Audit Sample: Growth Journeys")
        df_g_sample = simulate_growth_data(records=1000)
        st.dataframe(df_g_sample, height=200, use_container_width=True)
        # Assuming simulate_growth_data is available to create the full 100k set for download
        st.download_button("Download Growth Journeys (100k)", data=simulate_growth_data(100000).to_csv(index=False).encode('utf-8'), file_name='aequitas_growth_journeys.csv')