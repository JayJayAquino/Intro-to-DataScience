import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')

address = "C:/School/side_projects/Intro-to-DataScience/DataSets/Superstore-Sales.csv"
df = pd.read_csv(address, encoding="ISO-8859-1", index_col='Order Date', parse_dates=True)
print(df.head())

df['Order Quantity'].plot()
plt.show()

df2 = df.sample(n=100, random_state=25, axis=0)
plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Store Sales')

df2['Order Quantity'].plot()
plt.show()
