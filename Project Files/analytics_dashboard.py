import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():
    st.subheader("📊 Your Health Trends")

    # Sample data (You can replace with real input later)
    data = {
        "Date": ["2025-06-01", "2025-06-05", "2025-06-10", "2025-06-15"],
        "Heart Rate": [78, 82, 76, 80],
        "Blood Pressure": [120, 122, 118, 121],
        "Blood Glucose": [95, 102, 98, 99]
    }

    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df["Date"])

    # Line chart
    st.line_chart(df.set_index("Date"))

    # Optional: Show raw data
    if st.checkbox("Show raw data"):
        st.write(df)
