import pandas as pd
import numpy as np

def generate_ohlcv_data(start_date, end_date, freq='1h'):
    dates = pd.date_range(start=start_date, end=end_date, freq=freq)
    n = len(dates)
    price = np.cumsum(np.random.randn(n)) + 100
    open_ = price + np.random.uniform(-1, 1, n)
    close = open_ + np.random.uniform(-2, 2, n)
    high = np.maximum(open_, close) + np.random.uniform(0, 2, n)
    low = np.minimum(open_, close) - np.random.uniform(0, 2, n)
    volume = np.random.randint(100, 1000, n)
    df = pd.DataFrame({
        'datetime': dates,
        'open': open_,
        'high': high,
        'low': low,
        'close': close,
        'volume': volume
    })
    return df

if __name__ == "__main__":
    df = generate_ohlcv_data('2024-01-01', '2024-01-10')
    df.to_csv('ohlcv_data.csv', index=False)
