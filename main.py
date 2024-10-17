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
days = 20
historical_x_day_returns = historical_returns.rolling(window=days).sum()

#create a covariance matrix for all securities
cov_matrix = log_returns.cov() * 252

#calculate the standard deviation of portfolio
portfolio_std_dev = np.sqrt(weights.T @ cov_matrix @ weights)

#set different confidence levels to calculate and visualize 
confidence_levels = [0.9, 0.95, 0.99]
VaRs = []

for cl in confidence_levels:
    z_score = norm.ppf(1-cl)
    VaR = portfolio_value * portfolio_std_dev * z_score *np.sqrt(days/252)
    VaRs.append(VaR)

#print out Var results
print(f'{"Confidence Level":<20}{"Value at Risk":<20}')
print('-'*40)

for cl, VaR in zip(confidence_levels, VaRs):
    print(f'{cl * 100:>6.0f}%: {"":<8} ${VaR:>10,.2f}')

#convert returns to dollar values for the histogram
historical_x_days_returns_dollar = historical_x_day_returns * portfolio_value
#plot the histogram
plt.hist(historical_x_days_returns_dollar, bins = 50, density=True, alpha = 0.5, label=f'{days}-Day Returns')

#add vertical lines representing VaR at each confidence level
colors = ['g','b','r']
for cl, VaR, c in zip(confidence_levels, VaRs, colors):
    plt.axvline(x=VaR, linestyle='--', color=c, label='VaR at {}%Confidence'.format(int(cl*100)))
    
plt.xlabel(f'{days}-Day Portfolio Return ($)')
plt.ylabel('Frequency')
plt.title(f'Distribution of Portfolio {days}-Day Returns and Parametric VaR Estimates')
plt.legend()
plt.show()