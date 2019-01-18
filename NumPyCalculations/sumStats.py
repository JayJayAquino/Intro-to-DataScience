import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

url = 'https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/mtcars.csv'
cars = pd.read_csv(url)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
print(cars.head())
print(' ')
# sum of all columns
print(cars.sum())
print(' ')

# sum of all rows
# print(cars.sum(axis=1))
# print(' ')

# median
print(cars.median())
print(' ')

# mean or average
print(cars.mean())
print(' ')

# max
print(cars.max())
print(' ')

mpg = cars.mpg
# location of where max value was found
print(mpg.idxmax())
print(' ')

# standard deviation
print(cars.std())
print(' ')

# variance
print(cars.var())
print(' ')

gear = cars.gear
print(gear.value_counts())

# detail summary of data
print(cars.describe())
