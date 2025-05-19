import pandas as pd

def compare_forecast_vs_actual(forecast_df, actual_df):
    forecast_df['Month'] = pd.to_datetime(forecast_df['Month']).dt.to_period('M').astype(str)
    actual_df['Month'] = pd.to_datetime(actual_df['Month']).dt.to_period('M').astype(str)
    merged = pd.merge(forecast_df, actual_df, on='Month', how='left', suffixes=('_Forecast', '_Actual'))

    merged['Inflow_Actual'] = merged.get('Inflow_Actual', 0).fillna(0)
    merged['Outflow_Actual'] = merged.get('Outflow_Actual', 0).fillna(0)
    merged['Net Actual'] = merged['Inflow_Actual'] + merged['Outflow_Actual']
    merged['Net Forecast'] = merged['Net Cash Flow']
    merged['Net Variance'] = merged['Net Actual'] - merged['Net Forecast']
    merged['Accuracy %'] = 100 - abs(merged['Net Variance']) / merged['Net Forecast'].replace(0, 1) * 100

    def remark(acc): return "Excellent" if acc >= 95 else "Good" if acc >= 85 else "Fair" if acc >= 70 else "Poor"
    merged['Remark'] = merged['Accuracy %'].apply(remark)
    return merged