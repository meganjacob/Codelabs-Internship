import numpy as np
import pandas as pd

#Given a pandas series, this returns the standarized series(in z-score space).
#TODO what if you want to standardize multiple columns? is creating global variables a safe way to maintain state?
stat = dict()
def standardize(df,col):
    input_std = np.std(df[col])
    input_mean = df[col].mean()
    global stat
    stat[col] = [input_std,input_mean]
    return (df[col]-input_mean)/input_std


#Unstandarizes a series. 
def unstandardize(ser,col):
    global stat
    return ser*stat[col][0] + stat[col][1]


#Gives two dataframes. The first one has the stats mean, min, and max, and the second one has the cumulative sums.
#TODO don't hardcode! what if you only want the mean?

#feature has to be an array filled with strings of the desired features, except cumsum -- if you want cumsum, please use the cum_stat function instead. An example of features is ['mean','min','max']
def stat_feature(df,grouping,col,features):
    agg = df.groupby([grouping])[col].agg(features)
    return agg

    
def cum_stat(df,grouping,col):
    cumsum = df.groupby([grouping])[col].shift(periods = 1).agg(['cumsum'])
    return cumsum


#Detrends a dataframe, given the grouping, and column. 
def detrend_feature(df,grouping,col):
    return df[col] - df[col].shift(periods=1)



#The following are the 6 time-related features. Not sure how to use external data for holiday flags and major events
def month_feature(dataframeinput):
    return dataframeinput['datetime'].dt.month

def quarter_feature(dataframeinput):
    return dataframeinput['datetime'].dt.quarter
    #January-March = 1, April-June = 2, etc.
    
def week_of_year_feature(dataframeinput):
    return dataframeinput['datetime'].dt.weekofyear

def day_of_week_feature(dataframeinput):
    return dataframeinput['datetime'].dt.dayofweek

def month_year_feature(dataframeinput):
    year = dataframeinput['datetime'].dt.year
    month = month_feature(dataframeinput)
    newdataframe = pd.DataFrame()
    newdataframe['month'] = month
    newdataframe['year'] = year
    return(newdataframe)

def semester_feature(dataframeinput):
    dataframeinputcopy = dataframeinput
    dataframeinputcopy['quarter'] = quarter_feature(dataframeinput)
    dataframeinputcopy['semester'] = np.where(dataframeinputcopy.quarter.isin([1,2]),1,2)
    return dataframeinputcopy[['datetime', 'semester']].head()