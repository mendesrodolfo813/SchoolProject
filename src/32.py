import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 22],
    "City": ["New York", "Chicago", "Los Angeles"]
}

df = pd.DataFrame(data)
print(df)
