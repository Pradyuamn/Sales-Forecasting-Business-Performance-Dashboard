import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales.csv")

# Convert Month to datetime (important)
df['Month'] = pd.to_datetime(df['Month'])

# -------------------------------
# 1. Monthly Sales Trend
# -------------------------------
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# -------------------------------
# 2. Region-wise Sales
# -------------------------------
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# 3. Category-wise Sales
# -------------------------------
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()