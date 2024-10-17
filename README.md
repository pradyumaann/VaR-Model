# Value at Risk (VaR) Model

This repository contains a Python script that calculates the Value at Risk (VaR) for a diversified portfolio of securities over a given time period. The model uses historical data to estimate the risk associated with potential losses in the portfolio, leveraging log returns, covariance matrices, and confidence intervals to present meaningful insights.

## Files
- **main.py**: The Python script that downloads financial data, calculates historical portfolio returns, and estimates VaR at multiple confidence levels.

## Dependencies
To run the script, you will need the following libraries:
- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `yfinance`

You can install them using pip:
```bash
pip install numpy pandas matplotlib scipy yfinance
```

## Data Source
The model uses **Yahoo Finance** to fetch historical adjusted close prices for the selected securities. The tickers included in this portfolio are:
- SPY (S&P 500 ETF)
- BND (Bond Index ETF)
- GLD (Gold ETF)
- QQQ (NASDAQ-100 ETF)
- VTI (Total Stock Market ETF)

These tickers represent a diversified portfolio, including equities, bonds, and gold.

## Model Overview
The script:
1. **Fetches historical data** for a 15-year period.
2. **Calculates log returns** for each security in the portfolio.
3. **Constructs an equally weighted portfolio** using the given securities.
4. **Calculates historical returns** over a rolling window of 20 days.
5. **Estimates the portfolio’s volatility** using a covariance matrix of returns.
6. **Computes Value at Risk (VaR)** at three different confidence levels: 90%, 95%, and 99%.
7. **Visualizes the results** by plotting the distribution of portfolio returns and adding lines to indicate the VaR at each confidence level.

### VaR Calculation
The VaR is calculated based on the following steps:
- Compute the portfolio's standard deviation using the covariance matrix and the asset weights.
- Use the standard deviation and portfolio value to estimate the potential losses over a 20-day period, assuming a normal distribution of returns.
- The model computes VaR at 90%, 95%, and 99% confidence levels.

### Visualization
The script creates a histogram of the portfolio's historical 20-day returns and marks the VaR thresholds for each confidence level, allowing users to visualize the risk associated with their portfolio.

## Running the Script
Simply run the `main.py` script to fetch the data, calculate VaR, and display the results:
```bash
python main.py
```

The script will print the VaR estimates at different confidence levels and display a plot showing the distribution of returns and the calculated VaR points.

## Example Output
The output will include a table similar to the following:

```
Confidence Level    Value at Risk      
----------------------------------------
   90%:             $ -24,000.00
   95%:             $ -35,000.00
   99%:             $ -50,000.00
```

The visualization will display a histogram of the portfolio's historical returns with vertical lines representing the calculated VaR at each confidence level.

## Customization
You can modify the following parameters:
- **`tickers`**: Add or remove financial instruments to include in your portfolio.
- **`years`**: Adjust the number of years of historical data to analyze.
- **`days`**: Change the rolling window period used to calculate returns (default is 20 days).
- **`weights`**: Customize the allocation of assets in your portfolio by changing the weights assigned to each security.

## License
This project is open source and available under the [MIT License](LICENSE).

Feel free to modify and extend this model to suit your specific portfolio and risk analysis needs!
