import pandas as pd
import yfinance as yf  # You can use any other library to fetch financial data

# Function to fetch historical stock data
def get_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close']

# Function to implement moving average crossover strategy
def moving_average_crossover_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Create short simple moving average
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Create long simple moving average
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Generate signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Function to visualize the strategy
def visualize_strategy(data, signals):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 8))

    # Plotting the closing price
    data['Close'].plot(ax=ax, label='Close Price')

    # Plotting the short and long moving averages
    signals['short_mavg'].plot(ax=ax, label='Short Moving Average', linestyle='--')
    signals['long_mavg'].plot(ax=ax, label='Long Moving Average', linestyle='--')

    # Plotting buy signals
    ax.plot(signals.loc[signals.positions == 1.0].index,
            signals.short_mavg[signals.positions == 1.0],
            '^', markersize=10, color='g', label='Buy Signal')

    # Plotting sell signals
    ax.plot(signals.loc[signals.positions == -1.0].index,
            signals.short_mavg[signals.positions == -1.0],
            'v', markersize=10, color='r', label='Sell Signal')

    plt.title('Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()

# Main function
if __name__ == '__main__':
    ticker_symbol = 'AAPL'
    start_date = '2020-01-01'
    end_date = '2021-01-01'

    # Fetch historical stock data
    stock_data = get_stock_data(ticker_symbol, start_date, end_date)

    # Define moving average window lengths
    short_window = 40
    long_window = 100

    # Implement moving average crossover strategy
    signals = moving_average_crossover_strategy(stock_data, short_window, long_window)

    # Visualize the strategy
    visualize_strategy(stock_data, signals)
