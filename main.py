# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 23:40:00 2021

@author: evgeny
"""
# Project's aims:
# Prediction of COVID 19 patients number in Israeli cities.
# DATA SOURCE:
# The data set taken from Israeli Health ministry and was uploaded from :
# https://raw.githubusercontent.com/idandrd/israel-covid19-data/master/CityData.csv
# Project's value:
# Early identification potential of Covid 19 spread in certain Israeli city.
# Earlier detection should allow a more proactive measures to take place in order to stop the spread of Covid 19

# Code structure:
# 1. Getting data regarding number of patients by city from github dataset
# 2. Normalizing data, fixing mistakes
# 3. Creating functions for dash, models for dates, regression analysis
# 4. Creating predictions for spreading rate per city
# 5. Display the prediction spread by city chosen by user


import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

import io
import numpy as np
import matplotlib.pyplot as plt
import numpy.ma as ma
import pandas as pd
import requests

from city_model import CityModel
from enumarated_dates import EnumeratedDates

# 1. Prepare Dash framework
external_stylesheet = ['https://codepen.io/chrilddyp/pen/bWLwpP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

#
#DATAFRAME made of csv taken from url
url = "https://raw.githubusercontent.com/idandrd/israel-covid19-data/master/CityData.csv"
s = requests.get(url).content
_df = pd.read_csv(io.StringIO(s.decode('utf-8')))
#2.Prepearing data for analysis all 0
df = _df.fillna(0)
# Replacing cells containing "-" with zeros
df.replace('-', 0., inplace=True)
# Extracting dates as keys and extracting their indices
keys = df.keys()
dates = EnumeratedDates(keys[2:])

# TODO: change np.array to Python list with the following structure
# creating dash : creating list of cities and indices for Combobox
# { name: 'Tel-Aviv',
#   rowId: 'from DataFrame
# }
city_models = [{
    "name" : "Jerusalem",
    "rowId": 0
},
{
    "name": "Tel-Aviv",
    "rowId": 1
}]

app.layout = html.Div(children=[
    html.H1(children='CyberCOVID'),
    html.Div([
        dcc.Dropdown(
            id='city-name-dropdown',
            options=[
                {"label": x['name'], "value": x['rowId']} for x in city_models
            ]
        ),
        html.Div(id='dd-output-container'),
        dcc.Graph(id='city-graph')
    ])
])

@app.callback(
    dash.dependencies.Output(component_id='city-graph', component_property='figure'),
    [dash.dependencies.Input('city-name-dropdown', 'value')]
)
def city_changed(row_id):

    fig = go.Figure(layout=go.Layout(width=1200, height=400))

    # TODO: find the element in DataFrame with row_id selected from the combo-box
    try:
        row  = df.iloc[row_id].to_numpy()
    except TypeError:
        return fig
    else:
        model = CityModel(city_name=row[0], x=dates.indices, y= row[2:])

        fig.layout.title = row[0]
        model.display(fig, regressors=dates)
        return fig

if __name__ == '__main__':
    app.run_server(debug=True)




