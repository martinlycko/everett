from src.Distributions import Normal
from src.Model import ForecastingModel

import pandas as pd


def cummulative_function(steps):
    # Create an empty dataframe with relevant columns
    results = pd.DataFrame(columns=['Step', 'ServiceUsers', 'NewServiceUsers', 'AbandonRate', 'ServiceUsersLost'])
    
    # Create and initialise state of initial values
    ServiceUsersStock = []
    ServiceUsersStock.append(0)
    
    i = 0
    while i < steps:
        NewServiceUsers = testmodel.Inputs['NetNewSUs'].generateValue()
        AbandonRate = testmodel.Inputs['ReturnRate'].generateValue()
        ServiceUsersLost = ServiceUsers[i] * AbandonRate
        ServiceUsers = ServiceUsers[i] + NewServiceUsers - ServiceUsersLost
        
        ServiceUsersStock.append(NewSUs)

        # Add a row to the results dataframe including
        results = results.append({
            'Step': i,
            'ServiceUsers': ServiceUsers,
            'NewServiceUsers': NewServiceUsers,
            'ServiceUsersLost': ServiceUsersLost
        }, ignore_index=True)

        i = i + 1

    # Make this a dataframe
    return results


if __name__ == "__main__":
    # Create objects
    NewSUs =  Normal(100, 10)
    ReturnRate = Normal(0.2, 0.01)

    testmodel = ForecastingModel()
    testmodel.addInput('NetNewSUs', NewSUs)
    testmodel.addInput('ReturnRate', ReturnRate)

    testmodel.multiverse(10000, cummulative_function, 100)
    print(sum(testmodel.results)/len(testmodel.results))