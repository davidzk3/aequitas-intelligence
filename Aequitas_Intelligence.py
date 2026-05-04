import streamlit as st

# --- PROFESSIONAL STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .report-title { font-size: 2.8rem; font-weight: 800; color: #1e293b; margin-bottom: 5px; }
    .report-subtitle { font-size: 1.2rem; color: #64748b; margin-bottom: 25px; }
    .section-header { border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-top: 30px; font-weight: 700; color: #0f172a; }
    .rationale-box { background-color: #ffffff; border-left: 5px solid #2563eb; padding: 20px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    /* Minimize spacing between navigation links */
    .stPageLink { margin-bottom: -15px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<div class='report-title'>Aequitas Intelligence Hub</div>", unsafe_allow_html=True)
st.markdown("<div class='report-subtitle'>Fiscal Year 2026 | Strategic Recovery & Growth Workspace</div>", unsafe_allow_html=True)
st.write("---")

# --- EXECUTIVE SUMMARY & EXTERNAL REFS ---
st.markdown("### **I. Q1 Recovery Briefing**")
st.markdown("""
This terminal serves as an analytical workspace for the Aequitas protocol. Following the identification of a 
**37% YoY revenue contraction (c. $13.3M deficit)**, this environment provides a data-driven framework
to transition the protocol from transactional 'Swap' utility to a **Primary Financial Residency** model.
""")

# --- SECTION II: EXTERNAL DATA ---
st.markdown("<div class='section-header'>II. External Reference Financials</div>", unsafe_allow_html=True)
st.write("")
st.markdown("""
**Public Reporting (NYSE: EXOD)**
*   📄 **[Exodus Investor Relations](https://www.exodus.com/investors/)**: Primary source for quarterly and annual financial reporting.
*   📊 **[SEC Filings (Form 10-K/10-Q)](https://www.sec.gov/edgar/browse/?CIK=1821534)**: Audited financial statements used for the 2026 deficit baseline.
""")

# --- SECTION III: INTERNAL MODULES ---
st.markdown("<div class='section-header'>III. Analytical Workspaces & Modules</div>", unsafe_allow_html=True)
st.write("")

# Updated path to match your actual filename: 03_risk_terminal.py
st.page_link("pages/01_flux_terminal.py", label="Flux Revenue Autopsy (Forensic Reporting): Detailed PVM attribution and fee-tier yield analysis.", icon="📘")
st.page_link("pages/02_growth_strategy.py", label="2026 GTM Blueprint (Strategic Framework): Rationale for the 'Wealth Management' pivot and capital allocation.", icon="🎯")
st.page_link("pages/03_risk_terminal.py", label="Treasury Guard Protocols (Risk Mandate): Solvency stress-testing and delta-neutral hedging requirements.", icon="🛡️")

st.write("")
st.info("💡 **Navigation Note:** Use the sidebar or the clickable modules above to switch between terminals.")

# --- PRODUCT RATIONALE ---
st.markdown("<div class='section-header'>IV. Core Analytical Rationale</div>", unsafe_allow_html=True)
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