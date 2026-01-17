import pandas as pd

# Load the sales dataset
df = pd.read_csv("../data/Sales Data.csv")

# Basic inspection
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns)

# Missing values check
print("\nMissing values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Business insights (run only if columns exist)
if "Sales" in df.columns:
    print("\nTotal Sales:", df["Sales"].sum())
    print("Average Sales:", df["Sales"].mean())

if "Region" in df.columns and "Sales" in df.columns:
    print("\nSales by Region:")
    print(df.groupby("Region")["Sales"].sum())

if "Product" in df.columns and "Sales" in df.columns:
    print("\nSales by Product:")
    print(df.groupby("Product")["Sales"].sum())
