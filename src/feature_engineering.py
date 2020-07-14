import numpy as np
import pandas as pd

#Given a pandas series, this returns the standarized a(in z-score space), the mean, and the std for unstandardization.
#TODO use more describe names (b => result_df; a-> input_df; astd...)
#TODO add newlines in your code to make it visually easier to read (group similar lines together)
def standardize(a):
  astd = np.std(a)
  mean = a.mean()

  #TODO shouldn't need to copy if you don't use in-place operations here. condense down to one line?
  b = a.copy()
  b -= b.mean()
  b /= astd

  #TODO imagine that we don't want our users to manually enter mean and astd into unstandardize() since they're \
  # likely to forget to update these values after they change. how can you pass the mean and astd as a state to \
  # unstandardize without using params?
  return b,mean,astd

#Unstandarizes a series, given it's mean and std.
#TODO use more descriptive names (not a)
def unstandardize(a,mean,astd):
    #TODO is there a reason not to write this as: return a * astd + mean
    a = a*astd
    a = a + mean
    return a

def stat_feature(df1,grouping,col):
    #TODO copying dataframes doesn't scale well
    df = df1.copy()
    
    #TODO instead of passing mean, min, and max, calculate them all at once using a single line of code and an \
    #  aggregate_dict param (hint: use .agg())
    #TODO if we include the current row's data in an aggregate calculation, we'll "leak" data about the future when \
    # making predictions. shift your dataframe back one period  to avoid this issue
    mean = df.groupby([grouping])[col].mean()
    mi = df.groupby([grouping])[col].min()
    ma = df.groupby([grouping])[col].max()
    return mean, mi, ma

def agg_feature(df1,grouping,col):
    #TODO see my comments above; you can delete this function and just pass cumsum() into the dict
    df = df1.copy()
    return df.groupby([grouping])[col].cumsum()


def detrend_feature(df1,grouping,col):
    #TODO no copying
    df = df1.copy()

    #TODO not sure you need to instantiate series; can chain the methods instead
    series = df[col]
    X = series.values
    
    #TODO no for-loops! iterating over rows won't scale. calculate this using pandas built-ins (hint: see .shift())
    diff = list()
    diff.append(np.nan)
    for i in range(1, len(X)):
        value = X[i] - X[i - 1]
        diff.append(value)
    return pd.series(diff)
