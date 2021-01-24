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
# Using formula identified in the artickle x35
import io
import numpy as np
import numpy.ma as ma
import pandas as pd
import requests

from city_model import CityModel
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

#
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
#print(df)


# 3. Calculate the regression model params
# The function below will be called for each city (row) in the prepared dataset
# Input: x - regressors (dates)
#        y - labels (infected people)
# Output: regression's parameters
def calculate_regression_params(x, y, name):
    from sklearn import linear_model
    from sklearn.model_selection import train_test_split

    model = linear_model.LinearRegression()
    #turning data into one row for analysis
    X = x.reshape(-1, 1)
    Y = y.reshape(-1, 1)

    # Split the dataset to training part and test part
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    print('Score: {}. Regression Params. Intercept: {} Coefficient: {}'.format(score, model.intercept_[0], model.coef_[0, 0]))

    return CityModel(y, model, name)




# 4. Calculate the model's parameters for all cities (rows)
# As an output of this step we have the regression coefficients for each city!!!
#

city_models = np.array([])
ndata = df.to_numpy()
for row in ndata:
    #  First two rows are defined as 'City' and 'Population'. We skip them
    model = calculate_regression_params(dates.indices, row[2:], row[0])
    city_models = np.append(city_models, model)

# TODO 3:
#call rows of ndata
# y of function
#function will bb called as long as there rows
#will get one parametr only of content of rows
def rows_calculate(y):
    city_name = y[0]
    model = linear_model.LinearRegression()
    #turning data into one row for analysis
    X = x.reshape(-1, 1)
    Y = y.reshape(-1, 1)

    # Split the dataset to training part and test part
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    print('Score: {}. Regression Params. Intercept: {} Coefficient: {}'.format(score, model.intercept_[0], model.coef_[0, 0]))

    return CityModel(y, model, name)

np.apply_along_axis(calculate_regression_params, 1, ndata )


with dates:
    for i in np.arange(0, 4):
        city_models[i].show_regression(dates.labels)


# 5. Apply calculated regresion model in order to predict the spread
#       of infected people for each city


















