import numpy as np
import pandas as pd
from pandas import Series, DataFrame

missing = np.nan

series_obj = Series(['row 1', 'row 2', missing, 'row 4', 'row 5', 'row 6', missing, 'row 8'])
# print(series_obj)

# print(series_obj.isnull())

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
# print(DF_obj)

DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing
# print(DF_obj)

#manual fill all NaN
filled_DF = DF_obj.fillna(0)
# print(filled_DF)

#manual fill column then value for NaN
filled_DF = DF_obj.fillna({0:0.1, 5:1.25})
# print(filled_DF)

#if value is NaN, use most recelty used value to fill
fill_DF = DF_obj.fillna(method='ffill')
# print(fill_DF)

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing
print(DF_obj)

#for every column, return number of NaN
print(DF_obj.isnull().sum())

# if a row has any missing values, it gets dropped from the DF
DF_no_NaN = DF_obj.dropna()
print(DF_no_NaN)

# can pass in the axis = 1 to change the serach to 'by column' instead of 'by row'
DF_no_NaN = DF_obj.dropna(axis=1)
print(DF_no_NaN)

# drop data if entire row is NaN
# in this case nothing should be dropped
print(DF_obj.dropna(how='all'))
