import os
from typing import Optional

import numpy as np
import pandas as pd
from faker import Faker

from config import DATA_DIR


class GenerateData:
    """Generate synthetic ecommerce datasets and save them to CSV files.

    Methods mirror the previous module-level functions but are instance methods
    so users can configure `data_dir` and `seed` per instance.
    """

    def __init__(self, data_dir: Optional[str] = None, seed: int = 42):
        self.data_dir = data_dir or DATA_DIR
        self.fake = Faker()
        self.seed = seed
        np.random.seed(self.seed)

    def generate_customers(self, n: int = 25) -> pd.DataFrame:
        return pd.DataFrame({
            "customer_id": range(1, n + 1),
            "name": [self.fake.name() for _ in range(n)],
            "email": [self.fake.email() for _ in range(n)],
            "city": [self.fake.city() for _ in range(n)],
            "signup_date": [self.fake.date_between(start_date="-2y", end_date="today") for _ in range(n)],
        })

    def generate_products(self, n: int = 25) -> pd.DataFrame:
        categories = ["Electronics", "Fashion", "Home", "Sports", "Beauty"]
        return pd.DataFrame({
            "product_id": range(1, n + 1),
            "name": [self.fake.word().title() for _ in range(n)],
            "category": np.random.choice(categories, n),
            "price": np.random.uniform(10, 500, n).round(2),
        })

    def generate_orders(self, customers: pd.DataFrame, n: int = 25) -> pd.DataFrame:
        return pd.DataFrame({
            "order_id": range(1, n + 1),
            "customer_id": np.random.choice(customers["customer_id"], n),
            "order_date": [self.fake.date_between(start_date="-1y", end_date="today") for _ in range(n)],
            "total_amount": np.random.uniform(20, 1000, n).round(2),
        })

    def generate_order_items(self, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
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
                    product["price"],
                ])
                item_id += 1
        return pd.DataFrame(rows, columns=["item_id", "order_id", "product_id", "quantity", "item_price"])

    def generate_payments(self, orders: pd.DataFrame) -> pd.DataFrame:
        methods = ["Credit Card", "UPI", "NetBanking", "Wallet"]
        statuses = ["Success", "Failed", "Pending"]
        return pd.DataFrame({
            "payment_id": range(1, len(orders) + 1),
            "order_id": orders["order_id"],
            "method": np.random.choice(methods, len(orders)),
            "status": np.random.choice(statuses, len(orders)),
            "payment_date": orders["order_date"],
        })

    def save(self, df: pd.DataFrame, filename: str) -> None:
        os.makedirs(self.data_dir, exist_ok=True)
        df.to_csv(os.path.join(self.data_dir, filename), index=False)

    def generate_all(self, n_customers: int = 25, n_products: int = 25, n_orders: int = 25) -> None:
        customers = self.generate_customers(n_customers)
        products = self.generate_products(n_products)
        orders = self.generate_orders(customers, n_orders)
        order_items = self.generate_order_items(orders, products)
        payments = self.generate_payments(orders)

        self.save(customers, "customers.csv")
        self.save(products, "products.csv")
        self.save(orders, "orders.csv")
        self.save(order_items, "order_items.csv")
        self.save(payments, "payments.csv")


def main():
    generator = GenerateData()
    generator.generate_all()
    print("Synthetic dataset generated successfully.")


if __name__ == "__main__":
    main()
