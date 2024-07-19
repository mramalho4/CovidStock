!pip install matplotlib seaborn yfinance pandas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import yfinance as yf
import matplotlib.dates as mdates

class StockMarketAnalyzer:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.download_data()
        
    def download_data(self):
        stock_data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        stock_data.reset_index(inplace=True)
        return stock_data
    
    def plot_trend(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Date'], self.data['Close'], label='Close Price')
        plt.title(f'Stock Price Trend for {self.ticker}')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.legend()
        
        # Improve date formatting on x-axis
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # set interval to 3 months
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # format as year-month
        plt.gcf().autofmt_xdate()  # auto-format dates to prevent overlap
        
        plt.show()
    
    def correlation_analysis(self, other_ticker):
        other_data = yf.download(other_ticker, start=self.start_date, end=self.end_date)
        other_data.reset_index(inplace=True)
        merged_data = pd.merge(self.data, other_data, on='Date', suffixes=(f'_{self.ticker}', f'_{other_ticker}'))
        correlation = merged_data[f'Close_{self.ticker}'].corr(merged_data[f'Close_{other_ticker}'])
        return correlation

# Example usage
if __name__ == "__main__":
    analyzer = StockMarketAnalyzer(ticker="AAPL", start_date="2020-01-01", end_date="2022-01-01")
    analyzer.plot_trend()
    correlation = analyzer.correlation_analysis(other_ticker="MSFT")
    print(f'Correlation between AAPL and MSFT: {correlation}')

