"""main"""

from os import system

from matplotlib import pyplot as plt

from datasets.iris import DatasetIris

system("cls")


iris = DatasetIris()

colors = ["#026842", "#57CC99", "#22577A"]

for target in set(iris.target):
    subset = iris.data[iris.target == target]

    plt.scatter(
        subset[:, 0],
        subset[:, 1],
        c=colors[target],
        label=iris.get_class_name(target),
    )

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris Dataset")

plt.legend(title="Classes")
plt.show()
