# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 23:40:00 2021

@author: evgeny
"""
# The structure of analysis :
# Getting data regarding number of patients by city
# Normalizing data, fixing mistakes
# Creating predictions for spreading rate per city

import io
import numpy as np
import matplotlib.pyplot as plt
import numpy.ma as ma
import pandas as pd
import requests
import platform
print('Python platform: {}'.format(platform.architecture()[0]))

from regressions import calculate_regression_params
from enumarated_dates import EnumeratedDates

# Check libraries' versions
print('{} version: {}'.format(np.__name__, np.__version__))
print('{} version: {}'.format(pd.__name__, pd.__version__))

#
# 1. Download the raw data into Dataframe
#   Note that it's a raw data in csv format and it differs from the data displayed
#   by Github at https://github.com/idandrd/israel-covid19-data/blob/master/CityData.csv
url = "https://raw.githubusercontent.com/idandrd/israel-covid19-data/master/CityData.csv"
s = requests.get(url).content
_df = pd.read_csv(io.StringIO(s.decode('utf-8')))

df = _df.fillna(0)
# Replace cells containing "-" with zeros
df.replace('-', 0., inplace=True)
# exctracting dates from dataframe via EnumeratedDates function
keys = df.keys()
dates = EnumeratedDates(keys[2:])
#Defining city _models for later use in regression functions

city_models = np.array([])
ndata = df.to_numpy()
model=np.array([])

#  First two rows are defined as 'City' and 'Population'. We skip them
#  we upload each row in ndata - dataframe that contains cities info into a function City model which  calculates regression
#  the function returns y, x, name, score
for row in ndata:
    model = calculate_regression_params(dates.indices, row[2:], row[0])
    city_models = np.append(city_models, model)

# defining 0.8 THRESHOLD score  as a  borderline
THRESHOLD = 0.8
# checking score with a  THRESHOlD
with dates:

    fig = plt.figure(figsize=(8,10))
    fig.suptitle('Infected spreads in most populated cities')

    for i in np.arange(0, 4):
        # %%
        if city_models[i].score > THRESHOLD:
            ax = fig.add_subplot(2, 2, i + 1)
            city_models[i].display(axe=ax, regressors=dates.labels)
        # %%
    plt.show()
