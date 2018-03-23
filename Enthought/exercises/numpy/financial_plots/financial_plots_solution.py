"""
Financial plots
===============

In this exercise, we will learn to build various types of financial plots.

This folder contains historical prices for the stock of 5 large companies
for each business day from 2005-2009:
AAPL, GOOGL, MSFT, PG, XOM
stored in a numpy structured array (we'll learn about these in more depth
later). Some code below is provided to load the data for you. The resulting
data object can be used a bit like a dictionary of numpy arrays, containing the
time series for each stock. For example, data["AAPL"] is the timeseries for the
Apple stock.

1. Plot the timeseries of AAPL against the number of business days since Jan
3rd 2005.
Superimpose all 4 other stocks. Make sure to provide a title, a legend and
axes labels. Bonus point for using a 'for' loop and for normalizing each
timeseries by the starting price of that stock.

2. Use IPython to learn about the matplotlib function `yscale`. Use it to make
the previous plot logarithmic in y. Save the resulting file as a .png. Search
for a function to do this programmatically inside matplotlib.pyplot.

3. We now want to create a new plot where each curve is in its own subplot
(with a vertical layout). Provide a label for each y axes but only provide a
label for the x axis to the last subplot.

4. We would like to visualize the variation of each stock over time and
compare these variations to each other. This can be done with a boxplot. Make
one.
Bonus: look at the xticks function from matplotlib and use it to make the
boxplot display 'AAPL', 'GOOGL', 'MSFT', 'PG', 'XOM' instead of 1, 2, 3, 4, 5
along the x axis.

5. So far we've been drawing line plots, but correlations are better shown on
scatter plots. Create two scatter plots showing the prices of (1) APPL vs GOOG
and (2) APPL vs PG. Later in the course, when we will have learned about
slicing, we will learn to compute the returns, which is a better quantity to
use when making scatter plots of a ticker vs another.

Bonus:
~~~~~~
6. It would be nice to compare visually all possible scatter plots similar to
the 2 created at question 5.
Make a table of scatter plots displaying the correlation between all the
stocks using matplotlib's `subplot` (it will be a 5x5 table of plots). On the
diagonal, display the distribution of values for the stock as a histogram. Look
at `correlation_scatters.png` for a saved representation of the desired plot.
If you have time, add plot labels along the changing dimensions of the table.
"""

# Preliminaries: loading the data.
from financial_plot_support import load_stock_data

data = load_stock_data("open_stock_data_yahoo_2005_2010.csv")
stock_names = ["AAPL", "GOOGL", "MSFT", "PG", "XOM"]

# Imports
from matplotlib.pyplot import plot, boxplot, figure, hist, legend, show, \
    savefig, scatter, subplot, title, xlabel, xticks, yscale, ylabel

# 1.
figure(1)
for stock in stock_names:
    plot(data[stock], label=stock)
title("Stocks for %s from 2005/1/1 to 2009/12/31" % stock_names)
xlabel("Business days since 2005/1/1")
legend()

# 2.
yscale('log')
savefig("my_log_plot.png")

# 3.
figure(2)
for i, stock in enumerate(stock_names):
    subplot(len(stock_names), 1, i + 1)
    plot(data[stock], label=stock)
    ylabel(stock)
xlabel("Business days since 2005/1/1")

# 4.
figure(3)
box = boxplot([data[stock]for stock in stock_names])
xtick_locs = range(1, 6)
xticks(xtick_locs, stock_names)

# 5.
figure(4)
scatter(data["AAPL"], data["GOOGL"])
title("Scatter plot of stock prices for AAPL and GOOGL")
xlabel("AAPL")
ylabel("GOOGL")

figure(5)
scatter(data["AAPL"], data["PG"])
title("Scatter plot of stock prices for AAPL and PG")
xlabel("AAPL")
ylabel("PG")

# Bonus
# 6.
figure(6)
num = 0
for i, stock1 in enumerate(stock_names):
    for j, stock2 in enumerate(stock_names):
        num += 1
        subplot(len(stock_names), len(stock_names), num)
        if stock1 != stock2:
            scatter(data[stock2], data[stock1])
        else:
            hist(data[stock1])

        # Put an x label for the last line and a y label to the first column
        if i == len(stock_names) - 1:
            xlabel(stock2)
        if j == 0:
            ylabel(stock1)

show()
