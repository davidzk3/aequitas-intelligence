def calculate_pvm_math(df):
    """
    Pure Python PVM calculation to ensure ground-truth accuracy.
    """
    # Split data to find the 'Variance' (80/20 split for demo purposes)
    split = int(len(df) * 0.8)
    base, curr = df.iloc[:split], df.iloc[split:]
    
    # Calculate Impact
    vol_impact = (curr['volume_usd'].sum() - base['volume_usd'].sum()) * base['fee_rate'].mean()
    price_impact = (curr['fee_rate'].mean() - base['fee_rate'].mean()) * curr['volume_usd'].sum()
    
    return price_impact, vol_impact