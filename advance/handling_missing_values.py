"""
handling missing values:
- the pandas provide the functinality to handle the missing values.
- the pandas provide the isnull(), fillna(), dropna() method to handle the missing values.

isnull() method :
- isnull() method is used to the detect the present missing values in dataset.
- it return the boolean values.

fillna() method :
- fillna() method is used the fill the missing with other values.

dropna() method :
- dropna() method is used the drop the missing values row or columns.
"""

# example :

import pandas as pd
import numpy as np

data = {
     "name" : ["jaypal","","dhoni","modi","akshay","ranveer","jethalal","smith","bhide","thor","ironman","black panther"],
    "city" : ["halvad","","ranchi","ahmedabad",None,"mumbai","gandhinagar","sidani","mumbai","ase-gard","new-york","wakanda"],
    "age" : [22,30,43,65,66,42,12,17,np.nan,30,31,33],
    "performace score" : [np.nan,12,67,98,89,45,44,64,63,56,78,np.nan]
}

df = pd.DataFrame(data)
print(f"the original dataset is:\n {df}")

#isnull() method
# print(f"after used of isnull method:\n{df.isnull()}")

# isnull().sum()    : return the count of the each column missing value
# print(f"after used of isnull with sum method:\n{df.isnull().sum()}")

# #handle the age column missing values
# df["age"].fillna(df["age"].mean(),inplace=True)
# print(f"after fill the mean of age in age column:\n {df}")

# print(df.isnull().sum())

# # handle the performance score column missing values
# df["performace score"].fillna(df["performace score"].mean(),inplace=True)
# print(df)

print(df.isnull().sum())

#dropna() method

# handle the name column missing value 
df["name"].dropna(axis=0,inplace=True)
print(df)