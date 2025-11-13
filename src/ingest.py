import sqlite3
import pandas as pd
import logging
import os
from config import DATA_DIR, DB_PATH, LOG_PATH

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

TABLES = {
    "customers": ["customer_id", "name", "email", "city", "signup_date"],
    "products": ["product_id", "name", "category", "price"],
    "orders": ["order_id", "customer_id", "order_date", "total_amount"],
    "order_items": ["item_id", "order_id", "product_id", "quantity", "item_price"],
    "payments": ["payment_id", "order_id", "method", "status", "payment_date"]
}

def ingest():
    conn = sqlite3.connect(DB_PATH)

    for table in TABLES.keys():
        csv_path = os.path.join(DATA_DIR, f"{table}.csv")
        df = pd.read_csv(csv_path)
        df.to_sql(table, conn, if_exists="replace", index=False)
        logging.info(f"{table}: {len(df)} rows ingested.")

    conn.close()
    print("Ingestion complete. Check logs/ingestion.log.")

if __name__ == "__main__":
    ingest()
