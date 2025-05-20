def generate_summary_report(forecast_df):
    total_inflow = forecast_df["Inflow"].sum()
    total_outflow = forecast_df["Outflow"].sum()
    net_cash_flow = forecast_df["Net Cash Flow"].sum()
    avg_dscr = forecast_df["DSCR"].mean()

    report = {
        "Total Inflow": round(total_inflow, 2),
        "Total Outflow": round(total_outflow, 2),
        "Net Cash Flow": round(net_cash_flow, 2),
        "Average DSCR": round(avg_dscr, 2),
        "Next Step": (
            "You may now generate your formal forecast summary report for submission to lenders. "
            "Ensure your assumptions reflect real business conditions."
        )
    }

    return report
