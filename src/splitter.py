from abc import ABC, abstractmethod

class Splitter(ABC):
    @abstractmethod
    def split_dataset(self, folder_name, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1, seed=42):
        """
        Split a dataset into training, validation, and test sets.

        Args:
            folder_name (str): The name of the dataset directory.
            train_ratio (float): Ratio of training set.
            val_ratio (float): Ratio of validation set.
            test_ratio (float): Ratio of test set.
            seed (int): Random seed for reproducibility. Default is 42. Put None for random seed.
        """
        pass