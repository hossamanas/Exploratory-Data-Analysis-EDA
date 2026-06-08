import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('Dataset for Data Analytics.xlsx - Sheet1.csv')

# 2. Data Profiling & Quick Inspection
print("--- Data Dimensions ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

print("--- Missing Values Check ---")
print(df.isnull().sum(), "\n")

# 3. Logic Skeleton: Five-Number Summary & Centers of Gravity
print("--- Descriptive Statistics for TotalPrice ---")
total_price_stats = df['TotalPrice'].describe()
print(total_price_stats, "\n")

print("--- Descriptive Statistics for UnitPrice ---")
unit_price_stats = df['UnitPrice'].describe()
print(unit_price_stats, "\n")

# 4. Product Insights (Revenue and Quantities)
print("--- Product Performance Analysis ---")
product_analysis = df.groupby('Product').agg(
    Total_Revenue=('TotalPrice', 'sum'),
    Total_Quantity=('Quantity', 'sum'),
    Average_Unit_Price=('UnitPrice', 'mean')
).sort_values(by='Total_Revenue', ascending=False)
print(product_analysis, "\n")

# 5. Operational Insights (Payment Methods & Order Status)
print("--- Payment Methods Distribution ---")
print(df['PaymentMethod'].value_counts(), "\n")

print("--- Order Status Distribution ---")
print(df['OrderStatus'].value_counts(), "\n")
