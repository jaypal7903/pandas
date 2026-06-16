"""
interpolition :
- interpolition is the technic of handle the missing values.
- iterpolition used to mathemathicsand stastistics method to fill the missing values with esstimated values.
- the interpolition used verious method's like linear,polynomian,time,quardratic,cubic etc..
- the interpolition technic is mainly used to works with time series data.
- pandas provide the interpolate() method to apply the interpolition technic.

interpolate() method:
- the three parameter pass in interpolate() method.
- first is the method to used the fill the esstimate value.
- second is the axis.
- third is the inplace.
"""

# example :

import pandas as pd
import numpy as np

df = pd.Series([10,20,np.nan,40,np.nan,60,70,np.nan,90,100])  #in Series data strcture axis parameter not exist.
print(df)

# linear method used
df.interpolate("linear",inplace=True)
print(f"after used interpolate method:\n{df}")