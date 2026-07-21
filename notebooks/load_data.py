# load_data.py
import os
import sqlite3
import pandas as pd

INPUT_FILE = "transformed_online_retail.csv"
DB_FILE = "retail_dw.db"
TABLE_NAME = "fact_transactions"

def main():
    print("Running from:", os.getcwd())

    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError("Run transform_data.py first (missing transformed_online_retail.csv).")

    df = pd.read_csv(INPUT_FILE)

    conn = sqlite3.connect(DB_FILE)
    try:
        df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

        # Verify load
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
        count = cur.fetchone()[0]

        print(f"✅ Load complete: {DB_FILE}")
        print(f"✅ Table: {TABLE_NAME}")
        print(f"✅ Rows loaded: {count}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()