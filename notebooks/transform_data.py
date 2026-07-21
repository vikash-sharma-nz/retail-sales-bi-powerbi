# transform_data.py
import os
import pandas as pd

INPUT_FILE = "extracted_online_retail.csv"
OUTPUT_FILE = "transformed_online_retail.csv"

def main():
    print("Running from:", os.getcwd())

    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError("Run extract_data.py first (missing extracted_online_retail.csv).")

    df = pd.read_csv(INPUT_FILE)

    # Normalize headers
    df.columns = [c.strip().replace("\ufeff", "") for c in df.columns]

    # Ensure required columns exist
    required = ["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise KeyError(f"Missing columns: {missing}\nFound: {list(df.columns)}")

    # Convert types
    df["InvoiceNo"] = df["InvoiceNo"].astype(str).str.strip()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")

    # Remove cancelled invoices (optional but common in Online Retail)
    df = df[~df["InvoiceNo"].str.startswith("C", na=False)]

    # Remove invalid rows
    df = df.dropna(subset=["InvoiceDate", "Quantity", "UnitPrice"])
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # Add calculated fields
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month

    # Add transaction_id
    df = df.reset_index(drop=True)
    df.insert(0, "transaction_id", df.index + 1)

    # Keep clean order
    cols = [
        "transaction_id", "InvoiceNo", "StockCode", "Description",
        "Quantity", "InvoiceDate", "UnitPrice", "Revenue",
        "CustomerID", "Country", "Year", "Month"
    ]
    df = df[cols]

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Transform complete: {OUTPUT_FILE} rows={len(df)}")

if __name__ == "__main__":
    main()