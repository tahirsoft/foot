import numpy as np

from parser import countries


def goals():
    score = np.random.choice(8, 2, p=[0.28, 0.25, 0.15, 0.12,
                                      0.1, 0.05, 0.04, 0.01])
    return score
