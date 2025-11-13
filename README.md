# E-Commerce ETL Pipeline (Synthetic Data → SQLite → SQL Analytics)

This project implements a complete **mini data engineering pipeline** that:

1. **Generates synthetic e-commerce data** (5 related CSV files)
2. **Ingests the data into a SQLite database**
3. **Runs an analytical SQL query** that joins all tables
4. **Outputs a clean, combined dataset**

The project is designed to demonstrate **ETL, SQL, and Python automation skills** using a real-world workflow.

---

## Features (Base Version)

- Generate 5 realistic e-commerce datasets:
  - `customers`
  - `products`
  - `orders`
  - `order_items`
  - `payments`
- Store them as CSV files inside `data/raw/`
- Create a SQLite database: `db/ecommerce.db`
- Load all CSVs into database tables
- Run a SQL JOIN query across all tables
- Display final analytics output using Python

---

## Project Structure
 ```
ecommerce-analytics/
│
├── data/
│ └── raw/ # Generated CSV files
│
├── db/ # SQLite database (ignored from Git)
│
├── logs/ # Log files (ignored from Git)
│
├── sql/
│ └── master_join.sql # Analytics SQL query
│
├── src/
│ ├── config.py
│ ├── generate_data.py # Generate synthetic e-commerce data
│ ├── ingest.py # Load CSVs into SQLite database
│ └── run_query.py # Run SQL join & print output
│
├── run_pipeline.bat # Optional Windows automation script
├── requirements.txt
└── README.md
 ```
---

## Requirements

- Python 3.8+
- pip
- Virtual environment (optional but recommended)
- SQLite (comes preinstalled with Python)

Install dependencies:

pip install -r requirements.txt


---

## Setup Instructions

### 1️ Clone the repository
 ```
git clone https://github.com/<your-username>/ecommerce-analytics.git
cd ecommerce-analytics
 ```

---

## 2️ Create and activate a virtual environment

### Windows:
 ```
python -m venv venv
venv\Scripts\activate
 ```

---

## 3️ Install Python dependencies
 ```
pip install -r requirements.txt
 ```

---

## 4️ Run the ETL Steps Manually (Base Version)

### Step 1: Generate Synthetic Data
 ```
python src/generate_data.py
 ```

This will create the following CSV files:

- `customers.csv`
- `products.csv`
- `orders.csv`
- `order_items.csv`
- `payments.csv`

Stored inside:
data/raw/


---

### Step 2: Ingest Data into SQLite
 ```
python src/ingest.py
 ```
This will create:

db/ecommerce.db

with 5 populated tables.

---

###  Step 3: Run the SQL Join Query
 ```
python src/run_query.py
 ```
This executes:

sql/master_join.sql

You will see a full combined table printed with:

- customer info  
- order info  
- product info  
- quantity & price  
- payment details  

---

## Optional: Run the Entire Pipeline in One Command

### If you are on Windows:
 ```
run_pipeline.bat
 ```
---

## How the Pipeline Works (ETL Flow)

### **Extract**
`generate_data.py` creates synthetic e-commerce data → saved as CSV.

### **Transform**
Data is formatted and structured into relational tables.

### **Load**
`ingest.py` loads all CSVs into `ecommerce.db` using SQLite.

### **Analyze**
`run_query.py` executes a SQL join query to produce a final report.

This simulates a **real-world data engineering workflow**.

---

## SQL Query Overview

The SQL file joins:

customers
orders
order_items
products
payments

to produce a merged dataset showing:

- Customer name & city
- Order details
- Product details
- Quantity & pricing
- Payment method & status

---

## Technologies Used

- Python
- Pandas
- Faker
- SQLite
- SQL
- Tabulate

---

## Author

**Akshay Kashyap M**  
E-commerce ETL Pipeline Project

---

## Future Enhancements (Optional)

- Add strict schema for SQLite
- Add validation before ingestion
- Add class-based data generator
- Add logging & profiling
- Add visualization dashboards
- Containerize with Docker
