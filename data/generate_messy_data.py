import pandas as pd
import numpy as np
import uuid
from datetime import datetime, timedelta

def generate_institutional_data(n_rows=100000):
    """Generates high-volume transaction data for performance validation."""
    pairs = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'WETH/USDT', 'USDC/USDT', 'USDC.e/USDT']
    data = []
    
    start_date = datetime.now() - timedelta(days=30)
    
    # Vectorize row generation for speed
    pairs_sample = np.random.choice(pairs, n_rows)
    vols = np.random.uniform(500, 75000, n_rows)
    fees = np.random.uniform(0.001, 0.004, n_rows)
    
    df = pd.DataFrame({
        'tx_id': [str(uuid.uuid4())[:18] for _ in range(n_rows)],
        'pair': pairs_sample,
        'volume_usd': vols,
        'fee_rate': fees,
        'timestamp': [(start_date + timedelta(seconds=i*25)).isoformat() for i in range(n_rows)]
    })
    
    # Introduce messy data (5% nulls)
    df.loc[df.sample(frac=0.05).index, 'fee_rate'] = np.nan
    
    df.to_csv("data/messy_swaps.csv", index=False)
    print(f"✅ Generated {n_rows} logs for institutional stress-testing.")

if __name__ == "__main__":
    generate_institutional_data()