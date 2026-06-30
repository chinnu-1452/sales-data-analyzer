import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Data Analyzer", page_icon="💼")

st.title("💼 Sales Data Analyzer")
st.subheader("Built by Talari Pranay | 90 Day DS Journey")

df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Product Sales
st.header("🏆 Sales by Product Line")
product_sales = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
st.bar_chart(product_sales)

# Monthly Trend
st.header("📈 Monthly Sales Trend")
df['Month'] = df['ORDERDATE'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['SALES'].sum()
st.line_chart(monthly_sales)

# Top Customers
st.header("👥 Top 10 Customers")
top_customers = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_customers)

# Country Sales
st.header("🌍 Sales by Country")
country_sales = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(10)
st.bar_chart(country_sales)

st.success("Built by Talari Pranay | #BuildingInPublic")