"""
Simple neural net implementation using backprogagation

Based on example and code by

    Mark Holt, General Assembly Data Science, NYC #22
    https://github.com/ga-students/GADS-22-NYC
    https://github.com/ga-students/GADS-22-NYC/blob/master/22_Neural_Networks/DEMO-NeuralNetwork_Iris.ipynb

Edited by Ruben Naeff
"""

import numpy as np


class NeuralNet(object):
    """Implements a basic neural network"""

    def __init__(self, hidden=10, eta=.01, max_iter=100, eps=5., lam=.0):

        self.nn_hidden = hidden  # number of hidden units
        self.eta = eta  # learning rate
        self.lam = lam  # weight decay parameter
        self.iterations = max_iter  # number of iterations
        self.epsilon = eps  # weights initialization parameters

        # initialize number of classes, the number of features, etc.
        self.nn_classes = 0
        self.nn_features = 0
        self.targets = 0
        self.weights_1 = 0
        self.weights_2 = 0
        self.nn_train = 0
        self.training_mse = []
        self.testing_mse = []
        self.min_mse = 0.0
        self.final_n = 0

    def activation(self, z):
        """Activiation function: just the sigmoid or logistic function"""
        return 1. / (1. + np.exp(-z))

    def calc_Ak(self, A, k, nn_out):
        '''This is the implementation of softmax'''
        sum_k = 0.0
        for kprime in xrange(nn_out):
            if k != kprime:
                sum_k += np.exp(A[kprime])
        return A[k] - np.log(sum_k)

    def calc_se(self, y, t):
        '''Calculates one half times the squared error'''
        temp = (y - t) * (y - t)
        return 0.5 * temp.sum()

    def retrieve_final_n(self):
        return self.final_n

    def retrieve_min_mse(self):
        return self.final_n

    def retrieve_weights(self):
        return (self.weights_1, self.weights_2)

    def retrieve_training_mse(self):
        return self.training_mse

    def retrieve_testing_mse(self):
        return self.testing_mse

    def convert_to_yhat(self, t):
        y_hat = np.zeros((len(t)))
        for i in xrange(len(t)):
            y_hat[i] = t[i].argmax()
        return y_hat

    def convert_to_binary(self, y):
        targets = np.zeros((len(y), self.nn_classes))
        for i, j in enumerate(y):
            targets[i][j] = 1.0
        return targets

    def fit(self, X, y):
        '''Fits a neural network to the training set X'''

        self.nn_classes = len(np.unique(y))  # number of unique class identifiers in y
        self.targets = self.convert_to_binary(y)

        self.nn_train = X.shape[0]
        self.nn_features = X.shape[1]

        nn_input = np.zeros((1, self.nn_features + 1))
        nn_input_2 = np.zeros((1, (self.nn_hidden + 1)))

        # self.weights_1 = np.zeros((self.nn_features+1, self.nn_hidden))
        self.weights_1 = ((np.random.rand((self.nn_features + 1) * self.nn_hidden)
                          * 2.0 * self.epsilon) - self.epsilon) \
            .reshape(self.nn_features + 1, self.nn_hidden)

        # self.weights_2 = np.zeros((self.nn_hidden+1, self.nn_classes))
        self.weights_2 = ((np.random.rand((self.nn_hidden + 1) * self.nn_classes)
                          * 2.0 * self.epsilon) - self.epsilon) \
            .reshape(self.nn_hidden + 1, self.nn_classes)

        pre_out = np.zeros((1, self.nn_classes))
        training_mse = []

        for n in xrange(self.iterations):
            mse = 0.0
            if (n > 0) & (n % 100 == 0):
                print '.',
            for r in xrange(self.nn_train):
                nn_input[0, 1:] = X[r, :]  # get input vector from the training set
                nn_input[0][0] = 1.0  # set the bias to 1.0
                A_1 = np.dot(nn_input, self.weights_1)  # mulitply with the matrix of weights
                A_1 = self.activation(A_1)  # calculate the activation function
                Z1 = A_1 * (1.0 - A_1)  # calculate the derivative - anticipating backprogagation
                nn_input_2[0, 1:] = A_1  # A_1 is the input into the next layer
                nn_input_2[0][0] = 1.0  # set the bias for the next layer
                A_2 = np.dot(nn_input_2, self.weights_2)  # multiply with matrix of weights

                # Compute the 'soft max' so that each output will be a probability
                # and that all outputs sum to 1
                for k in xrange(self.nn_classes):
                    pre_out[0][k] = self.calc_Ak(A_2[0], k, self.nn_classes)
                n_outputs = self.activation(pre_out)
                delta2 = n_outputs - self.targets[r]  # calculate the ouput layer delta
                mse += self.calc_se(n_outputs[0], self.targets[r])
                BP2 = np.dot(delta2, self.weights_2.T)  # backpropagate the error
                BP2 = BP2[:, 1:].copy()  # Biases do not need to be updated
                delta1 = BP2 * Z1  # Calculate the delta at the hidden layer

                for i in xrange(self.nn_features + 1):
                    for j in xrange(self.nn_hidden):
                        self.weights_1[i][j] += \
                            -(self.eta * delta1[0][j] * nn_input[0][i]) \
                            - (self.eta * self.lam * self.weights_1[i][j])

                for i in xrange(self.nn_hidden + 1):
                    for j in xrange(self.nn_classes):
                        self.weights_2[i][j] += \
                            -(self.eta * delta2[0][j] * nn_input_2[0][i]) \
                            - (self.eta * self.lam * self.weights_2[i][j])

            mse = mse / self.nn_train
            training_mse.append(mse)
        self.training_mse = training_mse

    def predict(self, X):
        nn_classes = self.weights_2.shape[1]
        nn_hidden = self.weights_1.shape[1]
        nn_features = X.shape[1]

        nn_input = np.zeros((1, self.nn_features + 1))
        nn_input_2 = np.zeros((1, (nn_hidden + 1)))
        pre_out = np.zeros((1, nn_classes))

        all_outputs = np.zeros((X.shape[0], nn_classes))

        for r in xrange(X.shape[0]):
            nn_input[0, 1:] = X[r,:]
            nn_input[0][0] = 1.0

            A_1 = np.dot(nn_input, self.weights_1)

            nn_input_2[0, 1:] = self.activation(A_1)
            nn_input_2[0][0] = 1.0

            A_2 = np.dot(nn_input_2, self.weights_2)

            for k in xrange(nn_classes):
                pre_out[0][k] =  self.calc_Ak(A_2[0], k, nn_classes)
            n_outputs = self.activation(pre_out)
            all_outputs[r, :] = n_outputs

        return self.convert_to_yhat(all_outputs)

    def fit_es(self, X, y, Xv, yv):
        '''This function is fit early stopping. It is similar to fit but
        at each iteration of training it evaluates the mse on the provided validation set'''

        # set the number of classes to be the number of unique class identifiers in y
        self.nn_classes = len(np.unique(y))
        self.targets = self.convert_to_binary(y)
        test_targets = self.convert_to_binary(yv)

        self.nn_train = X.shape[0]
        self.nn_features = X.shape[1]

        nn_input = np.zeros((1, self.nn_features + 1))
        nn_input_2 = np.zeros((1, (self.nn_hidden + 1)))

        l_weights_1 = (np.random.rand((self.nn_features + 1) * self.nn_hidden) * 2.0 * self.epsilon
                       - self.epsilon).reshape((self.nn_features + 1), self.nn_hidden)
        l_weights_2 = (np.random.rand((self.nn_hidden + 1) * self.nn_classes) * 2.0 * self.epsilon
                       - self.epsilon).reshape((self.nn_hidden + 1), self.nn_classes)

        pre_out = np.zeros((1, self.nn_classes))
        training_mse = []
        testing_mse = []
        min_mse = 9.9e99  # big

        for n in xrange(self.iterations):
            mse = 0.0
            if (n > 0) & (n % 100 == 0):
                print '.',
            for r in xrange(self.nn_train):
                nn_input[0, 1:] = X[r, :]  # get the input vector from the training set
                nn_input[0][0] = 1.0  # set the bias to 1.0
                A_1 = np.dot(nn_input, l_weights_1)  # mulitply with the matrix of weights
                A_1 = self.activation(A_1)  # calculate the activation function
                Z1 = A_1 * (1.0 - A_1)  # calculate the derivative - anticipating backprogagation
                nn_input_2[0, 1:] = A_1  # A_1 is the input into the next layer
                nn_input_2[0][0] = 1.0  # set the bias for the next layer
                A_2 = np.dot(nn_input_2, l_weights_2)  # multiply with the matrix of weights

                # compute the 'soft max' so that each output will be a probability and that
                # all outputs sum to 1
                for k in xrange(self.nn_classes):
                    pre_out[0][k] = self.calc_Ak(A_2[0], k, self.nn_classes)
                n_outputs = self.activation(pre_out)

                # keep a running total of the squared error for each training example
                mse += self.calc_se(n_outputs[0], self.targets[r])

                # The output layer delta is just the output - the target
                delta2 = n_outputs - self.targets[r]

                # backpropagate the delta by multiplying the output delta (delta 2 by the weights
                # matrix transposed)
                BP2 = np.dot(delta2, l_weights_2.T)
                BP2 = BP2[:,1:].copy()

                # calculate the delta at the hidden layer
                delta1 = BP2 * Z1

                # use the derivative information to update the weights. lam is the regularizer
                # to keep the weights from becoming too large eta is the learning rate
                for i in xrange(self.nn_features + 1):
                    for j in xrange(self.nn_hidden):
                        l_weights_1[i][j] += \
                            -(self.eta * delta1[0][j] * nn_input[0][i]) \
                            - (self.eta * self.lam * l_weights_1[i][j])

                for i in xrange(self.nn_hidden + 1):
                    for j in xrange(self.nn_classes):
                        l_weights_2[i][j] += \
                            -(self.eta * delta2[0][j] * nn_input_2[0][i]) \
                            - (self.eta * self.lam * l_weights_2[i][j])

            mse = mse / self.nn_train  # get the training mean squared error
            training_mse.append(mse)  # append this to the training list

            # use the predict early stopping routine to get the validation mean squared error
            test_mse = self.predict_es(Xv, yv, l_weights_1, l_weights_2)
            testing_mse.append(test_mse)  # append this to the validation list

            # record the minimum validation mean squared error
            if test_mse < min_mse:
                min_mse = test_mse
                self.min_mse = test_mse
                self.weights_1 = l_weights_1.copy()
                self.weights_2 = l_weights_2.copy()
                self.final_n = n

        # ensure the list of the training and validation mse's are available
        self.training_mse = training_mse
        self.testing_mse = testing_mse

    def predict_es(self, X, y, w1, w2):
        '''This is the predict function used internally by the class to get a validation set
        mean squared error at the end of each iteration of training'''
        test_targets = self.convert_to_binary(y)

        mse = 0.0
        nn_test = X.shape[0]
        nn_classes = w2.shape[1]
        nn_hidden = w1.shape[1]
        # nn_features = X.shape[1]

        nn_input = np.zeros((1, self.nn_features + 1))
        nn_input_2 = np.zeros((1, (nn_hidden + 1)))
        pre_out = np.zeros((1, nn_classes))
        all_outputs = np.zeros((nn_test, nn_classes))

        for r in xrange(nn_test):
            # forward propagate the validation example - this code is commented in fit
            nn_input[0, 1:] = X[r, :]
            nn_input[0][0] = 1.0
            A_1 = np.dot(nn_input, w1)
            nn_input_2[0, 1:] = self.activation(A_1)
            nn_input_2[0][0] = 1.0
            A_2 = np.dot(nn_input_2, w2)
            for k in xrange(nn_classes):
                pre_out[0][k] = self.calc_Ak(A_2[0], k, nn_classes)
            n_outputs = self.activation(pre_out)
            all_outputs[r, :] = n_outputs

            # accumulate the mean squared error for the validation set
            mse += self.calc_se(n_outputs[0], test_targets[r])

        # return the mean squared error for the validation set
        return mse / float(nn_test)
