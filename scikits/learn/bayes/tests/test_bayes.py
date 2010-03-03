import numpy as np
from scikits.learn.bayes.bayes import bayesian_ridge
from numpy.testing import assert_array_almost_equal

X = np.array([[1], [2]])
Y = np.array([1, 2])

def test_toy():
    w = bayesian_ridge(X, Y)
    assert_array_almost_equal(w, [1])