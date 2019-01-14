import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

rcParams['figure.figsize'] = 9,5
sb.set_style('whitegrid')

x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]

plt.bar(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

z = [1,2,3,4,0.5]
veh_type = ['bicycle','motorbike','car','van','stroller']
plt.pie(z,labels=veh_type)
plt.show()

address = 'C:/School/side_projects/Intro-to-DataScience/DataSets/mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg = cars.mpg

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars')
ax.set_xlabel('car names')
ax.set_ylabel('miles per gallon')
# plt.tight_layout() find out what this does
plt.show()

plt.pie(z)
plt.legend(veh_type, loc='best')
plt.show()

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars')
ax.set_xlabel('car names')
ax.set_ylabel('miles per gallon')

ax.legend(loc='best')
plt.show()

print(mpg.max())
ax2 = fig.add_axes([.1,.1,1,2])
mpg.plot()
ax2.set_title('Miles per Gallon of Cars in mtcars lol')
ax2.set_ylabel('miles per gallon oof')
ax2.set_ylim([0,45])

# arguments, string for annotation, xy to demark location you are annotating
# xytext specifies the location of annotation text to be placed, arrowprops specifies
# properties of arrow we are annotating
ax2.annotate('Toyota Corolla', xy=(19,33.9), xytext=(21,35), arrowprops=dict(facecolor='black',shrink=0.05))

plt.show()
