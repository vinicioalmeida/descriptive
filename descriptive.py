# Descriptive statistics
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.2f' % x)
import numpy as np
import datetime
import pandas_datareader.data as web   #pandas-datareader
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt
from IPython.core.display import display, HTML   #ipython
display(HTML("<style>.container { width:100% !important; }</style>"))

# dates
start = datetime.datetime(2007, 1, 2)
end = datetime.datetime(2023, 9, 5)

# fetch
bvsp = web.get_data_yahoo('^BVSP',start,end) 

# specific dates
bvsp.head(3)
bvsp.tail(3)
bvsp.loc['2023-05-22'] 
bvsp.loc['2023-06-01':'2023-06-16'] 

# price plot
bvsp['Adj Close'].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted")
plt.title("Ibov Price")
plt.show()

bvsp_daily_returns = bvsp['Adj Close'].pct_change()
bvsp_monthly_returns = bvsp['Adj Close'].resample('M').ffill().pct_change()

# daily returns plot
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(bvsp_daily_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("Ibov daily returns data")
plt.show()

# monthly returns plot
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(bvsp_monthly_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")  
ax1.set_title("Ibov monthly returns data")
plt.show()

# histogram
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
bvsp_daily_returns.plot.hist(bins = 60)
ax1.set_xlabel("Daily returns %")
ax1.set_ylabel("Percent")
ax1.set_title("Ibov daily returns data")
ax1.text(-0.35,200,"Extreme Low\nreturns")
ax1.text(0.25,200,"Extreme High\nreturns")
plt.show()
