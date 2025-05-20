import streamlit as st
import pandas as pd

def upload_actuals_and_compare(forecast_df):
    st.subheader("Upload Actual Financial Data")
    uploaded_file = st.file_uploader("Choose your actual financials CSV file", type="csv")

    if uploaded_file:
        actuals_df = pd.read_csv(uploaded_file)

        # Basic validation
        if "Month" in actuals_df.columns and "Net Cash Flow" in actuals_df.columns:
            comparison = forecast_df.merge(actuals_df, on="Month", suffixes=("_Forecast", "_Actual"))
            comparison["Variance"] = comparison["Net Cash Flow_Actual"] - comparison["Net Cash Flow_Forecast"]
            st.write("Comparison Table")
            st.dataframe(comparison)
        else:
            st.error("CSV must contain 'Month' and 'Net Cash Flow' columns.")
