import sqlite3
import pandas as pd
from tabulate import tabulate
from config import DB_PATH

def run():
    with open("sql/master_join.sql") as file:
        query = file.read()

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    
    print(tabulate(df, headers="keys", tablefmt="pretty"))
    conn.close()

if __name__ == "__main__":
    run()
