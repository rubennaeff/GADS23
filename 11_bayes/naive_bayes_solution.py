"""
Simple implementation of Naive Bayes algorithm for text classification

Goal of this exercise is to write a Naive Bayes text classifier.

You can check if your code works by typing on the command line:
    python naieve_bayes_exercise.py

@author Ruben Naeff - rubennaeff@gmail.com
July 2015
"""

import numpy as np
import pandas as pd


path_to_repo = "/Users/ruben/repo/personal/ga/DAT-23-NYC/"
trainingset = "data/insults/train-utf8.csv"


class NaiveBayes():
    """Class for applying a naive bayes algorithm for text classification"""

    def __init__(self):
        """Setup useful datastructures. Feel free to change this."""

        self._classes = []  # list of all labels (i.e., classes)
        self._word_counts = {}  # dictionary {word: {class: count of words in class}}
        self._class_counts = {}  # dictionary {class: count of class occurances in whole document}

    def fit(self, x, y):
        """Fit a Multinomial NaiveBayes model from the training set (x, y).
        :param x: array-like of strings (line of text or single document).
            e.g., "This is not an insult", "This is an insult, you moron"
        :param y: array-like of classes (e.g., 0, 1, "class1", "class2")
        :return: self
        """
        self._classes = list(set(y))  # Save all unique labels

        for comment, label in zip(x, y):
            # Update class counts: Increment count by 1, or set count to 1 if never seen before
            self._class_counts[label] = self._class_counts.get(label, 0) + 1

            for word in comment.split():
                # Update count for pair word & label
                if word not in self._word_counts:
                    self._word_counts[word] = {}
                self._word_counts[word][label] = self._word_counts[word].get(label, 0) + 1

        return self

    def _compute_class_probability(self, comment, label):
        """Compute probability of `comment` under class `label`
        :param comment: string (e.g., a line of text or single document)
        :return: float, class probability

        HINT: Often, multiplying many small probabilities leads to underflow (i.e., result zero).
              A common numerical trick is to compute the log probability.
              Remember, the log(p1 * p2 * p3) = log p1 + log p2 + log p3
        """

        # Naive Bayes:
        #   P(comment | label) = P(word-1 | label) * .. * P(word-N | label) * P(label)

        # For the prior P(label), we could use the relative frequency of the class overall
        prior = float(self._class_counts[label]) / sum(self._class_counts.values())
        log_prior = np.log(prior)  # make log for easy computation

        log_p = log_prior  # start with prior and adjust for each word

        for word in comment.split():
            # Compute P(word | label)
            if (word in self._word_counts) and (label in self._word_counts[word]):
                p_word = float(self._word_counts[word][label]) / self._class_counts[label]
                log_p_word = np.log(p_word)
                log_p += log_p_word  # adjust probability (add when logging instead of multiplying)
            else:  # What happens when we haven't seen word in c?
                pass  # Ignore it
                # Theoretically, that would mean p_word == 1
                # That is clearly nonsense, but that's also the naive part -- it seems to work
                # You could also try another strategy

        return np.exp(log_p)  # and return probability P(comment | label), instead of its log

    def _predict_instance(self, comment):
        """Return array of class predictions for one sample comment
        :param comment: string (a line of text or single document)
        :return: array[ float, float ... ] =  class probabilities
        """
        probabilities = \
            [self._compute_class_probability(comment, label) for label in self._classes]
        probabilities = [p / sum(probabilities) for p in probabilities]  # normalize, so sum = 1
        return probabilities

    def predict_proba(self, x):
        """Return array of class predictions for all samples in x
        :param x: array-like of strings (line of text or single document).
            e.g., "This is not an insult", "This is an insult, you moron"
        :return: [[float, float ... ], ...] = class probabilities per sample
        """
        return [self._predict_instance(instance) for instance in x]

    def predict(self, x):
        """Return the most likely class for each sample in x
        :param x: array-like of strings (line of text or single document).
            e.g., "This is not an insult", "This is an insult, you moron"
        :return: array[int] = class per sample
        """
        return [self._classes[np.argmax(probabilities)]
                for probabilities in self.predict_proba(x)]


def test_naive_bayes():
    """Test the NaiveBayes class with the insult trainingset"""
    data = pd.read_csv(path_to_repo + trainingset)
    model = NaiveBayes()
    model.fit(data.Comment, data.Insult)

    texts = ["This is not an insult", "You are a big moron", "You are a big stinking super moron",
             "I think moron is an interesting word"]
    for comment, label_pred, proba in zip(texts, model.predict(texts), model.predict_proba(texts)):
        print "%-40s is %s an insult" % (comment, ["not", "   "][label_pred]), proba


if __name__ == '__main__':
    test_naive_bayes()
