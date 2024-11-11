"""main"""

from os import system

from datasets.iris import DatasetIris
from utils.colors import Colors, colorize

system("cls")


iris = DatasetIris()

print(colorize("Iris dataset", Colors.BLUE))
print(iris.target_names)
