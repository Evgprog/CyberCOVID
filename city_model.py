import matplotlib.pyplot as plt
import numpy as np
from city_row_model import CityRawModel
#CityModel performs regression analysis
# it receives x(data),y (regression),score  of regression analysis
# the model has to functions : 1 predict that performs prediction, 2. show regression - shows a graph
## defining self.model as regression model allows us to use regressors

class CityModel(CityRawModel):
    def __init__(self, data, regression_model, city_name,score):
        super().__init__(data, regression_model, score)
        self.name = city_name[::-1] # Data set is in hebrew from left to right  therefore city_name has to apply -1  order


# 1 # linspace data and showing it as a plt
    def display(self, axe, regressors):

        axe.title.set_text(self.name)
        axe.scatter(regressors, self.data)

        x_new = np.linspace(0, 30, 100)
        y_new = super().predict(x_new[:, np.newaxis])
        axe.plot(x_new, y_new, color='red')

