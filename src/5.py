import pandas as pd

def get_unique_values(df, column):
    return df[column].unique()

df = pd.read_csv("data.csv")
print(get_unique_values(df, "City"))