import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

sea_level = pd.read_csv('epa-sea-level.csv')
plt.scatter('Year', 'CSIRO Adjusted Sea Level', data=sea_level)

slope, intercept, r, p, std_err = linregress(sea_level['Year'], sea_level['CSIRO Adjusted Sea Level'])


def regressionmodel(x):
    return intercept + (x * slope)


arr = np.arange(1880, 2051)
reg_model = list(map(regressionmodel, arr))
plt.plot(arr, reg_model, color='red')

condition = sea_level['Year'] >= 2000
sea_level = sea_level.loc[condition]
sea_level = sea_level.reset_index()
sea_level = sea_level.drop(columns='index')

slope2, intercept2, r2, p2, std_err2 = linregress(sea_level['Year'], sea_level['CSIRO Adjusted Sea Level'])
def regressionmodel2(x):
    return intercept2 + (x * slope2)


arr = np.arange(2000, 2051)
reg_model = list(map(regressionmodel2, arr))
plt.plot(arr, reg_model, color='purple')


plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.savefig('scatter_plot.png')
