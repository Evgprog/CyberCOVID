from city_model import  CityModel

# 3. Calculate the regression model params
# The function below will be called for each city (row) in the prepared dataset
# Input: x - regressors (dates)
#        y - labels (infected people)
# Output: regression's parameters

# class TFLinearRegression:
#     def __init__(self):
#         self.m = tf.Variable(0.) #   coefficient variable
#         self.b = tf.Variable(0.) #  error variable
#
#     def mse(self, y_true, y_predicted):
#         return tf.reduce_mean( tf.square(y_true - y_predicted) ) #  calculating error size between existin and predicted value
#     #     def predict(self, x):
#         return tf.reduce_sum(self.m * x + self.b) # calculating linear formula
#
#     def update(self, x, y, learning_rate): #
#         with tf.GradientTape() as tape:
#             loss = self.mse(y, self.predict(x))
#
#             gradients  = tape.gradient(loss, [self.m, self.b])
#
#             self.m.assigm_sub(learning_rate * gradients[0])
#             self.b.assign_sub(learning_rate * gradients[1])

def calculate_regression_params(x, y, name):
    from sklearn import linear_model
    from sklearn.model_selection import train_test_split
    model = linear_model.LinearRegression()
    # turning data fit for the regression analysis
    X = x.reshape(-1, 1)
    Y = y.reshape(-1, 1)
    # Split the dataset to training part and test part
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)

    # returning data from a citymodel with y, x, and name
    _model = CityModel(data=y, regression_model=model, city_name=name, score=score)
    print(_model)
    return _model