import matplotlib.pyplot as plt
import numpy as np
from city_row_model import CityRawModel
import plotly.graph_objects as go

#CityModel performs regression analysis
# it receives x(data),y (regression),score  of regression analysis
# the model has to functions :  1 predict that performs prediction, 2. show regression - shows a graph
## defining self.model as regression model allows us to use regressors

class CityModel(CityRawModel):
    def __init__(self, city_name, x, y) :
        super().__init__(x, y)
        self.name = city_name[::-1] # Data set is in hebrew from left to right  therefore city_name has to apply -1  order

    def display(self, figure, regressors):
        figure.add_trace(go.Scatter(x=regressors.labels, y=self.data,
                                    mode='markers', name='Cases'))

        x_new = np.linspace(0, len(regressors.labels)-1, 100)
        y_new = super().predict(x_new[:, np.newaxis])
        value = np.concatenate(y_new, axis=0)  # TODO: find more effective way
        figure.add_trace(go.Line(x=regressors.labels, y=value, name='Prognosis'))


