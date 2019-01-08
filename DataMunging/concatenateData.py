import numpy as np
import pandas as pd
from pandas import Series, DataFrame

DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
# print(DF_obj)
DF_obj2 = pd.DataFrame(np.arange(15).reshape(5,3))
# print(DF_obj2)

# concat both objects about their columns (more columns that originals)
# print(pd.concat([DF_obj, DF_obj2], axis=1))

# concat both objects about rows (more rows that originals)
# print(pd.concat([DF_obj, DF_obj2]))

# Dropping Data
# print(DF_obj.drop([0,2]))
# print(DF_obj.drop([0,2], axis=1))

# Adding Data
series_obj = Series(np.arange(6))
series_obj.name = "added_variable"
# print(series_obj)

var_added = DataFrame.join(DF_obj, series_obj)
# print(var_added)

# dont re-index
added_table = var_added.append(var_added, ignore_index=False)
print(added_table)

#allow re-indexing
added_table = var_added.append(var_added, ignore_index=True)
print(added_table)

# Sort by
DF_sorted = DF_obj.sort_values(by=[5], ascending=[False])
print(DF_sorted)
