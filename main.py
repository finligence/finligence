import streamlit as st
from assumptions import run_assumption_wizard
from forecast_engine import generate_forecast
from report_generator import generate_summary_report
from upload_actuals import upload_actuals_and_compare
from accuracy_checker import display_accuracy_results

# Language setup
LANGUAGES = {"English": "en", "Khmer": "km"}
st.set_page_config(page_title="Finligence", layout="wide")

# Sidebar: App Navigation
st.sidebar.image("finligence_logo_bluegray.png", width=180)
st.sidebar.title("Finligence")
language = st.sidebar.selectbox("🌐 Language", options=LANGUAGES.keys())

# Wizard navigation
pages = {
    "🏁 Start": "start",
    "📊 Step 1: Input Assumptions": "assumptions",
    "📈 Step 2: Forecast & Cash Flow": "forecast",
    "📝 Step 3: Report Summary": "report",
    "📤 Step 4: Upload Actuals (optional)": "actuals",
    "📐 Step 5: Accuracy Check": "accuracy",
}

selection = st.sidebar.radio("Navigate", list(pages.keys()))

# Render selected section
if pages[selection] == "start":
    st.title("Finligence")
    st.subheader("Forecast. Certify. Lend.")
    st.markdown(
        """
        👋 Welcome to Finligence — your AI-powered financial assistant.
        
        Use the wizard on the left to input your business assumptions, 
        generate financial forecasts, and produce a bank-ready report.
        """
    )

elif pages[selection] == "assumptions":
    run_assumption_wizard(language=LANGUAGES[language])

elif pages[selection] == "forecast":
    generate_forecast(language=LANGUAGES[language])

elif pages[selection] == "report":
    generate_summary_report(language=LANGUAGES[language])

elif pages[selection] == "actuals":
    upload_actuals_and_compare(language=LANGUAGES[language])

elif pages[selection] == "accuracy":
    display_accuracy_results(language=LANGUAGES[language])
