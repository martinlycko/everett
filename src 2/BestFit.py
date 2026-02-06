import numpy as np

class Linear:
    def __init__(self, intercept, gradient):
        self.intercept = intercept
        self.gradient = gradient

    def predict(self, step):
        return self.intercept + self.gradient * step

class Logarithmic:
    def __init__(self, intercept, gradient):
        self.intercept = intercept
        self.gradient = gradient

    def predict(self, step):
        return self.intercept + self.gradient * np.log(step)