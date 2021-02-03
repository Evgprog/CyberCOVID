from sklearn import linear_model
from sklearn.model_selection import train_test_split


# we import dates and results of regression model with the score
class CityRawModel:
    def __init__(self, x, y):
        self.model = linear_model.LinearRegression()
        # turning data fit for the regression analysis
        X = x.reshape(-1, 1)
        Y = y.reshape(-1, 1)

        # splitting the dataset to training part and test part
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
        self.model.fit(x_train, y_train)
        score = self.model.score(x_test, y_test)

        self.data = y
        self.score = score

    def predict(self, regressors):
        predictions = self.model.predict(regressors)
        return predictions

    def __str__(self):
        return 'Score: {}. Regression Params. Intercept: {} Coefficient: {}'.format(self.score, self.model.intercept_[0],
                                                                                   self.model.coef_[0, 0])