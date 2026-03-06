import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart Farming Dashboard")

# load data
df = pd.read_csv("smart_farming_cleaned.csv")

# tampilkan data
st.subheader("Dataset Preview")
st.write(df.head())

# grafik temperature
st.subheader("Temperature Distribution")

fig, ax = plt.subplots()
ax.hist(df["temperature"])
st.pyplot(fig)

# grafik soil moisture
st.subheader("Soil Moisture Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(df["soil_moisture"])
st.pyplot(fig2)
