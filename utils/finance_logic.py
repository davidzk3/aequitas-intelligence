import pandas as pd

def calculate_pvm_attribution(df, standard="IFRS (Crypto-Native)"):
    """
    Deterministic Price-Volume-Mix (PVM) variance attribution logic.
    Includes institutional rounding to provide credible "approximate" estimates[cite: 1, 4].
    Calculates the impact of fee-tier changes, turnover volume, and asset composition.
    """
    # Define populations for comparative delta (YoY baseline vs current)
    split_idx = int(len(df) * 0.8)
    base, curr = df.iloc[:split_idx], df.iloc[split_idx:]
    
    # GAAP applies a 2.5% conservative provision to price-driven fee recognition[cite: 2]
    adj = 0.975 if "GAAP" in standard else 1.0
    
    # PVM Calculation Logic
    # Vol Impact = (Current Volume - Base Volume) * Base Fee Rate
    vol_impact = (curr['volume_usd'].sum() - base['volume_usd'].sum()) * base['fee_rate'].mean()
    
    # Price Impact = (Current Rate - Base Rate) * Current Volume
    price_impact = (curr['fee_rate'].mean() - base['fee_rate'].mean()) * curr['volume_usd'].sum() * adj
    
    total_rev_delta = (curr['revenue'].sum() * adj) - base['revenue'].sum()
    
    # Mix Impact is the residual delta caused by asset/network migration
    mix_impact = total_rev_delta - (vol_impact + price_impact)
    
    # Institutional Rounding[cite: 4]
    # We round to the nearest $100 to avoid "to-the-penny" manipulation concerns.
    # This aligns the math with the "c." (Circa) reporting in the UI[cite: 4].
    return {
        "price_variance": round(price_impact, -2),
        "volume_variance": round(vol_impact, -2),
        "mix_variance": round(mix_impact, -2),
        "total_delta": round(total_rev_delta, -2)
    }