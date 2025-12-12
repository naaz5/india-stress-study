import pandas as pd
import numpy as np

# Load the weekly trends data
df = pd.read_csv('google_trends_national.csv', parse_dates=['date'], index_col='date')

# Convert weekly data → monthly average
monthly = df.resample('M').mean()

# Normalize each keyword column (0 to 1 scale)
normed = (monthly - monthly.min()) / (monthly.max() - monthly.min())

# Create composite stress index (average of all keywords)
normed['stress_index'] = normed.mean(axis=1)

# Save output
normed[['stress_index']].to_csv('stress_index_monthly.csv')

print("Saved stress_index_monthly.csv! Rows:", normed.shape[0])
