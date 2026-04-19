from sklearn.linear_model import LinearRegression
import numpy as np

def forecast(df):
    X = df[['Year']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    future = np.array([[2022], [2023], [2024]])
    pred = model.predict(future)

    print("Future Predictions:", pred)