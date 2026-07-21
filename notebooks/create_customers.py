import pandas as pd

INPUT_FILE = "transformed_online_retail.csv"
OUTPUT_FILE = "customers_new.csv"

df = pd.read_csv(INPUT_FILE)

customers = (
    df[["CustomerID", "Country"]]
    .dropna(subset=["CustomerID"])
    .drop_duplicates()
    .sort_values("CustomerID")
)

customers.to_csv(OUTPUT_FILE, index=False)

print("customers_new.csv created with rows:", len(customers))