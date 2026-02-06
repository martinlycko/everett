from BestFit import Linear, Logarithmic
import numpy as np

class Variable:
    def __init__(self, timeseries):
        # Store source data
        self.series = timeseries
        self.steps = []
        for i in range(len(timeseries)):
            self.steps.append(i+1)
        
        # Line of best fit
        self.fit = self.get_best_fit()

    def get_best_fit(self):
        log_steps = np.log(self.steps)
        
        # Calculate the line of best fit for the data
        linear = np.polyfit(self.steps, self.series, 1, full=True)
        logarithmic = np.polyfit(log_steps, self.series, 1, full=True)
        
        if linear[1][0] < logarithmic[1][0]:
            return Linear(linear[0][1], linear[0][0])
        else:
            return Logarithmic(logarithmic[0][1], logarithmic[0][0])


if __name__ == "__main__":

    # Example usage
    timeseries = [2, 4, 6, 8, 10]
    variable = Variable(timeseries)

    print(variable.fit.predict(6))  # Predict the value at step 6


    timeseries2 = [0, 6.9, 10.9, 13.8, 16.1]
    variable2 = Variable(timeseries2)

    print(variable2.fit.predict(7))  # Predict the value at step 6

    #plt.scatter(variable.steps, variable.series, color='blue')
    #plt.plot(variable.steps, np.polyval(variable.coefficients, variable.steps), color='red')
    #plt.show()