import pandas as pd

def summarize(data_series, total_n):
    summary = pd.DataFrame({
    'Count': data_series,
    'Proportion (%)': (data_series / total_n * 100).round(1)
    })
    return summary