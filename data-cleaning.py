# clean_sales_data.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create fictional sales dataset
np.random.seed(42)
dates = pd.date_range(start='2025-05-01', end='2025-05-31', freq='D')
products = ['T-Shirt', 'Pants', 'Shoes', 'Cap']
regions = ['SP', 'RJ', 'MG', 'Sao Paulo', 'Rio']

data = {
    'Date': dates,
    'Product': np.random.choice(products, size=len(dates)),
    'Quantity': np.random.randint(5, 20, size=len(dates)),
    'Unit Price': np.random.uniform(20, 150, size=len(dates)).round(2),
    'Region': np.random.choice(regions, size=len(dates))
}

df = pd.DataFrame(data)

# Add missing values
df.loc[np.random.choice(df.index, 5), 'Unit Price'] = np.nan
df.loc[np.random.choice(df.index, 3), 'Quantity'] = np.nan

# Add duplicates
df = pd.concat([df, df.iloc[[5, 10, 15]]], ignore_index=True)

# Add outlier
df.loc[25, 'Unit Price'] = 1000

# Calculate Total Sale
df['Total Sale'] = df['Quantity'] * df['Unit Price']
df['Total Sale'] = df['Total Sale'].fillna(0)

# Save raw dataset
df.to_csv('sales_data_raw.csv', index=False)

# 2. Identify issues
print("Descriptive statistics before cleaning:")
print(df.describe())
print("\nMissing values:")
print(df.isnull().sum())
print(f"\nNumber of duplicates: {df.duplicated().sum()}")

# 3. Remove duplicates
df = df.drop_duplicates()
print(f"\nAfter removing duplicates: {len(df)} rows remaining")

# 4. Handle missing values
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
df['Unit Price'] = df['Unit Price'].fillna(df['Unit Price'].median())
df['Total Sale'] = df['Quantity'] * df['Unit Price']
print("\nMissing values after filling:")
print(df.isnull().sum())

# 5. Standardize 'Region' column
df['Region'] = df['Region'].replace({'Sao Paulo': 'SP', 'Rio': 'RJ'}).fillna('MG')
print("\nUnique values in 'Region' column after standardization:")
print(df['Region'].unique())

# 6. Remove outliers
Q1 = df['Unit Price'].quantile(0.25)
Q3 = df['Unit Price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['Unit Price'] >= lower_bound) & (df['Unit Price'] <= upper_bound)]
print(f"\nAfter removing outliers: {len(df)} rows remaining")

# 7. Visualize distribution after cleaning
plt.figure(figsize=(10, 5))
plt.boxplot(df['Unit Price'])
plt.title('Unit Price Distribution After Cleaning')
plt.savefig('unit_price_distribution.png')
plt.close()

# 8. Save cleaned dataset
df.to_csv('sales_data_cleaned.csv', index=False)
print("\nCleaned dataset saved as 'sales_data_cleaned.csv'")
