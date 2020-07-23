#Downcast in order to save memory
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


def compress_dataframe(df):
    """
    Downcast dataframe and convert objects to categories to save memory
    """
    def handle_numeric_downcast(array, type_):
        return pd.to_numeric(array, downcast=type_)

    for type_ in ['integer', 'float', 'object']:
        column_list = df.select_dtypes(include=type_)

        if type_ == 'object':
            df[column_list] = df[column_list].astype('category') 
        else:
            df[column_list] = handle_numeric_downcast(df[column_list], type_)

#TODO when splitting up tasks in multiple functions, ask if it makes the code easier or harder to read. 
# IMO, these splits make the code harder to understand

#I tried upsampling in order to find the weeks that are missing by adding those rows in and filling them in with NaN
#However, for some reason, after '2011-01-31' instead of '2011-02-07', it starts with '2011-02-06' so it throws it off
#TODO can you show me screenshots of what you mean? the data was aggregated using W-MON format, maybe that will solve your issue
#TODO don't hardcode things like date formats since they're likely to change
#TODO don't need parentheses around return (minor style issue)


#The following function is quite inefficient since it has quadratic runtime O(n^2), but I'm not sure how to fix this
def find_missing_weeks_in_entire_dataframe(dataframe):
    #TODO if you'll never use any of these functions again, define them within the scope of this function so they aren't hanging out in memory
    def find_item_and_store_combo(dataframe, store_id, item_id):
        #TODO nice job on the descriptive variable names!
        #TODO hardcoding
        #TODO why cast to a dict only to cast it back to a dataframe? seems like there's a better way
        return dataframe[(dataframe['store_id'] == store_id) & (dataframe['item_id'] == item_id)]
    
    def upsampling(dataframeinput):
        return dataframeinput.set_index('datetime').resample('w').asfreq()
    
    def find_missing_weeks_for_specific_combo(dataframeinput):
        return dataframeinput[dataframeinput['dept_id'].isna()]

    combo_dict = dataframe.groupby(['store_id', 'item_id']).groups.keys()
    for key in combo_dict: 
        combo = find_item_and_store_combo(dataframe, key[0], key[1])
        upsampled = upsampling(combo)
        print(find_missing_weeks_for_specific_combo(upsampled))

    #TODO after you upsample and fill the missing rows with NaNs, you should be able to use .grouby(grouping_cols).count() to get the number of missing. no for-loops!


#Write a function to calculated MAPE weighted by the total sales for a given item across all stores
def mape(df, item, predict):
    real = df[(df['item_id'] == item)]['sales'].sum()
    return np.mean(np.abs((real - predict) / y_true)) * 100
 
   
    

    