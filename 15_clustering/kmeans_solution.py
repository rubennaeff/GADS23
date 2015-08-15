"""
Simple implementation of K-Means clustering

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

        # define k clusters randomly around the center
        middle = X.mean(axis=0)
        noise = X.std(axis=0) / 3.
        centroids = middle + \
            noise * np.random.randn(self.k * self.n_features).reshape(self.k, self.n_features)

        labels = None
        best_score = np.inf
        self.history = [dict(score=None, labels=None, centroids=centroids)]
        for i in xrange(max_iter):
            new_labels, score = self._compute_labels_and_score(X, centroids)
            if (labels is not None) and (new_labels == labels).all():
                break  # model converged (didn't do anything), so break
            labels = new_labels
            centroids = self._compute_centroids(X, labels)
            self.history.append(dict(score=score, labels=labels, centroids=centroids))
            if score < best_score:
                best_score = score
                best_centroids = centroids

        self.centroids = best_centroids

        if i == max_iter:
            print "Warning: algorithm stopped but did not necssarily converge."

    def _compute_centroids(self, X, labels):
        return np.array([X[labels == label, :].mean(axis=0) for label in xrange(self.k)])

    def _compute_labels_and_score(self, X, centroids):
        distances = np.array([np.sqrt(np.square(X - centroid).sum(axis=1))
                              for centroid in centroids])
        labels = distances.argmin(axis=0)
        score = distances.min(axis=1).mean()
        return labels, score

    def predict(self, X):
        """Predict which to which clusters the data in X belongs"""
        return self._compute_labels_and_score(X, self.centroids)[0]

    def score(self, X):
        """Average distance to nearest cluster. Negative value, so that higher is better."""
        return -self._compute_labels_and_score(X, self.centroids)[1]
