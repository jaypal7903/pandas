"""
reading from the different formet :
- pandas provide the functionality to read the data from the different formet.
"""
# example:

import pandas as pd

#reading into the csv formet
df = pd.read_csv("data.csv")
print(f"rading data from the csv formet:\n {df}")

#reading into the excel file
df = pd.read_excel("data.xlsx")
print(f"reading data into the excel formet:\n {df}")

#reading data from the json formet
df = pd.read_json("data.json")
print(f"rading data from the json formet:\n {df}")