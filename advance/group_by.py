"""
group by :
- the group by is work as the join operation in sql.
- pandas provide the groupby() method.

groupby("column_name") :
"""

#example :

import pandas as pd

data ={
    "name" :["jaypal","john","jack","virat","mahi"],
    "salary" : [50000,70000,50000,12000,12000],
    "performance score" : [72,78,81,72,81]
}

df = pd.DataFrame(data=data)
print(f"the original dataset is:\n {df}")

#group the salary
grouped = df.groupby("salary")["performance score"].mean()
print(grouped)

# group the name 
grouped = df.groupby("name")["salary"].mean()
print(grouped)