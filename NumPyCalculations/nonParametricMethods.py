import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats import spearmanr

rcParams['figure.figsize'] = 8,4
plt.style.use('seaborn-whitegrid')

address = 'C:/School/side_projects/Intro-to-DataScience/DataSets/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
print(cars.head())

x = cars[['cyl', 'vs', 'am', 'gear']]
sb.pairplot(x)
plt.show()

cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']
spearmanr_coefficient, p_value = spearmanr(cyl,vs)
print('Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient))

spearmanr_coefficient, p_value = spearmanr(cyl,am)
print('Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient))

spearmanr_coefficient, p_value = spearmanr(cyl,gear)
print('Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient))

table = pd.crosstab(cyl, am)

from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square Statistic %0.3f p_value %0.3f' % (chi2,p))

table = pd.crosstab(cars['cyl'], cars['vs'])
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square Statistic %0.3f p_value %0.3f' % (chi2,p))

table = pd.crosstab(cars['cyl'], cars['gear'])
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square Statistic %0.3f p_value %0.3f' % (chi2,p))
