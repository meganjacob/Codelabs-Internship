import pandas as pd
import dask.dataframe as dd

pandas_df = pd.read_pickle("./raw_weekly_df.pkl")
dask_df = dd.from_pandas(pandas_df, npartitions=8)

#Downcast the dataframe
pandas_df.info(memory_usage="Deep")
