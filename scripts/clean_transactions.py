import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Standardize transaction types
mapping = {
    'sip': 'SIP',
    'lumpsum': 'Lumpsum',
    'redemption': 'Redemption'
}

df['transaction_type'] = (
    df['transaction_type']
    .str.lower()
    .map(mapping)
)

# Dates
df['transaction_date'] = pd.to_datetime(
    df['transaction_date']
)

# Positive amount only
df = df[df['amount_inr'] > 0]

# KYC validation
valid_kyc = ['Verified', 'Pending', 'Rejected']

df['kyc_status_valid'] = (
    df['kyc_status']
    .isin(valid_kyc)
)

print(df['kyc_status_valid'].value_counts())

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions Cleaned")