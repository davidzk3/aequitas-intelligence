# Aequitas Intelligence
### On-Chain Financial Architecture & Risk Simulation

**Aequitas Intelligence** is a high-fidelity financial terminal designed to investigate on-chain treasury performance. It processes a population of **100,000 transaction logs**, normalizing messy decentralized data into structured executive insights using deterministic math and historical market precedents.

---

## 📈 Aequitas Flux: Revenue Attribution
Flux investigates the mathematical drivers behind protocol revenue fluctuations by isolating three distinct variables:

*   **Price Impact**: Measures changes in fee-tier yields and realized yield-per-swap.
*   **Volume Impact**: Isolates the effect of raw turnover velocity and TVL utilization.
*   **Mix Impact**: Identifies revenue shifts caused by changes in the asset-pair composition of total swaps.
*   **Accounting Standards**: Supports real-time revaluation between **IFRS (Crypto-Native)** and **GAAP (Conservative)** reporting policies.

---

## 🛡️ Aequitas Guard: Risk Simulation
Guard provides forward-looking **Value-at-Risk (VaR)** assessments. It stress-tests the 100,000-log population against historical "contagion" events to determine treasury solvency:

*   **Stablecoin De-pegging**: High-intensity simulation modeled after the May '22 (UST) and March '23 (USDC) collapses.
*   **Bitcoin Flash Crash**: Models systemic liquidation cascades based on May '21 and Nov '22 market volatility.
*   **Historical Rationale**: Every simulation includes the market context and data risk profile identified within the specific log population.
*   **Operational Protocols**: Generates specific hedging mandates, such as **Delta-Neutral Rebalancing** and **LSD-Spot Basis Hedging**, to mitigate identified risks.

---

## ⚙️ Data Science & Logic
The framework utilizes a separated architecture to ensure mathematical ground-truth and technical transparency:

*   **Deterministic Core**: All Price-Volume-Mix (PVM) math is executed via pure Python in a dedicated utility layer to ensure 100% calculation accuracy.
*   **Data Rigor**: Sparse or inconsistent logs are cleaned using **Median-Imputation** for missing fee rates and **IQR Outlier Detection** to eliminate oracle anomalies.
*   **Interpretive Layer**: Quantitative outputs are synthesized into professional financial narratives, providing a qualitative explanation of the mathematical findings.
*   **Data Sovereignty**: Includes a full-population audit tool allowing for the manual review and download of the entire 100,000 record set.