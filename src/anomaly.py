def detect_anomalies(df):
    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Anomaly'] = ((df['Temperature'] - mean)/std).apply(
        lambda x: 'Yes' if abs(x) > 1.5 else 'No'
    )

    return df