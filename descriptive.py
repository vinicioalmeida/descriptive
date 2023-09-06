# Descriptive statistics

petr4 = web.get_data_yahoo('PETR4.SA',start,end) 
petr4.head(3) # tres primeiros
petr4.tail(3) # tres ultimos
petr4.loc['2023-05-22'] # cotacao em dia especifico
petr4.loc['2023-06-01':'2023-06-16'] # cotacoes em periodo especifico

# grafico de preco
petr4['Adj Close'].plot()
plt.xlabel("Data")
plt.ylabel("Ajustado")
plt.title("Preço de PETR4")
plt.show()

petr4_daily_returns = petr4['Adj Close'].pct_change()
petr4_monthly_returns = petr4['Adj Close'].resample('M').ffill().pct_change()

# grafico diario
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(petr4_daily_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("PETR4 daily returns data")
plt.show()

# grafico mensal
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(petr4_monthly_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")  
ax1.set_title("PETR4 monthly returns data")
plt.show()

# histograma
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
petr4_daily_returns.plot.hist(bins = 60)
ax1.set_xlabel("Daily returns %")
ax1.set_ylabel("Percent")
ax1.set_title("PETR4 daily returns data")
ax1.text(-0.35,200,"Extreme Low\nreturns")
ax1.text(0.25,200,"Extreme High\nreturns")
plt.show()


multpl_stock_daily_returns = multpl_stocks['Adj Close'].pct_change()
multpl_stock_monthly_returns = multpl_stocks['Adj Close'].resample('M').ffill().pct_change()

fig =   plt.figure()
(multpl_stock_monthly_returns + 1).cumprod().plot()
plt.show()

