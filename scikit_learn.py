from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x,y = make_regression(n_samples = 200 , n_features=1, noise = 30)
plt.scatter(x,y)
plt.show()

modelo = LinearRegression()

plt.scatter(x,y)
plt.plot(x, modelo.predict(x), color="red", linewidth=3)
plt.show()