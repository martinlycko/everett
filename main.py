from src.Input import Input
from src.Distributions import Distribution

def test_avg():
    data = [1, 2, 3, 4, 5]
    inp = Input(data, distribution=Distribution.NORMAL)
    assert inp.avg() == 3