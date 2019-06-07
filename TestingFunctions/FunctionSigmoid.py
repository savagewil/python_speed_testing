import math

from TestingFunctions.FunctionExample import FunctionExample
def sigmoid(x):
    return 1.0 / (1.0 + (math.e ** (-x)))

class FunctionSigmoid(FunctionExample):
    def run(self, data):
        return sigmoid(data)

    def run_no_return(self, data):
        sigmoid(data)
