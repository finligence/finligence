import streamlit as st
import pandas as pd

def upload_actual_cashflow():
    st.header("Upload Actual Cash Flow")

    uploaded_file = st.file_uploader("Upload CSV file (with Date, Description, Debit, Credit)", type=["csv"])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            df['Date'] = pd.to_datetime(df['Date'])
            df['Amount'] = df['Credit'].fillna(0) - df['Debit'].fillna(0)
            df['Month'] = df['Date'].dt.to_period("M").astype(str)
            df['Type'] = df['Amount'].apply(lambda x: "Inflow" if x > 0 else "Outflow")
            monthly_summary = df.groupby(['Month', 'Type'])['Amount'].sum().unstack(fill_value=0).reset_index()
            monthly_summary['Net Cash Flow'] = monthly_summary.get('Inflow', 0) + monthly_summary.get('Outflow', 0)
            st.dataframe(monthly_summary)
            return monthly_summary
        except Exception as e:
            st.error(f"Upload failed: {e}")
    return None