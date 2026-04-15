import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats

# Load and prepare data
df = pd.read_csv('sales_cleaned.csv')
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Date_Ordinal'] = df['Date'].map(dt.datetime.toordinal)

# --- Baseline Model (Day 9) ---
X = df[['Date_Ordinal']]
y = df['Sales']
model_orig = LinearRegression().fit(X, y)

# --- Outlier Removal (Today's Task) ---
df['z_score'] = np.abs(stats.zscore(df['Sales']))
df_clean = df[df['z_score'] <= 3].copy()
outliers_removed = len(df) - len(df_clean)

# Re-run the forecast on cleaned data
X_clean = df_clean[['Date_Ordinal']]
y_clean = df_clean['Sales']
model_clean = LinearRegression().fit(X_clean, y_clean)

# Predict next 30 days
last_date = df['Date_Ordinal'].max()
future_dates = np.array(range(last_date + 1, last_date + 31)).reshape(-1, 1)
future_dates_dt = [dt.datetime.fromordinal(int(d[0])) for d in future_dates]

pred_orig = model_orig.predict(future_dates)
pred_clean = model_clean.predict(future_dates)

# Visualization
plt.figure(figsize=(12, 6))
plt.scatter(df['Date'], df['Sales'], color='blue', alpha=0.3, label='Actual Data')
plt.plot(future_dates_dt, pred_orig, color='red', linestyle=':', label='Original Trend')
plt.plot(future_dates_dt, pred_clean, color='green', linewidth=2, label='Cleaned Trend')

plt.title(f"Forecast Comparison (Outliers Removed: {outliers_removed})")
plt.legend()
plt.savefig('cleaned_forecast.png')

print(f"Original Trend Slope: {model_orig.coef_[0]:.4f}")
print(f"Cleaned Trend Slope: {model_clean.coef_[0]:.4f}")

# Outliers are mistakes when caused by errors.
# They are discoveries when they represent real business events.
# So, they should be analyzed before removing.
