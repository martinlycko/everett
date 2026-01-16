import math

from src.Input import Input
from src.Distributions import Distribution

def test_input_normal():
    # Creating a test case for normal distribution
    data = [1, 2, 3, 4, 5]
    inp = Input(data, distribution=Distribution.NORMAL)
    assert inp.avg() == 3
    assert inp.sd() == (2.0 ** 0.5)
    assert round(inp.log_avg(), 2) == 0.96
    assert round(inp.log_sd(), 2) == 0.57

    # Checking the distributions of generated values match expecations
    sample = inp.generateValues(1000)
    sample_avg = sum(sample) / len(sample)
    sample_sd = (sum((x - sample_avg) ** 2 for x in sample) / len(sample)) ** 0.5
    assert round(sample_avg, 2) >= inp.avg() * 0.9
    assert round(sample_avg, 2) <= inp.avg() * 1.1
    assert round(sample_sd, 2) >= inp.sd() * 0.9
    assert round(sample_sd, 2) <= inp.sd() * 1.1

    # Confirm run of test
    print("Normal distribution input test passed.")

def test_input_lognormal():
    # Creating a test case for lognormal distribution
    data = [2, 3, 5, 9, 15]
    inp = Input(data, distribution=Distribution.LOGNORMAL)

    # Checking log average and log standard deviation
    assert round(inp.log_avg(), 2) == 1.66
    assert round(inp.log_sd(), 2) == 0.73

    # Checking the distributions of generated values match expecations
    sample = inp.generateValues(1000)
    sample_log = [math.log(x) for x in sample]
    sample_log_avg = sum(sample_log) / len(sample_log)
    sample_log_sd = (sum((x - sample_log_avg) ** 2 for x in sample_log) / len(sample_log)) ** 0.5
    assert round(sample_log_avg, 1) >= inp.log_avg() * 0.9
    assert round(sample_log_avg, 1) <= inp.log_avg() * 1.1
    assert round(sample_log_sd, 1) >= inp.log_sd() * 0.9
    assert round(sample_log_sd, 1) <= inp.log_sd() * 1.1

    # Confirm run of test
    print("Lognormal distribution input test passed.")

if __name__ == "__main__":
    test_input_normal()
    test_input_lognormal()
