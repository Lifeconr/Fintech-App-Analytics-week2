import pandas as pd

# Load raw data
df = pd.read_csv("raw_reviews.csv")

# Validate required columns
required_columns = ["review", "bank", "rating", "date"]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

# Remove duplicates
df.drop_duplicates(subset=["review", "bank"], inplace=True)

# Drop missing values in required columns
df.dropna(subset=required_columns, inplace=True)

# Standardize bank IDs to uppercase and map to consistent values
bank_mapping = {"cbe": "CBE", "boa": "BOA", "dash": "DASH"}  # Add other variations as needed
df["bank"] = df["bank"].str.upper().map(lambda x: bank_mapping.get(x, x))

# Format date
df["date"] = pd.to_datetime(df["date"]).dt.strftime('%Y-%m-%d')

# Save clean version
df.to_csv("clean_reviews.csv", index=False)
print("Preprocessing complete. Clean data saved to clean_reviews.csv")