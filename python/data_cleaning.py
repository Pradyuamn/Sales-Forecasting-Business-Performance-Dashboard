import pandas as pd

# Load dataset
df = pd.read_csv("../data/Superstore.csv", encoding='latin1')

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Remove missing values
df = df.dropna()

# Create Month column
df['Month'] = df['Order Date'].dt.to_period('M')

# Save cleaned data
df.to_csv("../data/cleaned_sales.csv", index=False)

print("Data cleaning completed ✅")