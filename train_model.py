from sklearn.linear_model import Perceptron
import joblib
import numpy as np

X = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
y = np.array([0, 1, 1, 0])

model = Perceptron()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
