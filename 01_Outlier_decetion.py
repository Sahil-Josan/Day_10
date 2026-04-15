import pandas as pd
import numpy as np


df = pd.read_csv(r"E:\Data Analytics work\VS code work\day10\sales_cleaned.csv")

# 2. Calculate Z-Score for Sales [cite: 15]
df['z_score'] = (df['Sales'] - df['Sales'].mean()) / df['Sales'].std()

# 3. Identify Outliers (threshold of > 3 or < -3) 
outliers = df[np.abs(df['z_score']) > 3]

print(f"Detected {len(outliers)} outliers in the dataset.")
print(outliers[['Date', 'Product', 'Sales', 'z_score']])
