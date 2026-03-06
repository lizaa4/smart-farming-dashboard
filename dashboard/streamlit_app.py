import streamlit as st
import pandas as pd

st.title("Smart Farming Dashboard")

df = pd.read_csv("../outputs/cleaned_data.csv")

st.write("Preview Data")
st.dataframe(df)
