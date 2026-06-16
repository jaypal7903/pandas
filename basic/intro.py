"""
pandas :
- pandas is the python library that helps to the data manuplation(like modify, remove and transform) and data analysis.
- pandas provide the functionality to read the data in the different formet of file(like excel,csv,json).
-the pandas has mainly two type of data structure:
    1) Series
    2)DataFrame

Series :
- Series is the one-dimensional array that store the any type of data like object,number etc.
- in Series, every element of Series has one unique label like index.

DataFrame :
- DataFrame is the two-dimensional array that store the data like table in sql.
- in DataFrame ,every row of DataFrame has one unique lablel like index.
"""
#import pandas

import pandas as pd

# create a dict
data = {
    "name" : ["jaypal","virat","dhoni","modi","akshay","ranveer","jethalal","smith","bhide","thor","ironman","black panther"],
    "city" : ["halvad","delhi","ranchi","ahmedabad","mumbai","mumbai","gandhinagar","sidani","mumbai","ase-gard","new-york","wakanda"],
    "age" : [22,30,43,65,66,42,12,17,20,30,31,33],
    "performace score" : [90,12,67,98,89,45,44,64,63,56,78,76]
}

print(f"before convert into dataframe:\n{data}")

#convert into DataFrame
df = pd.DataFrame(data=data)
print(f"after convert into dataframe:\n {df}")

#save to the csv forment
df.to_csv("data.csv",index=False)

#save the excel formet
df.to_excel("data.xlsx",index=False)

#save the json formet
df.to_json("data.json",index=False)