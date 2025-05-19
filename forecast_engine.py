import pandas as pd

def generate_forecast(assumptions):
    base_sales = assumptions['base_sales']
    growth = assumptions['sales_growth']
    immediate_pct = assumptions['immediate_payment_pct']
    cogs_pct = assumptions['cogs_pct']
    fixed_expenses = assumptions['fixed_expenses']
    loan_payment = assumptions['loan_payment']
    tax_pct = assumptions['tax_reserve_pct']
    inflow_delay = assumptions['inflow_delay']
    outflow_timing = assumptions['outflow_timing']

    forecast = []
    delayed_cash = 0

    for month in range(1, 13):
        month_name = pd.to_datetime(f'2025-{month:02d}-01').strftime('%b %Y')
        sales = base_sales * ((1 + growth) ** (month - 1))

        if inflow_delay == "30 days":
            inflow = delayed_cash
            delayed_cash = sales * immediate_pct
        else:
            inflow = sales * immediate_pct
            delayed_cash = sales * (1 - immediate_pct)

        cogs = sales * cogs_pct
        rent = fixed_expenses['rent']
        salaries = fixed_expenses['salaries']
        utilities = fixed_expenses['utilities']
        seasonal = fixed_expenses['seasonal']

        outflow = cogs + rent + salaries + utilities + seasonal + loan_payment + (sales * tax_pct)

        net_cash = inflow - outflow
        dscr = (inflow - (sales * tax_pct)) / loan_payment if loan_payment else None

        forecast.append({
            "Month": month_name,
            "Sales": round(sales, 2),
            "Inflow": round(inflow, 2),
            "Outflow": round(outflow, 2),
            "Net Cash Flow": round(net_cash, 2),
            "DSCR": round(dscr, 2) if dscr else "N/A"
        })

    return pd.DataFrame(forecast)