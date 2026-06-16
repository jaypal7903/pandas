"""
- pandas provide the functinality to add new column in dataset.
- the two ways to add new column in dataset.
- first way to directly write down the new column name in squre breaket.
- second way to use the insert method to add specific location of the column.
"""

# example :

import pandas as pd 

df = pd.read_csv("data.csv")
print(f"the original csv file is:\n {df}")

# inserting the new column in state way
df["salary"] = [50000,35000,45000,65000,61500,22500,11000,87000,100000,58000,63000,54854]

print(f"after inserting new column:\n {df}")

# use insert() method         df.insert(location,"column_name",values)
df.insert(0,"id",[10,20,30,40,50,60,70,80,90,100,110,120])

print(f"after inserting id column:\n {df}")