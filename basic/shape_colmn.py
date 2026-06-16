"""
shape and colmn :
- before work with dataset, the user can required get the shape and name of colmns of the dataset.
- the pandas provide the functionality to identify the shape and name of colmns of the dataset.
- the DataFreme object has two attribute:
    1) shape
    2)columns

shape :
- the shape attribute return the shape of dataset in the form of tuple.
- (row,colmn) 

columns :
- the columns attribute the return the name of all columns present in dataset and also dtype of columns. 
"""
# example :

import pandas as pd

#load the dataset
df= pd.read_csv("../../dataset/Sale Report.csv")
print(f"the original dataset is:\n {df}")

#use shape
print(f"the shape of dataset is: {df.shape}")

#use columns 
print(f"the colmns present in dataset:\n {df.columns}")