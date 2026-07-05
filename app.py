import streamlit as st
import pandas as pd

st.title("📊 Customer Analytics Dashboard")

# Load your Excel file
data = pd.read_csv("customer.csv")

st.write("### Raw Data Preview")
st.dataframe(data)

st.write("### Summary Statistics")
st.write(data.describe())


st.title("📊 Customer Behaviour Dashboard")

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=37926c74-62d8-46d5-a100-a573e40cdad9&autoAuth=true&ctid=68a6b772-3760-49f5-b2d2-6a292154f999"
st.components.v1.iframe(powerbi_url, height=800, scrolling=True)

