import streamlit as st
import pandas as pd

def display_accuracy_results():
    st.subheader("Check Forecast Accuracy")

    uploaded_file = st.file_uploader("Upload actuals CSV to compare", type="csv")

    if uploaded_file:
        try:
            actuals_df = pd.read_csv(uploaded_file)

            if "Month" in actuals_df.columns and "Net Cash Flow" in actuals_df.columns and "Forecast" in actuals_df.columns:
                actuals_df["Accuracy (%)"] = 100 - (abs(actuals_df["Net Cash Flow"] - actuals_df["Forecast"]) / actuals_df["Forecast"]) * 100
                st.success("Accuracy calculated.")
                st.dataframe(actuals_df)
            else:
                st.error("CSV must contain 'Month', 'Net Cash Flow', and 'Forecast' columns.")
        except Exception as e:
            st.error(f"Error loading file: {e}")
