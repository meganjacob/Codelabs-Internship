import numpy as np
import pandas as pd

#Given a pandas series, this returns the standarized a(in z-score space), the mean, and the std for unstandardization.
def standardize(a):
  astd = np.std(a)
  mean = a.mean()
  a -= a.mean()
  a /= astd
  return a,mean,astd

#Unstandarizes a series, given it's mean and std.
def unstandardize(a,mean,astd):
    a = a*astd
    a = a + mean
    return a

