import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
print(df.head())
print(df.shape)
print(df.columns)
# Sales by Product Line
print("\n--- SALES BY PRODUCT LINE ---")
product_sales = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
print(product_sales)

plt.figure(figsize=(12,6))
product_sales.plot(kind='bar', color='steelblue')
plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('product_sales.png')
plt.show()

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
df['Month'] = df['ORDERDATE'].dt.to_period('M')
monthly_sales = df.groupby('Month')['SALES'].sum()

plt.figure(figsize=(14,6))
monthly_sales.plot(kind='line', color='green', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales.png')
plt.show()

top_customers = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
top_customers.plot(kind='bar', color='orange')
plt.title('Top 10 Customers by Sales')
plt.xlabel('Customer')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_customers.png')
plt.show()


country_sales = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
country_sales.plot(kind='bar', color='purple')
plt.title('Top 10 Countries by Sales')
plt.xlabel('Country')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('country_sales.png')
plt.show()