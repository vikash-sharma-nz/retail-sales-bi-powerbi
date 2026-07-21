import pandas as pd

# Load full dataset
df = pd.read_csv("online_retail_full.csv")

# Remove cancelled transactions (negative quantity)
df = df[df["Quantity"] > 0]

# Drop rows without CustomerID
df = df.dropna(subset=["CustomerID"])

# Take a random sample of 10000 rows
sample_df = df.sample(n=10000, random_state=42)

# Save sample
sample_df.to_csv("online_retail_sample.csv", index=False)

print("Sample dataset created:", len(sample_df))