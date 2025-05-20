import streamlit as st

def run_assumption_wizard(language="en"):
    st.header("Business Forecast Assumptions")

    if language == "km":
        st.subheader("១. ការស្មានចំណូលអាជីវកម្ម")
        avg_sales = st.number_input("ចំណូលលក់ជាមធ្យម (USD)", value=10000)
        growth = st.slider("អត្រាកំណើនលក់ប្រចាំខែ (%)", -50, 100, 10)
        pay_now = st.slider("ភាគរយអតិថិជនបង់ប្រាក់ភ្លាមៗ (%)", 0, 100, 70)
    else:
        st.subheader("1. Business Revenue Assumptions")
        avg_sales = st.number_input("Average monthly sales (USD)", value=10000)
        growth = st.slider("Expected monthly sales growth (%)", -50, 100, 10)
        pay_now = st.slider("Percent of customers who pay immediately (%)", 0, 100, 70)

    if language == "km":
        st.subheader("២. ស្មានចំណាយប្រចាំខែ")
        cogs_pct = st.slider("ថ្លៃដើម (% នៃលក់)", 0, 100, 40)
        rent = st.number_input("ថ្លៃជួលប្រចាំខែ (USD)", value=1000)
        salaries = st.number_input("ប្រាក់ខែបុគ្គលិកសរុប (USD)", value=2500)
        utilities = st.number_input("ថ្លៃសេវាប្រើប្រាស់ (USD)", value=300)
        other = st.number_input("ចំណាយផ្សេងៗ / មួយដង (USD)", value=300)
    else:
        st.subheader("2. Cost and Expense Assumptions")
        cogs_pct = st.slider("Cost of goods sold (% of sales)", 0, 100, 40)
        rent = st.number_input("Monthly rent (USD)", value=1000)
        salaries = st.number_input("Monthly salaries (USD)", value=2500)
        utilities = st.number_input("Monthly utilities (USD)", value=300)
        other = st.number_input("Seasonal/One-time expenses (average per month)", value=300)

    if language == "km":
        st.subheader("៣. ស្មានថវិកាហិរញ្ញវត្ថុ")
        loan = st.number_input("បង់ប្រាក់កម្ចីប្រចាំខែ (USD)", value=500)
        reserve = st.slider("បម្រុងសម្រាប់ពន្ធនិងការអនុលោម (% នៃលក់)", 0, 100, 5)
    else:
        st.subheader("3. Financing & Loan Repayment")
        loan = st.number_input("Monthly loan repayment (USD)", value=500)
        reserve = st.slider("Reserve for tax & compliance (% of sales)", 0, 100, 5)

    # Save inputs
    st.session_state.assumptions = {
        "avg_sales": avg_sales,
        "growth": growth,
        "pay_now": pay_now,
        "cogs_pct": cogs_pct,
        "rent": rent,
        "salaries": salaries,
        "utilities": utilities,
        "other": other,
        "loan": loan,
        "reserve": reserve,
    }

    if language == "km":
        st.success("ស្មាននានាត្រូវបានរក្សាទុក! សូមបន្តទៅជំហានបន្ទាប់។")
    else:
        st.success("Assumptions saved. Proceed to the next step.")
