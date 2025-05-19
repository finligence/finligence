import pandas as pd

def rolling_forecast_with_actuals(forecast_df, actual_df):
    forecast_df['Month'] = pd.to_datetime(forecast_df['Month']).dt.to_period('M').astype(str)
    actual_df['Month'] = pd.to_datetime(actual_df['Month']).dt.to_period('M').astype(str)
    df = pd.merge(forecast_df, actual_df, on='Month', how='left', suffixes=('_Forecast', '_Actual'))

    df['Inflow_Final'] = df['Inflow_Actual'].combine_first(df['Inflow_Forecast'])
    df['Outflow_Final'] = df['Outflow_Actual'].combine_first(df['Outflow_Forecast'])
    df['Net Cash Flow_Final'] = df['Inflow_Final'] - df['Outflow_Final']

    df['Loan Payment'] = df.get('Loan Payment', 500)
    df['DSCR_Final'] = (df['Inflow_Final']) / df['Loan Payment']
    df['DSCR_Final'] = df['DSCR_Final'].round(2)

    result = df[['Month', 'Inflow_Final', 'Outflow_Final', 'Net Cash Flow_Final', 'DSCR_Final']].copy()
    result.columns = ['Month', 'Inflow', 'Outflow', 'Net Cash Flow', 'DSCR']
    return result