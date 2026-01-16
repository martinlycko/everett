import numbers, math
from numpy import random

from src.Distributions import Distribution


class Input:
    def __init__(self, data, distribution=Distribution.NORMAL):
        self.data = data
        
        if isinstance(distribution, Distribution):
            self.distribution = distribution
        else:
            raise ValueError("Distribution must be an instance of Distribution Enum")

    def avg(self):
        if not self.data:
            return 0
        if all(isinstance(x, numbers.Number) for x in self.data):
            return sum(self.data) / len(self.data)
        raise ValueError("All elements must be numbers to calculate average.")
    
    def sd(self):
        if not self.data:
            return 0
        if all(isinstance(x, numbers.Number) for x in self.data):
            avg = self.avg()
            variance = sum((x - avg) ** 2 for x in self.data) / len(self.data)
            return variance ** 0.5
        raise ValueError("All elements must be numbers to calculate standard deviation.")
    
    def log_avg(self):
        if not self.data:
            return 0
        if all(isinstance(x, numbers.Number) and x > 0 for x in self.data):
            log_data = [math.log(x) for x in self.data]
            return sum(log_data) / len(self.data)
        raise ValueError("All elements must be positive numbers to calculate log average.")
    
    def log_sd(self):
        import math
        if not self.data:
            return 0
        if all(isinstance(x, numbers.Number) and x > 0 for x in self.data):
            log_data = [math.log(x) for x in self.data]
            log_avg = sum(log_data) / len(log_data)
            variance = sum((x - log_avg) ** 2 for x in log_data) / len(log_data)
            return variance ** 0.5
        raise ValueError("All elements must be positive numbers to calculate log standard deviation.")
    
    def generateValue(self):
        match self.distribution:
            case Distribution.NORMAL:
                mu = self.avg()
                sigma = self.sd()
                return random.normal(mu, sigma)
            case Distribution.LOGNORMAL:
                mu = self.log_avg()
                sigma = self.log_sd()
                return random.lognormal(mu, sigma)
            case _:
                raise ValueError("Unsupported distribution type.")
            
    def generateValues(self, n):
        return [self.generateValue() for _ in range(n)]