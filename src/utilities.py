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
def get_dataframe_of_item_ids(dataframeinput):
    #TODO can't assume 'item_id' can be hardcoded
    x = (((dataframeinput[['item_id']]).drop_duplicates()))
    newdataframe = pd.DataFrame(x)
    return (newdataframe)

#example = (get_dataframe_of_item_ids(pandas_df))


def get_dataframe_of_store_ids(dataframeinput):
    #TODO hard-coding
    #TODO delete commented code
    x = (((dataframeinput[['store_id']]).drop_duplicates()))
    #newdataframe = pd.Dataframe(x)
    return (x)


def convert_dataframe_to_list(dataframe):
    return (dataframe.values.tolist())
#print(get_dataframe_of_store_ids(pandas_df))


def find_item_and_store_combo(dataframe, store_id, item_id):
    #TODO nice job on the descriptive variable names!
    #TODO hardcoding
    #TODO why cast to a dict only to cast it back to a dataframe? seems like there's a better way
    x = (dataframe[(dataframe['store_id'] == store_id) & (dataframe['item_id'] == item_id)]).to_dict()
    subsetdataframe = pd.DataFrame(x)
    return(subsetdataframe)
    
    
#I tried upsampling in order to find the weeks that are missing by adding those rows in and filling them in with NaN
#However, for some reason, after '2011-01-31' instead of '2011-02-07', it starts with '2011-02-06' so it throws it off
#TODO can you show me screenshots of what you mean? the data was aggregated using W-MON format, maybe that will solve your issue
#TODO don't hardcode things like date formats since they're likely to change
#TODO don't need parentheses around return (minor style issue)
def upsampling(dataframeinput):
    return(dataframeinput.set_index('datetime').resample('w').asfreq())

#TODO hardcoding
def find_missing_weeks_for_specific_combo(dataframeinput):
    return(dataframeinput[dataframeinput['dept_id'].isna()])


#The following function is quite inefficient since it has quadratic runtime O(n^2), but I'm not sure how to fix this
def find_missing_weeks_in_entire_dataframe(dataframe):
    #TODO if you'll never use any of these functions again, define them within the scope of this function so they aren't hanging out in memory
    dataframe_of_store_ids = get_dataframe_of_store_ids(dataframe)
    store_ids = convert_dataframe_to_list(dataframe_of_store_ids)
    dataframe_of_item_ids = get_dataframe_of_item_ids(dataframe)
    item_ids = convert_dataframe_to_list(dataframe_of_item_ids)
    
    #TODO after you upsample and fill the missing rows with NaNs, you should be able to use .grouby(grouping_cols).count() to get the number of missing. no for-loops!
    for store in store_ids:
        store_id = ''.join(store)
        print(store_id)
        for item in item_ids:
            item_id = ''.join(item)
            print('helo')
            print(item_id)
            combo = (find_item_and_store_combo(pandadataframe, store_id, item_id))
            print(combo)
            #psampled = upsampling(combo)
            #mssing_weeks = find_missing_weeks(upsampled)
            #t([store_id, item_id, missing_weeks])
            
#Write a function to calculated MAPE weighted by the total sales for a given item across all stores
def mape(df, item, predict):
    real = df[(df['item_id'] == item)]['sales'].sum()
    return np.mean(np.abs((real - predict) / y_true)) * 100
            
