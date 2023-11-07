# Import necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

np.random.seed(0)
X = np.random.rand(100, 1)
y = 2 * X + 1 + np.random.rand(100, 1)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Plot the data and regression line
plt.scatter(X, y, label='Data', color='b')
plt.plot(X, y_pred, label='Linear Regression', color='r')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
