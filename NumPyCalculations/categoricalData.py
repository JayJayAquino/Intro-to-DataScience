import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)



address = 'C:/School/side_projects/Intro-to-DataScience/DataSets/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.index = cars.car_names
print(cars.head(15))
print(' ')

carb = cars.carb
print(carb.value_counts())
print(' ')

cars_cat = cars[['cyl', 'vs', 'am', 'gear', 'carb']]
print(cars_cat.head())

gears_group = cars_cat.groupby('gear')
print(gears_group.describe())
print(' ')

cars['group'] = pd.Series(cars.gear, dtype="category")
print(cars['group'].dtypes)
print(cars['group'].value_counts())
print(' ')

print(pd.crosstab(cars['am'], cars['gear']))
