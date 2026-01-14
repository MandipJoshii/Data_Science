import pandas as pd
import numpy as np
marks = [10,20,30,40,50,60]

df = pd.DataFrame(marks, index=['A','B','C','D','E','F'])

print(df.loc['A'])

print(type(df.loc['A']))