import numpy as np


def compute_function(a: float, b: float) -> float:
    """
    Computes the formula a ** 2 + b ** 3 + 10

    :a: First value
    :param b: Second value
    :return: Result
    """
    return np.power(a, 2) + np.power(b, 3) + 10 + 40
