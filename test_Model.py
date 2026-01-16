from src.Input import Input
from src.Distributions import Distribution
from src.Model import ForecastingModel

def test_model_1():
    # Create objects
    data = [1, 2, 3, 4, 5]
    inp1 = Input(data, distribution=Distribution.NORMAL)
    inp2 = Input(data, distribution=Distribution.NORMAL)
        
    testmodel = ForecastingModel()
    def forecast_function(val1, val2):
        return val1 + val2
    testmodel.forecast = forecast_function
    testmodel.addInput(inp1)
    testmodel.addInput(inp2)

    # Run multiverse
    results = testmodel.multiverse(runs=1000)

    assert len(results) == 1000
    assert testmodel.multiverse_avg() >= 6 * 0.9
    assert testmodel.multiverse_avg() <= 6 * 1.1

    print("Model test 1 passed.")

if __name__ == "__main__":
    test_model_1()
    