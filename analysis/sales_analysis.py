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
