import numpy as np
import pandas as pd

#Given a pandas series, this returns the standarized a(in z-score space), the mean, and the std for unstandardization.
def standardize(a):
  astd = np.std(a)
  mean = a.mean()
  b = a.copy()
  b -= b.mean()
  b /= astd
  return b,mean,astd

#Unstandarizes a series, given it's mean and std.
def unstandardize(a,mean,astd):
    a = a*astd
    a = a + mean
    return a

def stat_feature(df1,grouping,col):
    df = df1.copy()
    mean = df.groupby([grouping])[col].mean()
    mi = df.groupby([grouping])[col].min()
    ma = df.groupby([grouping])[col].max()
    return mean, mi, ma

def agg_feature(df1,grouping,col):
    df = df1.copy()
    return df.groupby([grouping])[col].cumsum()

