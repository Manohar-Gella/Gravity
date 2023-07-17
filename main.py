import pandas as pd
import yfinance as yf

# Define the moving average crossover strategy
def moving_average_crossover_strategy(stock_symbol, short_window, long_window):
    # Download historical stock data
    data = yf.download(stock_symbol, start='2010-01-01', end='2022-12-31')
    
    # Calculate short-term moving average
    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    
    # Calculate long-term moving average
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()
    
    # Initialize the position
    position = None
    
    # Initialize a list to store the trading signals
    signals = []
    
    # Iterate over the data
    for i in range(len(data)):
        # Generate buy signal
        if data['Short_MA'][i] > data['Long_MA'][i] and position != 'Buy':
            signals.append((data.index[i], 'Buy'))
            position = 'Buy'
        
        # Generate sell signal
        elif data['Short_MA'][i] < data['Long_MA'][i] and position != 'Sell':
            signals.append((data.index[i], 'Sell'))
            position = 'Sell'
        
        # No action
        else:
            signals.append((data.index[i], 'Hold'))
    
    return signals

# Example usage
symbol = 'AAPL'  # Apple stock
short_window = 50  # Short-term moving average window
long_window = 200  # Long-term moving average window

signals = moving_average_crossover_strategy(symbol, short_window, long_window)

# Print the trading signals
for signal in signals:
    print(signal)
