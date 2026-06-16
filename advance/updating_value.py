"""
upadte the value :
- pandas provide the functinality to updating the value of specific position.
- pandas provide the .loc() method.
"""

# example :

import pandas as pd

df = pd.read_csv("data.csv")
print(f"the original csv file is:\n {df}")

# update the specific value 
df.loc[2,"age"] = 34
print(f"after updte the value:\n {df}")

# use iloc method
df.iloc[[2,2]] = 43
print(f"after use iloc mthod:\n {df}")

df.drop(columns=["age"],inplace=True)
print(df)