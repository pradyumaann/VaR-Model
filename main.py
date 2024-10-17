import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm

years = 15

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365*years)

tickers = ['SPY','BND','GLD','QQQ','VTI']

#download adjusted close prices as they account for dividend stock splits
adj_close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start = startDate, end = endDate)
    adj_close_df[ticker] = data['Adj Close']


#calculate daily log returns and drop any NAs
log_returns = np.log(adj_close_df/adj_close_df.shift(1))
log_returns = log_returns.dropna()

#create an equally weighted portfolio
portfolio_value = 1000000
weights = np.array([1/len(tickers)]*len(tickers))

#calculate the historical portfolio returns
historical_returns = (log_returns * weights).sum(axis = 1)
days = 5
historical_x_day_returns = historical_returns.rolling(window=days).sum()

#create a covariance matrix for all securities
cov_matrix = log_returns.cov() * 252

#calculate the standard deviation of portfolio
portfolio_std_dev = np.sqrt(weights.T @ cov_matrix @ weights)

#set different confidence levels to calculate and visualize 
confidence_levels = [0.9, 0.95, 0.99]
Vars = []

for cl in confidence_levels:
    Var = portfolio_value * portfolio_std_dev * norm.ppf(cl) *np.sqrt(days/252)
    Vars.append(Var)
    