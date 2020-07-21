#TODO use "_" per PEP8 conventions ("pandas_df")
#TODO why hardcode sales when you take take it as an argument and have a more general function to wokr with?
def univariate_sales_histogram(pandadataframe, sales_column):
    sales_series = pandadataframe[sales_column]
    max_sale = sales_series.max()
    (pandadataframe.hist(column=sales_column,bins=100, figsize=(12,8), range=[0,50]))
    
def bivariate_sales_by_state(pandadataframe, sales_column):
    sales_series = pandadataframe[sales_column]
    max_sale = sales_series.max()
    pandadataframe.hist(column=sales_column, by="state_id",bins=100, figsize=(12,8), range=[0,50])

def bivariate_sales_by_store(pandadataframe, sales_column):
    sales_series = pandadataframe[sales_column]
    max_sale = sales_series.max()
    pandadataframe.hist(column=sales_column, by="store_id",bins=100, figsize=(12,8), range=[0,50])

#TODO same as above
def sales_boxplot(dataframeinput, sales_column):
    sns.boxplot(x=dataframeinput[sales_column])
def sales_box_plot_by_state_id(dataframeinput, sales_column):
    dataframeinput.boxplot(by='state_id', column=[sales_column])
def sales_box_plot_by_store_id(dataframeinput, sales_column):
    dataframeinput.boxplot(by='store_id', column=[sales_column])

def heatmap_to_see_missing_data(pandas_df):
    sns.heatmap(pandas_df.isnull(), cbar = False)