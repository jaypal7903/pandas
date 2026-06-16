"""
delete :
- pandas provide the functionality to drop the column.
"""

# exmple :
import pandas as pd

df = pd.read_csv("data.csv")
print(f"the original dataset:\n{df}")

df.drop(columns=["performace score","age"],inplace=True)
print(f"after delete the row:\n{df}")