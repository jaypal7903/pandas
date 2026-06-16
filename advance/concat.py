"""
concat :
- pandas provide the concat method to merge the more then one dataframe.

cancat([df1,df2],...,axis=0/1) :
where, df1 = dataframe 1,
       df2 = dataframe 2.
"""

# example :

import pandas as pd

data1 = {
    "id" : [1,2,3,4,5],
    "name" : ["jaypal","john","jack","virat","mahi"]
}

data2 = {
    "id" : [1,2,3,6,7],
    "performance score" : [98,67,52,45,65]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(f"the original dataframe is:\n {df1}\n second datafeame is:\n{df2}")

#row wise concat
df3 = pd.concat([df1,df2],axis=0)
print(f"after merging the new dataframe is:\n {df3}")

#column wise concat
df3 = pd.concat([df1,df2],axis=1)
print(f"after merging column wise:\n {df3}")