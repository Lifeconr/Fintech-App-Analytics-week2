import pandas as pd

df = pd.read_csv("raw_reviews.csv")

# Remove duplicates
df.drop_duplicates(subset=["review", "bank"], inplace=True)

# Drop missing values
df.dropna(subset=["review", "rating", "date"], inplace=True)

# Format date
df["date"] = pd.to_datetime(df["date"]).dt.strftime('%Y-%m-%d')

# Save clean version
df.to_csv("clean_reviews.csv", index=False)
print("Preprocessing complete. Clean data saved to clean_reviews.csv")
