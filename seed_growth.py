import os
import pandas as pd
from utils.growth_logic import simulate_growth_data

# 1. Ensure the data directory exists
if not os.path.exists('data'):
    os.makedirs('data')
    print("Created 'data/' directory.")

# 2. Generate the 100k population for the Wealth Management model
print("Generating 100,000 Strategic Growth Journeys...")
# This logic uses the Social-Graph and Lock-in metrics we defined
df = simulate_growth_data(100000)

# 3. Save to CSV for the Methodology expander
df.to_csv('data/growth_journeys.csv', index=False)
print("SUCCESS: data/growth_journeys.csv generated.")