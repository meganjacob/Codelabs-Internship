import pandas as pd
import dask.dataframe as dd
import numpy as np


pandas_df = pd.read_pickle("./raw_weekly_df.pkl")
dask_df = dd.from_pandas(pandas_df, npartitions=8)
mean = 0
std = 0
  

#Given a pandas series, this returns the standarized series(in z-score space).
def standardize(input_ser):
    input_std = np.std(input_ser)
    input_mean = input_ser.mean()
    global mean
    global std
    mean = input_mean
    std = input_std
    
    return (input_ser-input_mean)/input_std



#Unstandarizes a series. 
def unstandardize(ser):
    return ser*std + mean


#Gives two dataframes. The first one has the stats mean, min, and max, and the second one has the cumulative sums.
def stat_feature(df,grouping,col):
    agg = df.groupby([grouping])[col].agg(['mean','min','max'])
    cumsum = df.groupby([grouping])[col].shift(periods = 1).agg(['cumsum'])
    return agg,cumsum 


#Detrends a dataframe, given the grouping, and column. 
def detrend_feature(df,grouping,col):
    return df[col] - df[col].shift(periods=1)
