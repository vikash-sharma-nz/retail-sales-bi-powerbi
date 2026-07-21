import pandas as pd

INPUT_FILE = "transformed_online_retail.csv"
OUTPUT_FILE = "products_new.csv"

df = pd.read_csv(INPUT_FILE)

products = (
    df[["StockCode", "Description"]]
    .dropna(subset=["StockCode"])
    .drop_duplicates()
    .sort_values("StockCode")
)

products.to_csv(OUTPUT_FILE, index=False)

print("products_new.csv created with rows:", len(products))