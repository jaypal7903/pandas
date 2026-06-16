"""
Exploring dataset:
- before use the dataset we can knowledge about dataset like what types of data save in dataset.
- pandas provide the functionality to indentify the structure about dataset.
- pandas provide two method to identify the structure abot dataset:
    1) head()
    2) tail()

head() :
- the head method return by default first 5 of the dataset.
- we can pass the integer number in parameter that return the no. of rows of top of the dataset.

tail() :
- the tail method return by default last 5 row of the dataset.
- we can pass the integer number in parameter that return the no. of rows of bottom of the dataset.
"""

# example :
import pandas as pd

df = pd.read_csv("../../dataset/Sale Report.csv")
print(f"the orginal dataset is:\n {df}")

#get the first 5 rows
print(f"explore the dataset with head method:\n {df.head()}")

#get the no. of rows pass in the parameter
print(f"get no.of row pass with the number in head parameter:\n {df.head(15)}")

#get the last 5 rows
print(f"explore the dataset with tail method:\n {df.tail()}")

#get the no. of rows pass in the parameter of tail
print(f"get no. of rows pass the number in tail method parameter:\n {df.tail(9)}")