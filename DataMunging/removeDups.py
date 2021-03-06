import numpy as np
import pandas as pd
from pandas import Series, DataFrame

DF_obj = DataFrame({'column 1' : [1,1,2,2,3,3,3],
                    'column 2' : ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                    'column 3' : ['A', 'A', 'B', 'B', 'C', 'C', 'C']})

print(DF_obj)

# see what rows are duplicates
print(DF_obj.duplicated())

#drop duplicates
print(DF_obj.drop_duplicates())

DF_obj = DataFrame({'column 1' : [1,1,2,2,3,3,3],
                    'column 2' : ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                    'column 3' : ['A', 'A', 'B', 'B', 'C', 'D', 'C']})

print(DF_obj)

#specify what column ur interested in checking
print(DF_obj.drop_duplicates(['column 3']))
