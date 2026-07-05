import streamlit as st
import pandas as pd

st.title("📊 Customer Analytics Dashboard")

# Load your Excel file
data = pd.read_excel("customer.xlsx")

st.write("### Raw Data Preview")
st.dataframe(data)

st.write("### Summary Statistics")
st.write(data.describe())
