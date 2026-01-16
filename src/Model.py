from src.Input import Input


class ForecastingModel:
    def __init__(self):
        self.Inputs = []
        self.results = []

    def forecast(self):
        # Overwrite this function in instance
        pass

    def addInput(self, input: Input):
        self.Inputs.append(input)

    def multiverse(self, runs: int):
        results = []
        for _ in range(runs):
            input_values = [inp.generateValue() for inp in self.Inputs]
            result = self.forecast(*input_values)
            results.append(result)
        self.results = results
        return results
    
    def multiverse_avg(self: int):
        return sum(self.results) / len(self.results)