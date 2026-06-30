from sqlalchemy import create_engine, text

# 1. Define your database file path
db_path = "bluestock_mf.db"

# 2. CREATE THE ENGINE FIRST (This fixes your NameError!)
engine = create_engine(f"sqlite:///{db_path}")

# 3. Your SQL table creation statements string
schema_sql = """
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_name TEXT NOT NULL,
    category TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_id TEXT PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    day_of_week TEXT
);

CREATE TABLE IF NOT EXISTS fact_nav (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date_id TEXT,
    nav REAL CHECK(nav > 0),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date_id TEXT,
    transaction_type TEXT CHECK(transaction_type IN ('SIP', 'Lumpsum', 'Redemption')),
    amount REAL CHECK(amount > 0),
    kyc_status TEXT CHECK(kyc_status IN ('KYC Validated', 'KYC Registered', 'KYC On-Hold', 'KYC Rejected')),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS fact_performance (
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    return_1y REAL,
    return_3y REAL,
    return_5y REAL,
    expense_ratio REAL CHECK(expense_ratio >= 0.1 AND expense_ratio <= 2.5),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);
"""

# 4. Now you can safely use engine.connect()
print("Initializing Database Schema...")
with engine.connect() as connection:
    # Split by semicolon to run statements one by one
    statements = [stmt.strip() for stmt in schema_sql.split(";") if stmt.strip()]
    
    for statement in statements:
        connection.execute(text(statement))
        
    print("Database tables created successfully with constraints!")