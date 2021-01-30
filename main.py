# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 23:40:00 2021

@author: evgeny
"""
# Project's aims: To allow localizaton of quarantine policy measures due to early identification of covid spread
# Currently a more binary policy is being used where all or no cities are quarantied
# the measures for infectios deseace prevention were used on the number o admitted patients
# risk analysis is done on overall number of patients which were identified
# and earlier detection based on the  prediction of possible number off patients might allow a more proactive measure to take place
# The structure of analysis :
# Getting data regarding number of patients by city
# Normalizing data, fixing mistakes
# Creating predictions for spreading rate per city
# Using formula identified in the article x35
# Read me for GITHUB
# The code performs predictions of potential spread of covid 19 in Israil's cities
# The codes's structure consist of the following parts:
# 1. Data upload from a website that contains a history of patients dinamycs  per city
# 2. Data  insertion into a pandas dataframework
# 3. Cleaning and prepearing of dataframe for analysis
# 4. Creating several models and classes for linear regression analysis and predictions
# 5. Creating a trashold for data set on 08 score
# 5. Applying models for each city dataset

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
# 2. Prepare the downloaded data for further analysis
#
# We're going to calculate the regression params for each
#     city (row) in the dataset. The input for regression is
#      - the set (numpy array) of the infected cases for each date
#      - the dates as defined in DataFrame's first row.
#          Note that the dates were downloaded in "dates" format
#           and in order to serve as such input, the dates' values should be
#           converted to numbers (see step 2b)

# 2a. Throw out nan values and other mess from the downloaded DataFrame
#   Thanks to God, Pandas has built-in function for such a purpose
# Output of Step 2a: df (cleaned/prepared DataFrame)
df = _df.fillna(0)
# Replace cells containing "-" with zeros
df.replace('-', 0., inplace=True)
# 2b. Prepare the dates obtained from the DataFrame to participate in the regression:
# just enumerate all the dates, i.e. convert them to the running number
# Output: enumeratedDates array
keys = df.keys()
dates = EnumeratedDates(keys[2:])

# We're done with data preparation.
# let's see how it looks like
# print(df)

# 4. Calculate the model's parameters for all cities (rows)
# As an output of this step we have the regression coefficients for each city!!!
city_models = np.array([])
ndata = df.to_numpy()
model=np.array([])

#  First two rows are defined as 'City' and 'Population'. We skip them
#  we upload each row in ndata - dataframe that contains cities info into a function City model which  calculates regression
#  the function returns y, x, name, score
for row in ndata:
    model = calculate_regression_params(dates.indices, row[2:], row[0])
    city_models = np.append(city_models, model)

#print(city_models)
# regcalcul=np.array([])
# regcalcul= np.apply_along_axis(calculate_regression_params, 1, ndata )

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

# 5. Apply calculated regression model in order to predict the spread
#       of infected people for each city


# Never call file with Big letters
# To Do 1 " requerments for python pushing describes dependencies numpy version
# To Do 2 class inheretence  name from row (1)
# To do 3 new class creation logical regression
# to d 4 saving apply funtion results to array
# To do score
# to put function
