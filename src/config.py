import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
DB_PATH = os.path.join(BASE_DIR, "db", "ecommerce.db")
LOG_PATH = os.path.join(BASE_DIR, "logs", "ingestion.log")
