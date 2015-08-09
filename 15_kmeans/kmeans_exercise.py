"""
Simple implementation of K-Means clustering

You'll need to complete three methods

    1. fit()
    2. _compute_centroids()
    3. _compute_labels_and_score()

@author Ruben Naeff - rubennaeff@gmail.com
August 2015
"""

import numpy as np


class KMeans():
    """Find k clusters in the given data
    NB Make sure your data is properly scaled!
    :param k: number of clusters to be found
    """
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, max_iter=100):
        """Find k clusters in the data X
        :param X: dataframe or numpu ndarray with n-dimensional data
        """
        X = np.array(X)  # concert to numpy array to be safe
        self.n_samples, self.n_features = X.shape

        # TODO
        # define k clusters randomly around the center
        # ....
        # ....
        centroids = None  # replace this

        # iterate:
        # - given centroids, compute labels for each point (and total score)
        # - given labels, compute centroids to be in the center of each cluster
        # repeat until labels do not change or max_iter has been reached
        # keep track of total score to make sure you return the best solution

        labels = None
        best_score = np.inf
        self.history = [dict(score=None, labels=None, centroids=centroids)]
        for i in xrange(max_iter):
            pass  # your code here...
            # labels, score = self._compute_labels_and_score(X, centroids)
            # centroids = self._compute_centroids(X, labels)

            # ...
            # ...

        if i == max_iter:
            print "Warning: algorithm stopped but did not necssarily converge."

    def _compute_centroids(self, X, labels):
        # TODO
        # Compute coordinates of the centers of each cluster
        # ...
        return None

    def _compute_labels_and_score(self, X, centroids):
        # TODO
        # Compute to which center the data is closest, and label accordingly
        # Also return score (average distance to closest cluster)
        # ...
        return labels, score

    def predict(self, X):
        """Predict which to which clusters the data in X belongs"""
        return self._compute_labels_and_score(X, self.centroids)[0]

    def score(self, X):
        """Average distance to nearest cluster. Negative value, so that higher is better."""
        return -self._compute_labels_and_score(X, self.centroids)[1]
