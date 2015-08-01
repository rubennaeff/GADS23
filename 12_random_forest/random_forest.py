"""
Simple implementation of Random Forest classification

@author Ruben Naeff - rubennaeff@gmail.com
August 2015
"""

from collections import defaultdict
import numpy as np


def entropy(y):
    """Given class labels `y`, compute the entropy of the set.
    Used by the ID3, C4.5 and C5.0 tree-generation algorithms"""
    classes = np.unique(y)
    p = np.array([(y == label).mean() for label in classes])
    return -np.nan_to_num(p * np.log2(p)).sum()


def gini(y):
    """Given class labels `y`, compute the Gini impurity of the set. Used by the CART algorithm
    (i.e., classification and regression tree). NB Not to be confused with Gini coefficient."""
    classes = np.unique(y)
    p = np.array([(y == label).mean() for label in classes])
    return 1 - np.square(p).sum()


class DecisionTree():
    """A decision tree classifier.
    :param criterion: string, optional (default="gini")
        The function to measure the quality of a split. Supported criteria are
        "gini" for the Gini impurity and "entropy" for the information gain.
    :param max_features: int, float, string or None, optional (default="auto")
        The number of features to consider when looking for the best split:
        - If int, then consider `max_features` features at each split.
        - If float, then `max_features` is a percentage of `n_features`
        - If "auto" or "sqrt", then `max_features=sqrt(n_features)`.
        - If None, then `max_features=n_features`.

    """
    def __init__(self, criterion='gini', max_features='sqrt'):
        self.tree = {}
        self.max_features = max_features
        self.criterion = criterion
        self._cost = dict(entropy=entropy, gini=gini)[criterion]

    def fit(self, X, y):
        """Build the decision tree.
        :param X: feature matrix, dataframe or 2-dimensional numpy ndarray
        :param y: class labels, series or numpy ndarray
        """

        def find_best_split(X, y, cost=entropy):
            """X and y are resp. a matrix and a vector, and should be an np.ndarrays"""
            best_feature, best_cutoff, best_gain = -1, -1, -1
            n_samples, n_features = X.shape
            for feature in xrange(n_features):
                indices = defaultdict(set)
                for i in xrange(n_samples):
                    indices[X[i, feature]].add(i)
                thresholds = sorted(indices.keys())[:-1]  # bigger than biggest makes no sense
                parent_cost = cost(y)  # either entropy or gini
                child1, child2 = set(xrange(len(y))), set([])
                for cutoff in thresholds:
                    child1 -= indices[cutoff]  # child1 <= cutoff
                    child2 = child2.union(indices[cutoff])  # child2 > cutoff
                    n1 = float(len(child1))
                    new_cost = n1 / n_samples * cost(y[list(child1)]) \
                        + (n_samples - n1) / n_samples * cost(y[list(child2)])
                    gain = parent_cost - new_cost
                    if new_cost == 0:  # if perfect split, stop immediately at this feature
                        return feature, cutoff, gain
                    elif gain > best_gain:
                        best_feature, best_cutoff, best_gain = feature, cutoff, gain

            return best_feature, best_cutoff, best_gain

        def split(X, y, max_features):
            """X and y are resp. a matrix and a vector, and should be an np.ndarrays"""
            if len(np.unique(y)) == 1:
                node = {'leaf': y[0]}
            else:
                n_samples, n_features = X.shape  # pick m random features
                new_features = np.random.choice(n_features, max_features, replace=False)
                feature, cutoff, gain = find_best_split(X[:, new_features], y)
                feature = new_features[feature]
                node = dict(feature=feature, cutoff=cutoff, gain=gain)
                idx = X[:, feature] > cutoff
                n1 = idx.sum()
                if 0 < n1 < n_samples:  # if really a split
                    node['bigger'] = split(X[idx], y[idx], max_features)  # child 1
                    node['smaller'] = split(X[~idx], y[~idx], max_features)  # child 2
                else:  # if features are equal, but labels are not
                    uniques, counts = np.unique(y, return_counts=True)
                    node['leaf'] = uniques[counts.argmax()]  # pick majority vote of what's left
                    # node['leaf'] = y.mean() > .5
            return node

        self.features = None
        if hasattr(X, 'columns'):
            self.features = X.columns

        X, y = np.array(X), np.array(y)
        self.n_samples, self.n_features = X.shape
        if self.max_features is None:
            max_features = self.n_features
        elif isinstance(self.max_features, int):
            max_features = max(1, min(self.n_features, max_features))
        elif isinstance(self.max_features, float):
            max_features = max(1, min(self.n_features, int(np.round(
                self.n_features * max_features))))
        elif self.max_features.lower() in ['sqrt', 'auto']:
            max_features = max(1, min(self.n_features, int(np.round(
                np.sqrt(self.n_features)))))
        elif self.max_features.lower() in ['log2']:
            max_features = max(1, min(self.n_features, int(np.round(
                np.log2(self.n_features)))))

        self.tree = split(X, y, max_features)
        return self

    def predict(self, X):

        def _predict(X, node):
            if 'leaf' in node:
                return np.array([node['leaf']] * len(X))
            else:
                idx = X[:, node['feature']] > node['cutoff']
                y = np.array([None] * len(X))
                y[idx] = _predict(X[idx], node['bigger'])
                y[~idx] = _predict(X[~idx], node['smaller'])
                return y

        return _predict(np.array(X), self.tree)

    def score(self, X, y):
        return (self.predict(X) == y).mean()

    def count_nodes(self):

        def count(subtree):
            if subtree:
                return 1 + count(subtree.get("bigger")) + count(subtree.get("smaller"))
            else:
                return 0

        return count(self.tree)

    def to_str(self, indent=2):

        def _to_str(subtree=None):
            if 'leaf' in subtree:
                return str(subtree['leaf'])
            else:
                return "if [%s] > %f:  (+%f)\n" % \
                    (self.features[subtree['feature']], subtree['cutoff'], subtree['gain']) + \
                    spaces + _to_str(subtree['bigger']).replace("\n", "\n" + spaces) + "\n" + \
                    "else:\n" + \
                    spaces + _to_str(subtree['smaller']).replace("\n", "\n" + spaces)

        spaces = " " * indent
        if self.features is None:
            self.features = range(self.n_features)
        return _to_str(self.tree)


class RandomForest():
    """A random forest classifier.
    :param n_estimators: number of decision trees (default=10)
    :param criterion: string, optional (default="gini")
        The function to measure the quality of a split. Supported criteria are
        "gini" for the Gini impurity and "entropy" for the information gain.
    :param max_features: int, float, string or None, optional (default="auto")
        The number of features to consider when looking for the best split:
        - If int, then consider `max_features` features at each split.
        - If float, then `max_features` is a percentage of `n_features`
        - If "auto" or "sqrt", then `max_features=sqrt(n_features)`.
        - If None, then `max_features=n_features`.

    """
    def __init__(self, n_estimators=10, criterion='gini', max_features='sqrt'):
        self.n_estimators = n_estimators
        self.max_features = max_features
        self.criterion = criterion

    def fit(self, X, y):
        self.trees = []
        self.classes = list(set(y))
        self._scores = []
        X, y = np.array(X), np.array(y)
        self.n_samples, self.n_features = X.shape
        for no in xrange(self.n_estimators):
            tree = DecisionTree(max_features=self.max_features, criterion=self.criterion)
            idx = np.random.choice(self.n_samples, self.n_samples, replace=True)
            self.trees.append(tree.fit(X[idx], y[idx]))
            oob = list(set(xrange(self.n_samples)) - set(idx))
            self._scores.append((tree.predict(X[oob]) == y[oob]).mean())
        return self

    def predict_proba(self, X):
        self._y_preds = []
        self._y_preds = np.array([tree.predict(X) for tree in self.trees])
        return np.array([(self._y_preds == label).mean(axis=0) for label in self.classes]).T

    def predict(self, X):
        return np.array(self.classes)[np.argmax(self.predict_proba(X), axis=1)]

    def score(self, X, y):
        return (self.predict(X) == y).mean()
