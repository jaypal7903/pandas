"""
information about dataset :
- the pandas provde the functionality get the information about dataset.
- the pandas provide two methods that give the information about dataset :
    1) info()
    2) describe()

info() :
- the info() method is return the various details about dataset like:
    - total no. of rows and total no. colmns in the dataset.
    - toal non-null count of each colmn.
    - dtypes of the each colmns.
    - memory usage of the dataset.

describe() :
- the describe() method works only those colmn that contains only numerical values.
- the describe() method return various details like :
    - total no. of count of each colmn.
    - mean value of each colmn.
    - minimum value of colmn.
    - std(standard deviation) of the colmn.
    - 25% (qutile-1) of the colmn.
    - 50% (qutile-2 or median) of the colmn.
    - 75% (qutile-3) of the colmn.
    - maximum value of the colmn.
"""
# example :

import pandas as pd

#looad the dataset
df = pd.read_csv("../../dataset/Sale Report.csv")
print(f"the original dataset is:\n {df}")

#use info() method
print(df.info())

# use describe() method
print(f"the details about those colmn that contain numerical values:\n {df.describe()}")