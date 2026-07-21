# extract_data.py
import os
import pandas as pd

INPUT_FILE = "online_retail_sample.csv"          # created by sample_data.py
OUTPUT_FILE = "extracted_online_retail.csv"      # optional staging file

def main():
    print("Running from:", os.getcwd())

    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(
            f"Cannot find {INPUT_FILE}. Make sure you ran sample_data.py and it exists in this folder."
        )

    df = pd.read_csv(INPUT_FILE)

    # Basic cleanup (safe)
    df.columns = [c.strip().replace("\ufeff", "") for c in df.columns]

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Extract complete: {OUTPUT_FILE} rows={len(df)}")

if __name__ == "__main__":
    main()