import math

def validateSplit(train: float, val: float, test: float):
    """
    Validate the split ratios.

    Args:
        train (float): Ratio of training set.
        val (float): Ratio of validation set.
        test (float): Ratio of test set.
    """
    if not math.isclose(train + val + test, 1.0, rel_tol=1e-9):  
        raise ValueError("The sum of train, val, and test ratios must be 1. You entered: train={}, val={}, test={}".format(train, val, test))
    if train < 0 or val < 0 or test < 0:
        raise ValueError("Ratios must be non-negative. You entered: train={}, val={}, test={}".format(train, val, test))
    if train == 0 or val == 0 or test == 0:
        raise ValueError("Ratios must be positive. You entered: train={}, val={}, test={}".format(train, val, test))
    return True
