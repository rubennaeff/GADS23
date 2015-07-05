#!/usr/bin/env python
"""
Testing your kNN algorithm

Type on the command line:

    python knn_test.py

"""

import pandas as pd
from sklearn.cross_validation import train_test_split

from knn import kNN  # import algorithm


DATAFILE = '../data/iris/iris.csv'
HEADER = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
FEATURES = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']


def main():
    """Do a test if called from the command line"""
    data = pd.read_csv(DATAFILE, header=None, names=HEADER)
    X = data[FEATURES]
    y = data.species

    model = kNN(k=10)
    model.fit(X, y)
    print "Accuracy on training set:", model.score(X, y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.80)
    model.fit(X_train, y_train)
    print "Accuracy on test set:    ", model.score(X_test, y_test)


if __name__ == "__main__":
    main()
