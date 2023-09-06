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
start = datetime.datetime(2000, 1, 2)
end = datetime.datetime(2023, 9, 5)

# fetch
petr4 = web.get_data_yahoo('PETR4.SA',start,end) 

# specific data
petr4.head(3)
petr4.tail(3)
petr4.loc['2023-05-22'] 
petr4.loc['2023-06-01':'2023-06-16'] 

# price plot
petr4['Adj Close'].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted")
plt.title("PETR4 Price")
plt.show()

petr4_daily_returns = petr4['Adj Close'].pct_change()
petr4_monthly_returns = petr4['Adj Close'].resample('M').ffill().pct_change()

# daily returns plot
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(petr4_daily_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("PETR4 daily returns data")
plt.show()

# monthly returns plot
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(petr4_monthly_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")  
ax1.set_title("PETR4 monthly returns data")
plt.show()

# histogram
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
petr4_daily_returns.plot.hist(bins = 60)
ax1.set_xlabel("Daily returns %")
ax1.set_ylabel("Percent")
ax1.set_title("PETR4 daily returns data")
ax1.text(-0.35,200,"Extreme Low\nreturns")
ax1.text(0.25,200,"Extreme High\nreturns")
plt.show()
