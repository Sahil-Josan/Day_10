import pandas as pd
import numpy as np

df = pd.read_csv(r"E:\Data Analytics work\VS code work\day10\sales_cleaned.csv")

df['Category'] = np.where(df['Sales'] > 500, 'High', 'Low')

pivot_comparison = df.pivot_table(
    values='Sales',
    index='Region',
    columns='Category',
    aggfunc='sum'
)

pivot_comparison['Growth'] = (
    pivot_comparison['High'] - pivot_comparison['Low']
) / pivot_comparison['Low']

print("Regional Category Performance:")
print(pivot_comparison)
