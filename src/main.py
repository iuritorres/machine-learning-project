"""main"""

from os import system

from matplotlib import pyplot as plt

from datasets.iris import DatasetIris
from utils.colors import Colors, colorize

system("cls")


iris = DatasetIris()

X = iris.data[:, 0]
y = iris.data[:, 1]

plt.scatter(X, y, c=iris.target, cmap="viridis", label="Data")
# plt.plot(iris.data, y_pred, color='red', label='Linear Regression')

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris Dataset")

plt.legend()
plt.show()
