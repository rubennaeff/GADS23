"""
Simple implementation for k-Nearest Neighbors algorithm

@author <your_name> - <your_email>
July 2015
"""


class kNN(object):
    """
    Class for simple k-Nearest Neighbors
    """

    def __init__(self, k=5):
        """
        Initialize model.
        :param k: number of Neighbors (the 'k' in kNN)
        """
        self.k = k

    def fit(self, X, y):
        """
        Fit model.
        :param X: pandas dataframe or numpy ndarray with features
        :param y: pandas series or numpy ndarray with classes
        """
        raise NotImplementedError

    def predict(self, X):
        """
        Predict classes of samples.
        :param X: pandas dataframe or numpy ndarray with features
        """
        raise NotImplementedError

    def score(self, X, y):
        """
        Compute accuracy of predictions on X.
        :param X: pandas dataframe or numpy ndarray with features
        :param y: pandas series or numpy ndarray with true classes
        """
        raise NotImplementedError

