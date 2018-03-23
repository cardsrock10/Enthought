"""
Stock returns
=============

We have loaded for you some data from the IO exercise which contains adjusted-
close data for 6 major stocks between 2005 and 2009.  In this exercise, we
will explore looking for correlations between these stocks.

1. We have loaded all data into a dataframe. Make a plot of all stock market
   timeseries.

2. Build another dataframe with all values renormalized by the value of the
   stock at their value on Jan 3rd, 2005.  Plot it in a different figure.

3. The daily return of a stock is defined by::

               adj clos(t+1) - adj clos(t)   adj clos(t+1)
        r(t) = --------------------------- = -------------  - 1
                      adj clos(t)             adj clos(t)

   Build another dataframe with the daily returns for each stock for each day
   except Jan 3rd, 2005. Plot it in a different figure.

4. We would like to visualize how correlated these returns are. In a new
   figure, make a scatter_matrix plot to show a scatter plot between each pair
   of tickers. On the diagonal, let's display the reconstructed pdf of these
   returns using the kernel density estimator method. For this, look at the
   optional keyword arguments of the scatter_matrix function.

5. The previous plot is simply a visualization of the values. Let's compute
   the actual correlation between each pair of returns. Matplotlib's imshow
   represents a 2D array of data like an image. That function can be used
   directly on a dataframe to view it as a matrix.  Use imshow to build a
   heatmap of the correlations of returns. Explore how that map changes when a
   different correlaton algorithm is used.

See :ref:`stock-return-solution`.
"""
from pandas import read_table, scatter_matrix
from matplotlib.pyplot import colorbar, figure, imshow, show, title, xticks, \
    yticks

# 0.
local_dataset = read_table("adj_close_stock_data_2005_2010.txt",
                           sep="\s+", parse_dates=[[0, 1, 2]])
local_dataset = local_dataset.set_index("year_month_day")
local_dataset.index.name = "Date"

# 1.

# 2.

# 3.

# 4:

# 5:
