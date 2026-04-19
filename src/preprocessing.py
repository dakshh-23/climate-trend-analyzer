import pandas as pd

def load_data():
    df = pd.read_csv('data/climate_data.csv')
    return df

def clean_data(df):
    df = df.dropna()
    return df