import pandas as pd

data = {
    'Name': ['Ram', 'Shyam', 'Hari'],
    'Marks': [85, 90, 88],
    'Passed': [True, True, True]
}

df = pd.DataFrame(data)
print(type(df))

print(df.dtypes)