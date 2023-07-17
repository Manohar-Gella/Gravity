import pandas as pd
import yfinance as yf
import talib

# Define the candlestick pattern algorithm
def candlestick_pattern_algorithm(stock_symbol, start_date, end_date, pattern):
    # Download historical stock data
    data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Calculate candlestick patterns
    data['Pattern'] = getattr(talib, pattern)(data['Open'], data['High'], data['Low'], data['Close'])

    # Filter rows with the specified pattern
    pattern_data = data[data['Pattern'] != 0]

    return pattern_data

# Example usage
symbol = 'AAPL'  # Apple stock
start_date = '2010-01-01'
end_date = '2022-12-31'
pattern = 'CDLDOJI'  # Doji candlestick pattern

pattern_data = candlestick_pattern_algorithm(symbol, start_date, end_date, pattern)

# Print the filtered data with the specified candlestick pattern
print(pattern_data)
