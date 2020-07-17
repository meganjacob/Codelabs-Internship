#Given a pandas series, this returns the standarized series(in z-score space).
#TODO what if you want to standardize multiple columns? is creating global variables a safe way to maintain state?
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
#TODO don't hardcode! what if you only want the mean?
def stat_feature(df,grouping,col):
    agg = df.groupby([grouping])[col].agg(['mean','min','max'])
    cumsum = df.groupby([grouping])[col].shift(periods = 1).agg(['cumsum'])
    return agg,cumsum 


#Detrends a dataframe, given the grouping, and column. 
def detrend_feature(df,grouping,col):
    return df[col] - df[col].shift(periods=1)
