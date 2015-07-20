"""
Simple implementation for k-Nearest Neighbors algorithm

@author Ruben Naeff - rubennaeff@gmail.com
November 2014
"""

import numpy as np


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
        # Save data in model. Convert to numpy arrays to avoid confusion
        self.X = np.array(X)
        self.y = np.array(y)
        # There's not much more we can do at this point..
        return self

    def predict(self, X):
        """
        Predict classes of samples.
        :param X: pandas dataframe or numpy ndarray with features
        """
        X = np.array(X)  # Convert X to ndarray, if it's not already
        predictions = []

        # Walk through every point of X, compute distance to all points in self.X
        for i in xrange(len(X)):
            distances = np.sqrt(np.square(self.X - X[i]).sum(axis=1))
            # distances.sort(ascending=True)  # Sort such that the nearest ones are at top
            k_nearest = self.y[np.argsort(distances)[:self.k]]  # Get class of k nearest neighbors
            classes, counts = np.unique(k_nearest, return_counts=True)
            predictions.append(classes[np.argmax(counts)])  # take most frequent class

        return np.array(predictions)

    def score(self, X, y):
        """
        Compute accuracy of predictions on X.
        :param X: pandas dataframe or numpy ndarray with features
        :param y: pandas series or numpy ndarray with true classes
        """
        return np.mean(self.predict(X) == y)
