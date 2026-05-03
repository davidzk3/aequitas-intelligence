import pandas as pd

def calculate_pvm_attribution(df, standard="IFRS (Crypto-Native)"):
    """
    Deterministic Price-Volume-Mix (PVM) variance attribution logic.
    Calculates the impact of fee-tier changes, turnover volume, and asset composition.
    """
    # Define populations for variance analysis (80/20 split for comparative delta)
    split_idx = int(len(df) * 0.8)
    base, curr = df.iloc[:split_idx], df.iloc[split_idx:]
    
    # Apply standard-specific accounting logic
    # GAAP applies a 2.5% conservative provision to price-driven fee recognition
    adj = 0.975 if "GAAP" in standard else 1.0
    
    # Core PVM Formulas
    vol_impact = (curr['volume_usd'].sum() - base['volume_usd'].sum()) * base['fee_rate'].mean()
    price_impact = (curr['fee_rate'].mean() - base['fee_rate'].mean()) * curr['volume_usd'].sum() * adj
    
    total_rev_delta = (curr['revenue'].sum() * adj) - base['revenue'].sum()
    mix_impact = total_rev_delta - (vol_impact + price_impact)
    
    return {
        "price_variance": price_impact,
        "volume_variance": vol_impact,
        "mix_variance": mix_impact,
        "total_delta": total_rev_delta
    }