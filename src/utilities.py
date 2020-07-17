import pandas as pd
import dask.dataframe as dd
import numpy as np

pandas_df = pd.read_pickle("./raw_weekly_df.pkl")
dask_df = dd.from_pandas(pandas_df, npartitions=8)


#Downcast in order to save memory
#TODO very nicely done! one thought: you don't want to hardcode the date format since that's likely to vary between datasets; \
# pass that as a param or global 
def downcast(df,date_format):
    cols = df.dtypes.index.tolist()
    types = df.dtypes.values.tolist()
    for i,t in enumerate(types):
        if 'int' in str(t):
            df[cols[i]] = pd.to_numeric(df[cols[i]], downcast='integer')
        elif 'float' in str(t):
            df[cols[i]] = pd.to_numeric(df[cols[i]], downcast='float')
        elif t == np.object:
            if cols[i] == 'date':
                df[cols[i]] = pd.to_datetime(df[cols[i]], format=date_format)
            else:
                df[cols[i]] = df[cols[i]].astype('category')
    return df  


