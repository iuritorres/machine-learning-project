""" Iris dataset module """

from pathlib import Path

import pandas as pd

from utils.colors import Colors, colorize


class DatasetIris:
    """Iris dataset class"""

    def __init__(self) -> None:
        self.data = []
        self.target = []

        self.feature_names = []
        self.target_names = []

        self.__load_dataset()

    def __load_dataset(self) -> None:
        """Load the iris dataset"""

        csv_path = f"{Path(__file__).parent}\\iris_dataset.csv"
        df = pd.read_csv(csv_path)

        df["target"] = df["target"].str.slice(5)

        self.target_names = df["target"].unique().tolist()
        self.feature_names = df.columns[:-1]
        self.data = df.iloc[:, :-1].values
        self.target = df["target"].map(self.target_names.index)

    def get_class_name(self, target_value: int) -> str:
        """Get the class name for a given target value"""

        if not target_value in range(len(self.target_names)):
            raise IndexError(
                colorize("There is no class matching this target value.", Colors.RED)
            )

        return self.target_names[target_value]
