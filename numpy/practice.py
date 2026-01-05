import pandas as pd
import numpy as np
import random 


"""
                                          BASICS

"""
student = {
    "name": ["dikshit","rushal",np.nan,"nikhil"],
    "age": [22,np.nan,21,np.nan],
    "score": [98,87,np.nan,98]
}

df = pd.DataFrame(student)
print("-"*50)

print(df["age"]*2)
print("-"*50)


""" 

                                BEGINNING OF ISNULL AND SUM COMBO TO FIND NULL VALUE
"""
#boolean mask = isnull()
#counter = sum()




#to find from which column and row the value is null
print(df.isnull())
print("-"*50)


#to count how many null value in total are there in per row and column 
print(df.isnull().sum())
print(type(df.isnull().sum()))
print("-"*50)




"""

                             BEGINNING OF DROPNA & FILLNA
   use of dropna: is to remove the null value from the row and column
   use of fillna: is the replace the missing value with a statical value(mean, median, mode[most_frequent])
"""


remove_null_row = df.dropna(axis=0)
remove_null_column = df.dropna(axis=1)
""" in dropna: axis = 0 is in default """


print("remove row: ")
print(remove_null_row)
print("-"*50)

print("remove column: ")
print(remove_null_column)
print("-"*50)

smart_remove = df.dropna(subset=['score']) #only gives those dataframe which has non missing value
print(smart_remove)
print("-"*50)


value = random.randint(1,11)
fill_value = df.fillna(value)

print("Filled all value: ")
print(fill_value)
print("-"*50)

print("whole column dtypes: ")
print(df.dtypes)

print("\n name type: ")
print(df["name"].dtypes)



print("-"*50)
print("USING MEAN: ")
mean_age = df["age"].mean()
print("AGE FOUND USING MEAN: ",mean_age)

fill_mean = df.fillna(mean_age)
print(fill_mean)

print("-"*50)
print("USING MEDIAN: ")
median_age = df["age"].median()
print("AGE FOUND USING MEDIAN: ",median_age)

fill_median = df.fillna(median_age)
print(fill_median)
print("-"*50)




