"""
Download the stock data from Yahoo API and save to a local file.

Used to generate the data file in this exercise.

"""
import datetime
from pandas import DataFrame
import pandas.io.data as web


outfile = 'adj_close_stock_data_2005_2010.txt'
start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2009, 12, 31)
symbols = ["AAPL", "GOOGL", "MSFT", "PG", "XOM"]
result = {}
for symbol in symbols:
    data = web.DataReader(symbol, 'yahoo', start, end)
    result[symbol] = data['Adj Close']
df = DataFrame(result)
df.insert(0, 'year', df.index.year)
df.insert(1, 'month', df.index.month)
df.insert(2, 'day', df.index.day)
df.to_csv(open(outfile, 'w'), sep=' ', float_format='%4.2f', index=False)
