import streamlit as st
from PIL import Image
from assumptions import get_assumptions
from forecast_engine import generate_forecast
from upload_actuals import upload_actual_cashflow
from accuracy_checker import compare_forecast_vs_actual
from report_generator import generate_pdf_report
from rolling_forecast import rolling_forecast_with_actuals

st.set_page_config(page_title="Finligence", layout="wide")

with st.sidebar:
    logo = Image.open("finligence_logo_bluegray.png")
    st.image(logo, use_column_width=True)
    st.title("Finligence")
    page = st.radio("Navigation", ["📊 Forecast", "📥 Upload Actuals", "🔁 Rolling Forecast", "📝 Generate Report"])
    st.markdown("---")
    st.markdown("**Certified by:**")
    st.markdown("FCPA | FCMA | CGMA")

st.title("Finligence — AI-Powered Financial Forecasting")

if page == "📊 Forecast":
    st.subheader("Step 1: Enter Forecast Assumptions")
    assumptions = get_assumptions()
    if st.button("Generate 12-Month Forecast"):
        forecast_df = generate_forecast(assumptions)
        st.success("Forecast generated successfully!")
        st.dataframe(forecast_df)
        st.line_chart(forecast_df.set_index("Month")[["Inflow", "Outflow", "Net Cash Flow"]])
        st.session_state["forecast_df"] = forecast_df

elif page == "📥 Upload Actuals":
    st.subheader("Step 2: Upload Actual Bank Statement")
    actual_df = upload_actual_cashflow()
    if actual_df is not None:
        st.session_state["actual_df"] = actual_df

elif page == "🔁 Rolling Forecast":
    st.subheader("Step 3: Rolling Forecast (with Actuals)")
    if "forecast_df" in st.session_state and "actual_df" in st.session_state:
        rolling_df = rolling_forecast_with_actuals(st.session_state["forecast_df"], st.session_state["actual_df"])
        st.dataframe(rolling_df)
        st.line_chart(rolling_df.set_index("Month")[["Inflow", "Outflow", "Net Cash Flow"]])
    else:
        st.warning("Please upload actuals and generate a forecast first.")

elif page == "📝 Generate Report":
    st.subheader("Step 4: Generate Certified PDF Report")
    if "forecast_df" in st.session_state and "actual_df" in st.session_state:
        comparison_df = compare_forecast_vs_actual(st.session_state["forecast_df"], st.session_state["actual_df"])
        pdf_path = generate_pdf_report(st.session_state["forecast_df"], comparison_df)
        st.success("PDF report generated!")
        with open(pdf_path, "rb") as f:
            st.download_button("Download Report", data=f, file_name="Finligence_CashFlow_Report.pdf")