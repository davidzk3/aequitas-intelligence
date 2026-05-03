import pandas as pd
import numpy as np

def simulate_growth_data(records=100000):
    # Mapping for concise (Chart) vs Elaborate (Table)
    channel_map = {
        'Embedded Social': 'Embedded Social (e.g. Farcaster/Lens)',
        'AI Search & Intent': 'AI Search & Intent (e.g. Perplexity/SearchGPT)',
        'Targeted Growth': 'On-Chain Targeted Growth (e.g. Safary/Spindl)',
        'Staking Vaults': 'Creator Staking Vaults (e.g. Social/Copy-trading)'
    }
    
    short_names = list(channel_map.keys())
    sources = np.random.choice(short_names, records, p=[0.30, 0.20, 0.25, 0.25])
    
    data = []
    for s in sources:
        noise = np.random.uniform(0.98, 1.02)
        
        # Logic remains deterministic based on short keys
        if s == 'Embedded Social':
            cac, ret_rate, gp_month = 20, 0.85, 11
        elif s == 'Staking Vaults':
            cac, ret_rate, gp_month = 28, 0.92, 13
        elif s == 'Targeted Growth':
            cac, ret_rate, gp_month = 50, 0.95, 15
        else: # AI Search & Intent
            cac, ret_rate, gp_month = 15, 0.75, 9

        data.append({
            'Channel': s, # Concise
            'Full_Channel_Name': channel_map[s], # Elaborate
            'CAC': cac * noise,
            'Monthly_GP': gp_month * noise,
            'Retention_12M': ret_rate,
            'Is_Locked_In': (ret_rate > 0.90) 
        })
    
    df = pd.DataFrame(data)
    df['LTV'] = (df['Monthly_GP'] * (1 / (1 - df['Retention_12M']))).round(0)
    df['LTV_CAC_Ratio'] = (df['LTV'] / df['CAC']).round(2)
    df['Payback_Months'] = (df['CAC'] / df['Monthly_GP']).round(1)
    
    return df

def calculate_recovery_curve(summary_df, target_deficit=13300000):
    """Calculates the 12-month recovery trend based on cohort decay."""
    months = np.arange(1, 13)
    data = []
    
    # We assume a fixed cohort size of 100k users split across 4 channels
    cohort_size = 100000 
    
    for m in months:
        monthly_revenue = 0
        for _, row in summary_df.iterrows():
            # Monthly GP * (Users per channel) * (Retention decayed over time)
            channel_share = cohort_size / 4
            decayed_retention = row['Retention_12M'] ** (m / 12)
            monthly_revenue += (row['Monthly_GP'] * channel_share) * decayed_retention
        
        cumulative = sum([d['Monthly_Revenue'] for d in data]) + monthly_revenue if data else monthly_revenue
        
        data.append({
            "Month": f"Month {m}", 
            "Monthly_Revenue": round(monthly_revenue, -3), # Round to nearest thousand
            "Cumulative_Recovery": round(cumulative, -3)   # Round to nearest thousand
        })
        
    return pd.DataFrame(data)