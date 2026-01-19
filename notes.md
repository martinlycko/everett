# Requirements
- Take a Pandas dataframe.
- The dataframe contains a time series.
- Each row is one time step
- Each column is one variable

# Enrich the data
- Highlight input columns, so stats can be derived
    - Set or derive probability distribution
    - Set or derive trend
- Set outcome variables, e.g. the final ones we are interested in
- Set intermediary variables, e.g. used to calculate intermediary steps
- Set calculations between columns for calculations on single timesteps
- Set calculations between rows for cumulative/stock variables

# Algorithms
- 