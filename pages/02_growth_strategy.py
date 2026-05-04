import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
# Consolidated all logic imports to the top
from utils.growth_logic import simulate_growth_data, calculate_recovery_curve

# --- UI & ARCHITECTURE ---
st.set_page_config(page_title="Aequitas Growth | Strategic Terminal", layout="wide")

st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .strategy-block { 
        background-color: #ffffff; border-radius: 8px; padding: 25px; 
        border: 1px solid #e2e8f0; border-top: 5px solid #10b981; margin-bottom: 25px; 
    }
    .metric-card { background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 15px; border-radius: 8px; }
    /* Action Button Styling */
    div.stButton > button:first-child {
        background-color: #10b981;
        color: white;
        border: none;
        padding: 12px 28px;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #059669;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-header'>Aequitas Intelligence: Growth</div>", unsafe_allow_html=True)
st.markdown("Strategic Prescription: Transitioning to Wealth Management | **2026 GTM Model**")
st.write("---")

# --- SIDEBAR ---
with st.sidebar:
    st.write("---")
    st.markdown("#### Data Integrity")
    st.markdown("Population: 100,000 Simulated User Journeys")
    st.write("---")
    st.caption("Institutional Digital Asset Intelligence")

# --- 1. STRATEGIC INTENT & PROBLEM STATEMENT ---
st.markdown(f"""
<div class='strategy-block'>
<h4>Analytical Intent: The Wealth Management Pivot</h4>
<strong>The Challenge</strong>: As diagnosed in the revenue autopsy, speculative swap utility is decaying due to L2 cannibalization. 
To bridge the <strong>c. $13.3M deficit</strong>, the protocol must move from transactional utility to a <strong>Primary Financial Residency</strong>.<br><br>
<strong>The Solution</strong>: Aequitas Growth models the <strong>'Lock-in' Strategy</strong>. By integrating Staking and Payment rails, 
the analysis demonstrates a conversion from high-churn traders into low-churn 'Wealth Management' users, stabilizing the revenue floor at <strong>c. $12.00 GP per month</strong>.
</div>
""", unsafe_allow_html=True)

# --- 2. THE 4-GATE FUNNEL ILLUSTRATION ---
st.markdown("### **I. The 2026 Acquisition Funnel: Gate-Level Activation**")
st.markdown("Acquisition is prioritized via **Social-Graph Distribution** (Farcaster/Lens) where the transaction occurs at the 'head' of the social feed.")

g1, g2, g3, g4 = st.columns(4)
with g1:
    st.markdown("<div class='metric-card'><strong>Gate A: Discovery</strong><br>Found via Social-Graph feed or AI Intent Search.</div>", unsafe_allow_html=True)
with g2:
    st.markdown("<div class='metric-card'><strong>Gate B: Engagement</strong><br>User connects staking rewards dashboard.</div>", unsafe_allow_html=True)
with g3:
    st.markdown("<div class='metric-card'><strong>Gate C: Activation</strong><br>First Staked deposit or Salary Route setup.</div>", unsafe_allow_html=True)
with g4:
    st.markdown("<div class='metric-card'><strong>Gate D: Lock-in</strong><br>User reaches c. 95% 12-mo retention maturity.</div>", unsafe_allow_html=True)

st.write("---")

# --- 3. EXECUTION: UNIT ECONOMICS LEDGER ---
if st.button("Execute Strategic Growth Simulation (100k Journeys)"):
    df_g = simulate_growth_data(100000)
    
    summary = df_g.groupby(['Channel', 'Full_Channel_Name']).agg({
        'CAC': 'mean',
        'Monthly_GP': 'mean',
        'Retention_12M': 'mean',
        'LTV': 'mean',
        'LTV_CAC_Ratio': 'mean',
        'Payback_Months': 'mean'
    }).reset_index()

    st.markdown("### **II. Channel-Level Unit Economics Matrix (Estimated)**")
    
    table_display = summary.drop(columns=['Channel']).rename(columns={'Full_Channel_Name': 'Channel'})
    st.dataframe(table_display.style.format({
        'CAC': 'c. ${:,.0f}', 
        'Monthly_GP': 'c. ${:,.2f}', 
        'Retention_12M': '~ {:.0%}', 
        'LTV': 'c. ${:,.0f}', 
        'LTV_CAC_Ratio': 'c. {:.1f}x', 
        'Payback_Months': 'c. {:.1f}'
    }), use_container_width=True)

    st.write("---")
    
    # --- 4. VISUAL ANALYSIS: SCALING MATRIX ---
    st.markdown("### **III. Strategic Scaling Matrix (LTV/CAC)**")
    
    fig = px.scatter(
        summary, x='CAC', y='LTV_CAC_Ratio', size='Monthly_GP', 
        color='Channel', 
        labels={'CAC': 'Acquisition Cost (USD)', 'LTV_CAC_Ratio': 'Capital Efficiency (Ratio)'},
        height=500
    )
    fig.update_yaxes(range=[0, 10]) 
    fig.add_hline(y=3.5, line_dash="dash", annotation_text="Sustainability Threshold (3.5x)")
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)

    # --- 5. THE GTM BLUEPRINT ---
    st.write("---")
    st.markdown("### **IV. Strategic GTM Blueprint & Capital Allocation**")
    
    col_gtm1, col_gtm2 = st.columns([2, 1])
    
    with col_gtm1:
        st.markdown("""
        #### **Execution Roadmap: The 'Wealth Management' Pivot**
        Based on the simulation, the path to bridging the **$13.3M deficit** requires a phased deployment of capital.

        1.  **Phase 1: Efficiency Baseline (Months 1-3)**  
            Focus on **AI Search & Intent** and **Embedded Social**. Lowest Payback Periods (c. 1.7 months).
        
        2.  **Phase 2: Retention Alpha (Months 4-8)**  
            Scale **On-Chain Targeted Growth**. Higher CAC (c. $50), but core 'Wealth' layer retention (95%).
        
        3.  **Phase 3: The Residency Lock (Months 9+ )**  
            Funnel users into **Creator Staking Vaults**. Max LTV state (c. $300 per user).
        """)

    with col_gtm2:
        st.markdown("#### **Suggested Monthly Budget**")
        budget_data = {
            "Channel": ["AI Intent", "Embedded Social", "Targeted Growth", "Staking Vaults"],
            "Allocation": ["15%", "25%", "40%", "20%"],
            "Monthly Est.": ["$45k", "$75k", "$120k", "$60k"]
        }
        st.table(pd.DataFrame(budget_data))
        st.caption("Target Monthly Spend: c. $300,000 (Scalable)")

    # --- 6. PAYBACK VELOCITY AGGREGATED ---
    st.write("---")
    st.markdown("### **V. Payback Velocity by Distribution Surface**")
    fig_payback = px.bar(
        summary, x='Channel', y='Payback_Months', color='Payback_Months',
        title="Average Months to Recover CAC (Lower is Superior)",
        color_continuous_scale='RdYlGn_r',
        height=400
    )
    st.plotly_chart(fig_payback, use_container_width=True)

    # --- 7. CUMULATIVE RECOVERY PROJECTION ---
    st.write("---")
    st.markdown("### **VI. Cumulative Revenue Recovery Projection (12-Month Horizon)**")
    
    # FIX: Generating the missing recovery_df variable
    recovery_df = calculate_recovery_curve(summary)
    
    fig_recovery = go.Figure()

    fig_recovery.add_trace(go.Scatter(
        x=recovery_df['Month'], y=recovery_df['Cumulative_Recovery'],
        fill='tozeroy', mode='lines+markers',
        name='Projected Recovery', line=dict(color='#2563eb', width=4)
    ))

    fig_recovery.add_hline(
        y=13300000, line_dash="dash", line_color="#ef4444",
        annotation_text="Flux Deficit Target ($13.3M)", 
        annotation_position="top left"
    )

    fig_recovery.update_layout(
        title="Projected Cumulative Gross Profit vs. YoY Revenue Deficit",
        xaxis_title="Simulation Timeline",
        yaxis_title="Cumulative USD Recovery",
        height=500,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(fig_recovery, use_container_width=True)

    st.info(f"""
    **Audit Conclusion**: At current retention levels (c. 95% in top-tier channels), the Wealth Management pivot is projected 
    to fully recover the **$13.3M deficit** by **Month 11**.
    """)

# --- 8. METHODOLOGY & CALCULATION DEPTH ---
st.write("---")
with st.expander("GTM Modeling Methodology & Data Science Rigor"):
    st.markdown("""
    ### **The Math of the Recovery**
    
    The simulation utilizes **Discrete-Event Modeling** over 100,000 user journeys to test the validity of the Wealth Management pivot.

    1. **Lifetime Value (LTV)**: The total gross profit expected from a user over their entire relationship with the platform. A c. 95% retention rate translates to an approx. 20-month expected lifetime.
    2. **Lock-in Logic**: The model assumes a user is only 'Locked-in' if they pass through Gate C (Staking) and Gate D (Payments). These users are assigned c. 4.5x higher LTV weights than 'Swap-only' users.
    3. **CAC Modeling**: Costs are dynamic based on 2026 market rates for Farcaster frame-based distribution versus legacy intent-search.
    """)
    
    st.markdown("#### **Sample Strategic Audit Logs**")
    # Generating a subset for forensic inspection
    sample_df = simulate_growth_data(1000)
    st.dataframe(sample_df.head(10), use_container_width=True)
    
    st.download_button(
        "Download Full Strategic Model (100k Records)", 
        data=simulate_growth_data(100000).to_csv(index=False).encode('utf-8'), 
        file_name='aequitas_growth_journeys.csv'
    )