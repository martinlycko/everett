import pandas as pd

class ForecastingModel:
    def __init__(self):
        self.Inputs = {}
        self.results = pd.DataFrame()
        self.runs = None
        self.steps = None

    def addInput(self, name, input):
        self.Inputs[name] = input

    def multiverse(self, runs: int, function, steps):
        # Empty the results dataframe
        self.results = pd.DataFrame()

        for i in range(runs):
            # Run the function for the given number of steps
            result = function(steps)
            # Append the result to the model's results dataframe with the run identifier
            result['run_id'] = i
            self.results = pd.concat([self.results, result], ignore_index=True)
        
        return self.results