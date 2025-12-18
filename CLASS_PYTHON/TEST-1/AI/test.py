import pandas as pd

df = pd.read_csv("student-mat.csv", delimiter=';')
print(df.head(5))