from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=330)

# Load keywords from file
keywords = [k.strip() for k in open('keywords.txt').read().splitlines() if k.strip()]

# Time range (last 5 years)
timeframe = '2019-12-01 2024-12-01'

# Build request for India
pytrends.build_payload(keywords, timeframe=timeframe, geo='IN')

# Fetch weekly interest data
df = pytrends.interest_over_time()

# Remove irrelevant column
if 'isPartial' in df.columns:
    df = df.drop(columns=['isPartial'])

# Save output
df.to_csv('google_trends_national.csv')
print("Saved google_trends_national.csv! Rows:", df.shape[0])
