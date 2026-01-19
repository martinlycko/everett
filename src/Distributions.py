from numpy import random

class Normal:
    def __init__(self, avg, sd):
        self.avg = avg
        self.sd = sd
    
    def generateValue(self):
        return random.normal(self.avg, self.sd)
    
class LogNormal:
    def __init__(self, log_avg, log_sd):
        self.log_avg = log_avg
        self.log_sd = log_sd
    
    def generateValue(self):
        return random.lognormal(self.log_avg, self.log_sd)