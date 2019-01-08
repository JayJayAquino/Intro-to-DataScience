import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#path for sample Data
address = 'C:/Users/JayJay/Desktop/CompSciProjects/dataScience/dataSets/mtcars.csv'
#create DataFrame
cars = pd.read_csv(address)

cars.columns = ['cars_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
# print(cars.head())

cars_groups = cars.groupby(cars['cyl'])
print(cars_groups.mean())
