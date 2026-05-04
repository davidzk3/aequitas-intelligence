import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Aequitas Intelligence Hub | Executive Briefing", 
    page_icon="📊", 
    layout="wide"
)

# --- PROFESSIONAL STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .report-title { font-size: 2.8rem; font-weight: 800; color: #1e293b; margin-bottom: 5px; }
    .report-subtitle { font-size: 1.2rem; color: #64748b; margin-bottom: 25px; }
    .section-header { border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-top: 30px; font-weight: 700; color: #0f172a; }
    .rationale-box { background-color: #ffffff; border-left: 5px solid #2563eb; padding: 20px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<div class='report-title'>Aequitas Intelligence Hub</div>", unsafe_allow_html=True)
st.markdown("<div class='report-subtitle'>Fiscal Year 2026 | Strategic Recovery & Growth Workspace</div>", unsafe_allow_html=True)
st.write("---")

# --- EXECUTIVE SUMMARY & EXTERNAL REFS ---
col_lh, col_rh = st.columns([2, 1])

with col_lh:
    st.markdown("### **I. Q1 Recovery Briefing**")
    st.markdown("""
    This terminal serves as the official analytical workspace for the Aequitas protocol. Following the identification of a 
    **37% YoY revenue contraction (c. $13.3M deficit)**, this environment provides the data-driven framework required 
    to transition the protocol from transactional 'Swap' utility to a **Primary Financial Residency** model.
    """)
    
    st.markdown("<div class='section-header'>II. Reference Financials & Strategic Documentation</div>", unsafe_allow_html=True)
    st.write("")
    
    # Official links for the reviewer
    st.markdown("""
    **External Reference Data (NYSE: EXOD)**
    *   📄 **[Exodus Investor Relations](https://www.exodus.com/investors/)**: Primary source for quarterly and annual financial reporting.
    *   📊 **[SEC Filings (Form 10-K/10-Q)](https://www.sec.gov/edgar/browse/?CIK=1821534)**: Audited financial statements used for the 2026 deficit baseline.
    """)

    # Arranged as a professional link directory
    st.markdown(f"""
    *   📘 **[Flux Revenue Autopsy (Forensic Reporting)](#)**: Detailed PVM attribution and fee-tier yield analysis.
    *   🎯 **[2026 GTM Blueprint (Strategic Framework)](#)**: Rational for the 'Wealth Management' pivot and capital allocation.
    *   🛡️ **[Treasury Guard Protocols (Risk Mandate)](#)**: Solvency stress-testing and delta-neutral hedging requirements.
    """)

with col_rh:
    st.markdown("### **Operational Integrity**")
    st.success("""
    **System Status: Active**
    *   **Population Depth**: 100,000 Records
    *   **Audit Trail**: IFRS/GAAP Compliant
    """)
    st.info("💡 Use the sidebar to navigate between Forensic (Flux) and Strategic (Growth) terminals.")

# --- PRODUCT RATIONALE ---
st.markdown("<div class='section-header'>III. Core Analytical Rationale</div>", unsafe_allow_html=True)
st.write("")

st.markdown("""
<div class='rationale-box'>
    <strong>Objective</strong>: To bridge the $13.3M revenue gap through structural decision-making rather than maintenance reporting.<br><br>
    The Aequitas Intelligence Suite was built to investigate the <strong>'Utility Decay'</strong> problem identified in the 
    accompanying revenue reporting. By isolating Price-Volume-Mix noise via the <strong>Flux Terminal</strong>, 
    we identified that L2 cannibalization is a structural shift, not a market cycle. The <strong>Growth Terminal</strong> 
    provides the 2026 roadmap for recovery, treating the product as a 'Wealth Management' layer where retention 
    is the primary lever for revenue stabilization.
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.write("---")
st.caption("Aequitas Digital Asset Intelligence")