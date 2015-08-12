"""
This file provides you with tools and a framework to quickly get you started
making predictions and winning the competition!

There are two places you could make a great impact

    1. Selecting and calibrating your model
    2. Selecting and creating your features

Good luck!

@author You!
@author Ruben Naeff - rubennaeff@gmail.com
August 2015
"""

from datetime import datetime
import numpy as np
import pandas as pd
import time

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, \
    ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cross_validation import train_test_split, cross_val_score


PATH_TO_DATA = "/Users/ruben/Downloads/"  # change this to your local path

TRAIN_FILE = PATH_TO_DATA + "train.csv"
TEST_FILE = PATH_TO_DATA + "test.csv"

NOW = datetime.now().strftime("%y%m%d_%H%M%S")  # get timestamp
SUBMISSION_FILE = PATH_TO_DATA + "submission_%s.csv" % NOW  # include timestamp for archiving


class KaggleCompetition():

    def __init__(self, train_file=TRAIN_FILE, test_file=TEST_FILE):
        """Load training set and test set from disk"""

        print "Loading %s..." % train_file
        self.train = pd.read_csv(train_file, index_col=0)
        print "Loading %s..." % test_file
        self.test = pd.read_csv(test_file, index_col=0)

        self.n_train, self.n_test = len(self.train), len(self.test)
        print "Loaded", self.n_train, "training samples and", self.n_test, "testing samples"

        # Just checking if you have indeed the right file
        if (self.n_train != 140272) or (self.n_test != 73290):
            raise ValueError("It seems like you have loaded the wrong datasets!")

# ------------------------------------------------------------------------------------ #
# You only need to worry about the code below here

    def setup_model(self):
        """Choose your favorite model and initialize it using your favorite parameters"""

        # kNN model: options include n_neighbors, weights='uniform'/'distance', etc.
        # model = KNeighborsClassifier()

        # Logistic Regression: inverse-regularization parameter C, with L1 or L2 norm
        # (big C leads to overfitting)
        model = LogisticRegression()

        # Naive Bayes: options include alpha for smoothing (see doc)
        # model = MultinomialNB()

        # Decision Trees and Random Forests: options include n_estimators (number of trees),
        # gini or entropy purtiy measures, pruning settings, etc.
        # model = DecisionTreeClassifier()  # one tree
        # model = RandomForestClassifier()  # random forest
        # model = ExtraTreesClassifier()  # random forest variation
        # model = AdaBoostClassifier()  # random forest variation
        # model = GradientBoostingClassifier()  # random forest variation

        # Support Vector Machines: inverse-regularization parameter C, with L1 or L2 norm
        # Kernels could be 'linear', 'poly', 'rbf', 'sigmoid', or 'precomputed'
        # Kernel 'poly' has option `degree`, kernel 'rbf' has option 'gamma', etc. (see doc)
        # model = LinearSVC()  # linear SVM
        # model = SVC()  # Gaussian kernel by default

        return model

    def extract_features(self, data, training=True):
        """Create additional features by adding columns to your dataset
        :param dataset: both training and test set
        :param training: if True, fit vectorizers, otherwise just transform
        :return: X, y  -- feature matrix and target values"""

        print "Extracting features from %s set..." % ['test', 'training'][training]

        # You can choose from the following columns (and you can make more, obviously)
        # all_columns = \
        #     ['PostId', 'PostCreationDate', 'OwnerUserId', 'OwnerCreationDate',
        #      'ReputationAtPostCreation', 'OwnerUndeletedAnswerCountAtPostTime',
        #      'Title', 'BodyMarkdown', 'Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5',
        #      'PostClosedDate', 'OpenStatus']

        # Add some simple basic feature for text metadata
        data["Title_n_char"] = data.Title.map(lambda x: len(x))
        data["Title_n_words"] = data.Title.map(lambda x: len(x.split()))
        data["Body_n_char"] = data.BodyMarkdown.map(lambda x: len(x))
        data["Body_n_words"] = data.BodyMarkdown.map(lambda x: len(x.split()))

        # Convert dates to datetime format, aggregate by year, compute ages
        # print "Converting dates to datetime format..."
        # data['PostCreationDate_dt'] = pd.to_datetime(data.PostCreationDate)
        # data['PostCreationDate_ord'] = data.PostCreationDate_dt.astype(int)  # just ordinal no
        # data['PostCreationDate_year'] = data.PostCreationDate_dt.dt.year
        # data["PostAge"] = (data.PostCreationDate_dt.max() - data.PostCreationDate_dt).dt.days

        # data['OwnerCreationDate_dt'] = pd.to_datetime(data.OwnerCreationDate)
        # data['OwnerCreationDate_ord'] = data.OwnerCreationDate_dt.astype(int)
        # data['OwnerCreationDate_year'] = data.OwnerCreationDate_dt.dt.year
        # data["OwnerAgeAtPosting"] = (data.PostCreationDate_dt - data.OwnerCreationDate_dt).dt.days

        # Maybe the number of tags is a good indicator of a post will be closed
        print "Counting number of tags per post..."
        data["n_tags"] = np.array([data["Tag%d" % i].notnull() for i in xrange(1, 6)]).sum(axis=0)

        # Create features for words in tags, title and body
        data['tags'] = data.apply(lambda x: " ".join(set(str(x['Tag%d' % i]) for i in xrange(1, 6))), axis=1)
        data['tags'] = data['tags'].str.replace('nan', '').str.replace("  ", " ").str.strip()

        if training:
            print "Creating features for each tag..."
            self.cv_tags = CountVectorizer(stop_words='english', ngram_range=(1, 1), max_features=5000)
            X_tags = self.cv_tags.fit_transform(data.tags)
            print "Creating features for post titles..."
            self.cv_title = CountVectorizer(stop_words='english', ngram_range=(1, 3), max_features=3000)
            X_title = self.cv_title.fit_transform(data.Title)
            print "Creating features for post body texts..."
            self.cv_body = CountVectorizer(stop_words='english', ngram_range=(1, 3), max_features=3000)
            X_body = self.cv_body.fit_transform(data.BodyMarkdown)
        else:
            X_tags = self.cv_tags.transform(data.tags)
            X_title = self.cv_title.transform(data.Title)
            X_body = self.cv_body.transform(data.BodyMarkdown)

        # ....
        # You could do much, much more to improve your score here
        # Add and create more features (including parsing the text columns)
        # Select and calibrate your model (see above)
        # ....

        # Include the following columns in your feature matrix
        features = \
            ['OwnerUserId', 'ReputationAtPostCreation', 'OwnerUndeletedAnswerCountAtPostTime',
             'Title_n_char', 'Title_n_words', 'Body_n_char', 'Body_n_words',
             # 'PostCreationDate_ord', 'PostCreationDate_year',
             # 'PostAge',
             # 'OwnerCreationDate_ord', 'OwnerCreationDate_year',
             # 'OwnerAgeAtPosting',
             'n_tags']

        # Create feature matrix
        # X = data[features]
        X = np.hstack([data[features], X_tags.toarray(), X_title.toarray(), X_body.toarray()])
        # X = np.hstack([data[features], X_tags.toarray()])

        if training:
            return X, data.OpenStatus
        else:
            return X

# ------------------------------------------------------------------------------------ #
# You don't need to do much below here

    def make_predictions(self, model, X_train, y_train, X_test, submission_file=SUBMISSION_FILE):
        """Train model on training set and make predictions for the test set.
        Then save predictions to disk."""

        if self.n_test != len(X_test):
            raise ValueError("Somewhere along the way you lost test samples! Please fix.")

        print "Training %s using %d samples (%d%% of original training set)" % \
            (model.__class__.__name__, len(X_train), 100. * len(X_train) / self.n_train)
        model.fit(X_train, y_train)

        print "Making predictions on the test set.."
        # We want the probabilities, not just 0 or 1. Just take 2nd column
        y_pred = model.predict_proba(X_test)[:, 1]

        print "Cross-validating model..."
        scores = cross_val_score(model, X_train, y_train, cv=3, scoring="roc_auc")
        print "Cross-validated AUC score: %.4f  (%s)" % (scores.mean(), scores.round(4))

        print "Saving predictions in %s..." % submission_file
        submission = pd.DataFrame(dict(id=self.test.index, OpenStatus=y_pred)).set_index('id')
        submission.to_csv(submission_file)


def main():
    start_time = time.time()
    kaggle = KaggleCompetition()
    X_train, y_train = kaggle.extract_features(kaggle.train)
    X_test = kaggle.extract_features(kaggle.test, training=False)
    model = kaggle.setup_model()
    kaggle.make_predictions(model, X_train, y_train, X_test)
    duration = time.time() - start_time
    print "Done! That took %dm%02ds" % (duration / 60, int(duration) % 60)


if __name__ == "__main__":
    main()
