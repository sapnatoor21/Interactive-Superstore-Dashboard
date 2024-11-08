import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Sample data creation
np.random.seed(42)
data = {
    'Order ID': range(1, 101),
    'Category': np.random.choice(['Furniture', 'Office Supplies', 'Technology'], size=100),
    'Sub-Category': np.random.choice(['Bookcases', 'Chairs', 'Tables', 'Binders', 'Pens', 'Phones', 'Copiers', 'Storage'], size=100),
    'Sales': np.random.uniform(50, 500, size=100),
    'Quantity': np.random.randint(1, 10, size=100),
    'Profit': np.random.uniform(-50, 200, size=100),
    'Region': np.random.choice(['East', 'West', 'South', 'North'], size=100)
}

df = pd.DataFrame(data)

# Title
st.title("Interactive Superstore Dashboard")

# Sidebar for filters
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())
region_filter = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())

# Filter data based on selections
filtered_data = df[df['Category'].isin(category_filter) & df['Region'].isin(region_filter)]

# Sales by Category Chart
st.subheader("Sales by Category")
sales_by_category = filtered_data.groupby('Category')['Sales'].sum().reset_index()
fig1 = px.bar(sales_by_category, x='Category', y='Sales', title='Total Sales by Category')
st.plotly_chart(fig1)

# Profit by Category Chart
st.subheader("Profit by Category")
profit_by_category = filtered_data.groupby('Category')['Profit'].sum().reset_index()
fig2 = px.bar(profit_by_category, x='Category', y='Profit', title='Total Profit by Category')
st.plotly_chart(fig2)

# Sales vs. Profit Scatter Plot
st.subheader("Sales vs. Profit")
fig3 = px.scatter(filtered_data, x='Sales', y='Profit', color='Category', title='Sales vs. Profit', hover_data=['Sub-Category'])
st.plotly_chart(fig3)

# Display the raw data
st.subheader("Raw Data")
st.write(filtered_data)
