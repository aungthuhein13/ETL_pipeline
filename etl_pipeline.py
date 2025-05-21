
import pandas as pd

# Load raw data
df = pd.read_csv("raw_data.csv")

# Step 1: Drop rows with null Order ID or Quantity
df = df.dropna(subset=["Order ID", "Quantity"])

# Step 2: Drop duplicates
df = df.drop_duplicates()

# Step 3: Fill missing Price with median
df["Price"] = df["Price"].fillna(df["Price"].median())

# Step 4: Convert data types
df["Order ID"] = df["Order ID"].astype(int)
df["Quantity"] = df["Quantity"].astype(int)

# Step 5: Rename columns
df = df.rename(columns={
    "Order ID": "order_id",
    "Customer Name": "customer_name",
    "Product": "product",
    "Quantity": "quantity",
    "Price": "price",
    "Purchase Date": "purchase_date"
})

# Step 6: Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("ETL pipeline complete. Cleaned data saved to data/cleaned_data.csv")
