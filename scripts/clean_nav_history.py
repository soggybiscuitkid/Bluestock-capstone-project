import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Parse dates
df['date'] = pd.to_datetime(df['date'])

# Sort
df = df.sort_values(['amfi_code', 'date'])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV within each fund
df['nav'] = df.groupby('amfi_code')['nav'].ffill()

# Remove invalid NAV
df = df[df['nav'] > 0]

print(df.isnull().sum())

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned")