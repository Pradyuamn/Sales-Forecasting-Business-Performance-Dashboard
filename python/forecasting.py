import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("../data/cleaned_sales.csv")

# Convert Month column
df['Month'] = pd.to_datetime(df['Month'])

# Group monthly sales
monthly_sales = df.groupby('Month')['Sales'].sum()

# -------------------------------
# BUILD MODEL (YOU WERE MISSING THIS 😑)
# -------------------------------
model = ARIMA(monthly_sales, order=(1,1,1))
model_fit = model.fit()

# -------------------------------
# FORECAST
# -------------------------------
forecast = model_fit.forecast(steps=6)

# -------------------------------
# FIX FORECAST INDEX (IMPORTANT)
# -------------------------------
forecast_index = pd.date_range(
    start=monthly_sales.index[-1] + pd.DateOffset(months=1),
    periods=6,
    freq='MS'
)

forecast.index = forecast_index

print("\n📊 Forecast for next 6 months:\n")
print(forecast)

# -------------------------------
# PLOT
# -------------------------------
plt.figure()
monthly_sales.plot(label="Actual Sales")
forecast.plot(label="Forecast", linestyle='dashed')
plt.title("Sales Forecast")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# -------------------------------
# SAVE FILES FOR TABLEAU
# -------------------------------
forecast_df = forecast.reset_index()
forecast_df.columns = ['Month', 'Sales']
forecast_df['Type'] = 'Forecast'

actual_df = monthly_sales.reset_index()
actual_df.columns = ['Month', 'Sales']
actual_df['Type'] = 'Actual'

final_df = pd.concat([actual_df, forecast_df])
final_df = final_df.sort_values(by='Month')

final_df.to_csv("../output/final_dataset.csv", index=False)

print("Final dataset created for Tableau ✅")