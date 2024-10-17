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

print(adj_close_df)

