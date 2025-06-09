import pandas as pd
import oracledb
import os

# === Database connection ===
username = "SYS"
password = "senait.01"  # Your actual password
dsn = oracledb.makedsn("localhost", 1521, service_name="xepdb1")
connection = oracledb.connect(user=username, password=password, dsn=dsn, mode=oracledb.SYSDBA)
cursor = connection.cursor()

# === Load cleaned data ===
input_path = 'data/processed/sentiment_results.csv'
df = pd.read_csv(input_path)

# === Check required columns ===
required_columns = ['bank', 'review', 'rating', 'date', 'source', 'textblob_label', 'textblob_score']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")

# === Insert data into Oracle ===
inserted_count = 0
failed_banks = []  # To store failed bank IDs
for index, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO reviews (
                bank_id, review_text, rating, date_posted, source,
                sentiment_label, sentiment_score, themes
            ) VALUES (
                :1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8
            )
        """, (
            row['bank'],
            row['review'],
            int(row['rating']),
            row['date'],
            row['source'],
            row['textblob_label'],
            float(row['textblob_score']),
            row.get('themes', None)
        ))
        inserted_count += 1
    except oracledb.DatabaseError as e:
        if "ORA-02291" in str(e):
            failed_banks.append((index, row['bank']))
        print(f"Row {index} insert failed: {e}")

# === Commit and close ===
connection.commit()
cursor.close()
connection.close()

print(f"Inserted {inserted_count} out of {len(df)} reviews into Oracle database.")
if failed_banks:
    print("Failed bank IDs:", [bank for _, bank in failed_banks])