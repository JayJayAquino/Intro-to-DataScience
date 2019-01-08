import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

# plt.plot(x,y)
# plt.show()

#path for sample Data
address = 'C:/Users/JayJay/Desktop/CompSciProjects/dataScience/dataSets/mtcars.csv'
#create DataFrame
cars = pd.read_csv(address)

cars.columns = ['cars_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars['mpg']
# mpg.plot()
# plt.show()

df = cars[['cyl', 'wt', 'mpg']]
# df.plot()
# plt.show()

# plt.bar(x,y)
# plt.show()
#
# mpg.plot(kind='bar')
# plt.show()

# for horizontal
# mpg.plot(kind='barh')
# plt.show()

x = [1,2,3,4,0.5]
plt.pie(x)
plt.show()

# to save graphs use
# plt.savefig('pie_chart.jpeg')
# plt.show()
# saves to working directory
