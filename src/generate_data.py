import pandas as pd
import numpy as np
from faker import Faker
import os
from config import DATA_DIR

fake = Faker()
np.random.seed(42)

def generate_customers(n=25):
    return pd.DataFrame({
        "customer_id": range(1, n+1),
        "name": [fake.name() for _ in range(n)],
        "email": [fake.email() for _ in range(n)],
        "city": [fake.city() for _ in range(n)],
        "signup_date": [fake.date_between(start_date="-2y", end_date="today") for _ in range(n)]
    })

def generate_products(n=25):
    categories = ["Electronics", "Fashion", "Home", "Sports", "Beauty"]
    return pd.DataFrame({
        "product_id": range(1, n+1),
        "name": [fake.word().title() for _ in range(n)],
        "category": np.random.choice(categories, n),
        "price": np.random.uniform(10, 500, n).round(2)
    })

def generate_orders(customers, n=25):
    return pd.DataFrame({
        "order_id": range(1, n+1),
        "customer_id": np.random.choice(customers["customer_id"], n),
        "order_date": [fake.date_between(start_date="-1y", end_date="today") for _ in range(n)],
        "total_amount": np.random.uniform(20, 1000, n).round(2)
    })

def generate_order_items(orders, products):
    rows = []
    item_id = 1
    for _, order in orders.iterrows():
        for _ in range(np.random.randint(1, 4)):
            product = products.sample(1).iloc[0]
            rows.append([
                item_id,
                order["order_id"],
                product["product_id"],
                np.random.randint(1, 5),
                product["price"]
            ])
            item_id += 1
    return pd.DataFrame(rows, columns=["item_id", "order_id", "product_id", "quantity", "item_price"])

def generate_payments(orders):
    methods = ["Credit Card", "UPI", "NetBanking", "Wallet"]
    statuses = ["Success", "Failed", "Pending"]
    return pd.DataFrame({
        "payment_id": range(1, len(orders)+1),
        "order_id": orders["order_id"],
        "method": np.random.choice(methods, len(orders)),
        "status": np.random.choice(statuses, len(orders)),
        "payment_date": orders["order_date"]
    })

def save(df, filename):
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(os.path.join(DATA_DIR, filename), index=False)

def main():
    customers = generate_customers()
    products = generate_products()
    orders = generate_orders(customers)
    order_items = generate_order_items(orders, products)
    payments = generate_payments(orders)

    save(customers, "customers.csv")
    save(products, "products.csv")
    save(orders, "orders.csv")
    save(order_items, "order_items.csv")
    save(payments, "payments.csv")

    print("Synthetic dataset generated successfully.")

if __name__ == "__main__":
    main()
