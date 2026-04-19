import streamlit as st
import pandas as pd

df = pd.read_csv('../data/climate_data.csv')

st.title("🌍 Climate Trend Analyzer")

year = st.selectbox("Select Year", df['Year'].unique())

filtered = df[df['Year'] == year]

st.write(filtered)

st.bar_chart(filtered[['Rainfall']])