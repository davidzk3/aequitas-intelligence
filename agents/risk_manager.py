from pydantic import BaseModel
from typing import List

class RiskAnalysis(BaseModel):
    historical_context: str
    scenario_driver: str
    impact_logic: str
    liquidity_threat: str
    primary_strategy: str
    execution_options: List[str]

class RiskReport(BaseModel):
    value_at_risk: float
    risk_score: int
    action_required: bool
    detailed_analysis: RiskAnalysis

def simulate_treasury_risk(scenario: str) -> RiskReport:
    """Simulates institutional risk profiles based on historical market precedents."""
    
    scenarios = {
        "20% Bitcoin Flash Crash": RiskReport(
            value_at_risk=1250000.00,
            risk_score=88,
            action_required=True,
            detailed_analysis=RiskAnalysis(
                historical_context="Referencing the May 2021 and November 2022 market events where BTC volatility triggered systemic liquidations across DeFi lending protocols.",
                scenario_driver="Rapid asset devaluation leads to a spike in correlation across all treasury holdings, neutralizing traditional diversification benefits.",
                impact_logic="A 20% drawdown in BTC spot price historically corresponds with a 35% contraction in swap turnover and a widening of liquidity spreads by 40-60 bps.",
                liquidity_threat="Inventory imbalance risk; the treasury may become 'long' on depreciating assets while liquidity for stable-pair exits evaporates.",
                primary_strategy="Delta-Neutral Portfolio Rebalancing",
                execution_options=[
                    "Hedge: Deploy OTM Put options for BTC/USD at 15% delta to protect the principal.",
                    "Liquidity: Shift 20% of active LP positions into isolated stablecoin pools to reduce impermanent loss exposure.",
                    "Collateral: Increase maintenance margin on all treasury-backed loans by a factor of 1.5x."
                ]
            )
        ),
        "Ethereum Shanghai-level Volatility": RiskReport(
            value_at_risk=480000.00,
            risk_score=62,
            action_required=True,
            detailed_analysis=RiskAnalysis(
                historical_context="Based on the April 2023 'Shapella' upgrade, which introduced unstaking liquidity, creating localized imbalances between ETH and Liquid Staking Derivatives (LSDs).",
                scenario_driver="Unstaking queue congestion creates a temporary arbitrage window, stressing the parity between staked-ETH and spot-ETH.",
                impact_logic="Divergence in LSD pegs (e.g., stETH/ETH) forces the protocol to recognize unrealized losses on treasury-held staked assets.",
                liquidity_threat="Peg-instability leads to automated liquidations in treasury-managed yield strategies.",
                primary_strategy="LSD-Spot Basis Hedging",
                execution_options=[
                    "Basis Trade: Short ETH futures against long LSD holdings to capture the spread convergence.",
                    "Inventory: Limit exposure to liquid-staking protocols to <15% of total ETH treasury reserves.",
                    "Arbitrage: Utilize internal liquidity to compress the LSD-spot discount back to within 10 bps."
                ]
            )
        ),
        "Stablecoin De-pegging Event": RiskReport(
            value_at_risk=4850000.00,
            risk_score=95,
            action_required=True,
            detailed_analysis=RiskAnalysis(
                historical_context="Modeled after the May 2022 UST collapse and the March 2023 USDC de-peg event (SVB contagion).",
                scenario_driver="A breach in the 1:1 parity of a core stablecoin primitive invalidates the accounting baseline for the entire protocol.",
                impact_logic="A 5% move off-peg triggers a 'Flight to Quality,' creating an immediate liquidity vacuum in swap pairs involving the affected asset.",
                liquidity_threat="Total insolvency if treasury reserves are concentrated in the de-pegged asset; slippage on exit routes exceeds 15% within minutes.",
                primary_strategy="Immediate Capital Preservation Protocol",
                execution_options=[
                    "Asset Rotation: Immediate exit into non-custodial hard assets (BTC/WBTC) or over-collateralized stables.",
                    "Lockdown: Pause all internal swap routing to the affected stablecoin to prevent 'dumping' into treasury liquidity.",
                    "Diversification: Re-establish reserves across a minimum of three distinct stablecoin issuers (Circle, Tether, Paxos)."
                ]
            )
        )
    }
    return scenarios.get(scenario)