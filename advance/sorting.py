"""
sorting :
- sorting is the method to arange the data into ascendling or descendling order.
- pandas provide the sort_values() method to sort the data.

sort_values(by= ["column_name"],ascending=True/False,inplace=True/False) :
"""

# example :

import pandas as pd

df = pd.read_csv("data.csv")
print(f"the original data is:\n {df}")

df.sort_values(by=["name"],ascending=False,inplace=True)
print(f"after sorting:\n {df}")