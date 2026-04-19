from src.preprocessing import load_data, clean_data
from src.analysis import plot_trends
from src.anomaly import detect_anomalies
from src.forecasting import forecast

df = load_data()
df = clean_data(df)

df = detect_anomalies(df)
print(df)

plot_trends(df)
forecast(df)