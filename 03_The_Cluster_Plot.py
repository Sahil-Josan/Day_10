import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv(r"E:\Data Analytics work\VS code work\day10\sales_cleaned.csv")
df['Category'] = np.where(df['Sales'] > 500, 'High', 'Low')

plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Sales', hue='Category', data=df, estimator=sum)
plt.title("Revenue Comparison: Region vs. Category")
plt.show()

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"E:\Data Analytics work\VS code work\day10\sales_cleaned.csv")

# Convert Sales to numeric (safe)
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Category'] = np.where(df['Sales'] > 500, 'High', 'Low')

# Plot using Product instead of Category
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Sales', hue='Product', data=df, estimator=sum)

plt.legend(title='Product')
plt.tight_layout()

plt.show()