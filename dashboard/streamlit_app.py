import streamlit as st
import pandas as pd

st.title("Smart Farming Dashboard")

df = pd.read_csv("outputs/cleaned_data.csv")

st.subheader("Preview Data")
st.dataframe(df)

st.subheader("Jumlah Jenis Tanaman")
st.bar_chart(df["crop_type"].value_counts())

st.subheader("Rata-rata Soil Moisture per Region")
st.bar_chart(df.groupby("region")["soil_moisture_%"].mean())

st.subheader("Distribusi Temperature")
st.line_chart(df["temperature_C"])
