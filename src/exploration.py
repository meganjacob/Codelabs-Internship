def univariate_sales_histogram(pandadataframe):
    sales_series = pandadataframe['sales']
    max_sale = sales_series.max()
    (pandadataframe.hist(column='sales',bins=100, figsize=(12,8), range=[0,50]))
    
def bivariate_sales_by_state(pandadataframe):
    sales_series = pandadataframe['sales']
    max_sale = sales_series.max()
    pandadataframe.hist(column='sales', by="state_id",bins=100, figsize=(12,8), range=[0,50])

def bivariate_sales_by_store(pandadataframe):
    sales_series = pandadataframe['sales']
    max_sale = sales_series.max()
    pandadataframe.hist(column='sales', by="store_id",bins=100, figsize=(12,8), range=[0,50])

univariate_sales_histogram(pandas_df)
"""The majority of sales are between 0 and 10, with most sales falling at 0."""
bivariate_sales_by_state(pandas_df)
"""Out of all three states, CA has the most number of 0.0 sales (around 700,000 sales at 0.0) as compared to Wisconsin and Texas (around 600,000 sales at 0.0). """
bivariate_sales_by_store(pandas_df)
"""In the previous observation, CA was observed to have the most number of 0.0 sales compared to the other two states. However, through this histogram, we see that CA actually has more stores than Texas and Wisconsin. All the graphs of the stores seem pretty similar, but if you observe closely, CA_1, CA_2, CA_3 (especially CA_3), CA_4, TX_1, TX_2 all have sales between 30 and 50 as well, unlike the other stores."""



def sales_boxplot(dataframeinput):
    sns.boxplot(x=dataframeinput['sales'])
def sales_box_plot_by_state_id(dataframeinput):
    dataframeinput.boxplot(by='state_id', column=['sales'])
def sales_box_plot_by_store_id(dataframeinput):
    dataframeinput.boxplot(by='store_id', column=['sales'])

sales_boxplot(pandas_df)
"""The max sales value, 4220 is clearly an outlier. There also seem to be 6 other outliers since they are separate. All the outliers are larger not smaller."""
sales_box_plot_by_state_id(pandas_df)
"""California has the largest value, 4220, which is also its largest outlier. California has 2 outliers that are 
at least 1000 more than the maximum in its data. Texas and Wisconsin have outliers that are smaller than 2000. Wisconsin has the least number of outliers."""
sales_box_plot_by_store_id(pandas_df)
"""Every store's outliers are beneath 2000 except for CA_3, all of whose outliers crossed 2000.
Since the range for CA_3 is higher than that of every other store, it indicates that CA_3 had the most sales."""



def heatmap_to_see_missing_data(dataframeinput):
    sns.heatmap(pandas_df.isnull(), cbar = False)

heatmap_to_see_missing_data(pandas_df)
"""The heatmap has a display column for each series in a pandadataframe, and will have horizontal rows within each column wherever there are missing values/data (NaN). In this case, there aren't any missing data yet, since the missing time_periods haven't been found and added in filled with NaNs."""