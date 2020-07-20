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

#TODO source files shouldn't call functions; move to .main
univariate_sales_histogram(pandas_df, "sales")
"""The majority of sales are between 0 and 10, with most sales falling at 0."""

bivariate_sales_by_state(pandas_df, "sales")
"""Out of all three states, CA has the most number of sales (around 700,000 sales at 0.0) as compared to Wisconsin and Texas."""
"""This makes sense since California has the largest population compared to the other two. """
bivariate_sales_by_store(pandas_df, "sales")
"""In the previous observation, CA was observed to have the most number of 0.0 sales compared to the other two states. However, through this histogram, we see that CA actually has more stores than Texas and Wisconsin. All the graphs of the stores seem pretty similar, but if you observe closely, CA_1, CA_2, CA_3 (especially CA_3), CA_4, TX_1, TX_2 all have sales between 30 and 50 as well, unlike the other stores."""
"""This makes sense as well since CA has the largest population compared to the other two states, and compared to Wisconsin, Texas has a larger population."""


#TODO same as above
def sales_boxplot(dataframeinput, sales_column):
    sns.boxplot(x=dataframeinput[sales_column])
def sales_box_plot_by_state_id(dataframeinput, sales_column):
    dataframeinput.boxplot(by='state_id', column=[sales_column])
def sales_box_plot_by_store_id(dataframeinput, sales_column):
    dataframeinput.boxplot(by='store_id', column=[sales_column])

sales_boxplot(pandas_df, "sales")
"""The max sales value, 4220 is clearly an outlier. There also seem to be 6 other outliers since they are separate. All the outliers are larger not smaller."""
"""California has this outlier which is the largest value; this makes sense since California has a larger amount of people who contribute to these larger outliers occassionally."""
sales_box_plot_by_state_id(pandas_df, "sales")
"""California has the largest value, 4220, which is also its largest outlier. California has 2 outliers that are 
at least 1000 more than the maximum in its data. Texas and Wisconsin have outliers that are smaller than 2000. Wisconsin has the least number of outliers."""
sales_box_plot_by_store_id(pandas_df, "sales")
"""Every store's outliers are beneath 2000 except for CA_3, all of whose outliers crossed 2000.
Since the range for CA_3 is higher than that of every other store, it indicates that CA_3 had the most sales."""
"""This makes sense since California has the largest population, so there will be more sales and larger outliers."""



def heatmap_to_see_missing_data(pandas_df):
    sns.heatmap(pandas_df.isnull(), cbar = False)

heatmap_to_see_missing_data(pandas_df)
"""The heatmap has a display column for each series in a pandadataframe, and will have horizontal rows within each column wherever there are missing values/data (NaN). In this case, there aren't any missing data so the heatmap is empty."""