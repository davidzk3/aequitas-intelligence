import pandas as pd
import numpy as np

def simulate_growth_data(records=100000):
    """
    Models the transition of Exodus into a Wealth Management Layer.
    Simulates Social-Graph Acquisition & Lock-in logic.
    """
    channels = [
        'Social Graph (Farcaster/Lens)', 
        'Intent-Based AI (Perplexity)', 
        'On-Chain Attribution (Safary)', 
        'Social Vaults (Creators)'
    ]
    
    # Weighting based on 2026 distribution surfaces
    sources = np.random.choice(channels, records, p=[0.30, 0.20, 0.25, 0.25])
    
    data = []
    for s in sources:
        if s == 'Social Graph (Farcaster/Lens)':
            # Low friction 'First-Trade' completion via headless transactions
            cac, ret_rate, gp_month = np.random.uniform(15, 25), 0.85, np.random.uniform(9, 13)
        elif s == 'Social Vaults (Creators)':
            # Community-driven staking pools and salary-routing
            cac, ret_rate, gp_month = np.random.uniform(20, 35), 0.92, np.random.uniform(10, 15)
        elif s == 'On-Chain Attribution (Safary)':
            # Targeting users with specific on-chain behaviors[cite: 6]
            cac, ret_rate, gp_month = np.random.uniform(40, 60), 0.95, np.random.uniform(12, 18)
        else: # Intent AI
            # Yield-seeking intent via AI aggregators[cite: 6]
            cac, ret_rate, gp_month = np.random.uniform(10, 20), 0.75, np.random.uniform(7, 11)

        data.append({
            'source': s,
            'cac': cac,
            'monthly_gp': gp_month,
            'retention_12m': ret_rate,
            'is_locked_in': (ret_rate > 0.90) # Lock-in requires Staking + Pay[cite: 6]
        })
    
    df = pd.DataFrame(data)
    # LTV = GP per month * expected lifetime (1 / churn)[cite: 6]
    df['ltv'] = df['monthly_gp'] * (1 / (1 - df['retention_12m']))
    df['ltv_cac_ratio'] = df['ltv'] / df['cac']
    return df