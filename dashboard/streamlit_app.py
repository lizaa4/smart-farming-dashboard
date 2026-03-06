import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Smart Farming Dashboard")

# Load data
df = pd.read_csv("../outputs/cleaned_data.csv")

st.subheader("Preview Data")
st.dataframe(df)

# =========================
# 1. TIME SERIES TREND
# =========================
st.subheader("Temperature Trend")

st.line_chart(df["temperature_C"])

# =========================
# 2. GAUGE METER (SOIL MOISTURE)
# =========================
st.subheader("Current Soil Moisture")

moisture = df["soil_moisture_%"].mean()

fig, ax = plt.subplots()

ax.barh(["Soil Moisture"], [moisture])
ax.set_xlim(0,100)

st.pyplot(fig)

st.write(f"Average Soil Moisture: {moisture:.2f}%")

# =========================
# 3. HEATMAP CORRELATION
# =========================
st.subheader("Sensor Correlation Heatmap")

corr = df.select_dtypes(include="number").corr()

fig2, ax2 = plt.subplots()

sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)

st.pyplot(fig2)

# =========================
# 4. ALERT SYSTEM
# =========================
st.subheader("Sensor Alerts")

temp_avg = df["temperature_C"].mean()
humidity_avg = df["humidity_%"].mean()

if temp_avg > 35:
    st.error("⚠️ Temperature too high!")
else:
    st.success("Temperature is normal")

if humidity_avg < 30:
    st.error("⚠️ Humidity too low!")
else:
    st.success("Humidity level is safe")
