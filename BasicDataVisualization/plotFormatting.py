import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

import seaborn as sb

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]

# plt.bar(x,y)
# plt.show()

wide = [0.5,0.5,0.5,0.9,0.9,0.9,0.5,0.5,0.5]
color = ['salmon']
plt.bar(x,y,width=wide,color=color,align='center')
plt.show()

#path for sample Data
address = 'C:/Users/JayJay/Desktop/CompSciProjects/dataScience/dataSets/mtcars.csv'
#create DataFrame
cars = pd.read_csv(address)
cars.columns = ['cars_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'mpg', 'wt']]
df.plot()
plt.show()
