import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams
import scipy

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale

rcParams['figure.figsize'] = 8,4
plt.style.use('seaborn-whitegrid')

address = 'C:/School/side_projects/Intro-to-DataScience/DataSets/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg = cars.mpg
plt.plot(mpg)
plt.show()

print(cars[['mpg']].describe())

mpg_matrix = mpg.values.reshape(-1,1)
scaled = preprocessing.MinMaxScaler()
scaled_mpg = scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)
plt.show()

# no standardization
standardized_mpg = scale(mpg, axis=0, with_mean=False, with_std=False)
plt.plot(standardized_mpg)
plt.show()

standardized_mpg = scale(mpg)
plt.plot(standardized_mpg)
plt.show()
