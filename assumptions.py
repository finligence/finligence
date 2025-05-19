import streamlit as st

def get_assumptions():
    st.subheader("1. Business Revenue Assumptions")

    base_sales = st.number_input("Average monthly sales (USD)", min_value=0.0, value=10000.0)
    sales_growth = st.slider("Expected monthly sales growth (%)", -50, 100, 0) / 100
    immediate_payment_pct = st.slider("Percent of customers who pay immediately", 0, 100, 70) / 100

    st.subheader("2. Cost and Expense Assumptions")

    cogs_pct = st.slider("Cost of goods sold (% of sales)", 0, 100, 40) / 100
    rent = st.number_input("Monthly rent (USD)", min_value=0.0, value=1000.0)
    salaries = st.number_input("Monthly salaries (USD)", min_value=0.0, value=2500.0)
    utilities = st.number_input("Monthly utilities (USD)", min_value=0.0, value=300.0)
    seasonal_expense = st.number_input("Seasonal/One-time expenses (average per month)", min_value=0.0, value=0.0)

    st.subheader("3. Financing & Loan Repayment")

    loan_payment = st.number_input("Monthly loan repayment (USD)", min_value=0.0, value=500.0)
    tax_reserve_pct = st.slider("Reserve for tax & compliance (% of sales)", 0, 50, 5) / 100

    st.subheader("4. Timing of Cash Flows")

    inflow_delay = st.selectbox("Customer payment delay timing", ["Immediate", "30 days"])
    outflow_timing = st.selectbox("Supplier/outflow timing", ["Same month", "Prepaid", "End of month"])

    assumptions = {
        "base_sales": base_sales,
        "sales_growth": sales_growth,
        "immediate_payment_pct": immediate_payment_pct,
        "cogs_pct": cogs_pct,
        "fixed_expenses": {
            "rent": rent,
            "salaries": salaries,
            "utilities": utilities,
            "seasonal": seasonal_expense
        },
        "loan_payment": loan_payment,
        "tax_reserve_pct": tax_reserve_pct,
        "inflow_delay": inflow_delay,
        "outflow_timing": outflow_timing
    }

    return assumptions