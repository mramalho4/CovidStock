 Project Summary: Analyzing the Impact of COVID-19 on Stock Market Trends

Problem Description:  
The COVID-19 pandemic significantly impacted global stock markets. This project aims to analyze how the pandemic affected stock prices across different sectors, focusing on specific companies like Apple (AAPL) and Microsoft (MSFT). The hypothesis is that the pandemic caused significant volatility and sector-specific changes in stock prices.

Related Work: 
Previous research has shown that global events, particularly health crises, influence stock markets. Studies have indicated patterns of market downturns followed by recovery periods during such crises.

Solution:  
- Methodology: Time series analysis and correlation analysis.
- Data Collection: Historical stock market data for selected companies during the pandemic, sourced from Yahoo Finance using the `yfinance` library.
- Analysis: Implementing Python functions and classes to clean, process, and analyze the data. Visualization of stock price trends and calculation of correlation between stock prices of different companies.
- Visualization: Using Matplotlib and Seaborn libraries to create clear and informative visualizations.

Code Implementation:
The Python script uses the `yfinance` library to download historical stock prices and analyzes the data with the following key components:
- A `StockMarketAnalyzer` class with methods for downloading data, plotting stock price trends, and performing correlation analysis.
- Improved date formatting on the x-axis for better readability in plots.


By executing this project, I aim to understand the trends and correlations in stock prices during the COVID-19 pandemic, providing insights into the market's response to global events.

