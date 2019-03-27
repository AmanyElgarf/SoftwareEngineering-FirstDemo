import numpy as np

class Neural_Network(object):
    def __init__(self):
        #parameters
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3
        
        #the current iteration of the Neural Network is Feed forward, takes 2 inputs, passes those through 3 hidden layers and gives one output
            
        #weights
        self.W1 = np.loadtxt("w1.txt")  # (3x2) weight matrix from input to hidden layer
        self.W2 = np.loadtxt("w2.txt")  # (3x1) weight matrix from hidden to output layer

    def forward(self, X):
        #forward propagation through our network
        self.z = np.dot(
            X,
            self.W1)  # dot product of X (input) and first set of 3x2 weights
        self.z2 = self.sigmoid(self.z)  # activation function
        self.z3 = np.dot(
            self.z2, self.W2
        )  # dot product of hidden layer (z2) and second set of 3x1 weights
        o = self.sigmoid(self.z3)  # final activation function
        return o

    def sigmoid(self, s):
        # activation function
        return 1 / (1 + np.exp(-s))

    def sigmoidPrime(self, s):
        #derivative of sigmoid
        return s * (1 - s)

    def backward(self, X, y, o):
        # backward propgate through the network
        self.o_error = y - o  # error in output
        self.o_delta = self.o_error * self.sigmoidPrime(
            o)  # applying derivative of sigmoid to error

        self.z2_error = self.o_delta.dot(
            self.W2.T
        )  # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error * self.sigmoidPrime(
            self.z2)  # applying derivative of sigmoid to z2 error

        self.W1 += X.T.dot(
            self.z2_delta)  # adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(
            self.o_delta)  # adjusting second set (hidden --> output) weights

    def train(self, X, y):
        #when called in a loop, this incrementally tests the Neural Network with Dataset X as an input, and y as an expected output
        o = self.forward(X)
        self.backward(X, y, o)

    def saveWeights(self):
        #when called after training it saves the weights that the NN uses to come up with a predicted output
        np.savetxt("w1.txt", self.W1, fmt="%s")
        np.savetxt("w2.txt", self.W2, fmt="%s")


    def predict(self, xPredicted):
        print("Predicted data based on trained weights: ")
       
        prediction = self.forward(xPredicted)
        
        return prediction

    def scaleinput(self, x):
        # scales the inputs so that the NN can process the data as intended
        xPredicted = np.array(x, dtype = float)
        xPredicted = xPredicted/np.amax(xPredicted, axis=0)
        return xPredicted



