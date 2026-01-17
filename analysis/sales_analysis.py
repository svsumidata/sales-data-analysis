import pandas as pd
import matplotlib.pyplot as plt


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
# -------------------------
# Sales by Category chart
# -------------------------

# Example: adjust column name if needed
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure()
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

