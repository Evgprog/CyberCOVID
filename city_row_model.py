import matplotlib.pyplot as plt
import numpy as np

class CityRawModel:
    def __init__(self, data, regression_model, score):
        self.data = data
        self.model = regression_model
        self.score = score

    def predict(self, regressors):
        predictions = self.model.predict(regressors[:, np.newaxis])
        return predictions

    def __str__(self):
        return 'Score: {}. Regression Params. Intercept: {} Coefficient: {}'.format(self.score, self.model.intercept_[0],
                                                                                   self.model.coef_[0, 0])