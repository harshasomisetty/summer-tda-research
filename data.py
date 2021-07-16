import yfinance as yf
import pandas as pd

def download_data(tickers):
    return yf.download(tickers, start="2008-01-01", end="2009-06-01", interval = "1d", group_by = "ticker")

def save_data(data, location):
    data.to_csv(location)

def load_data(location):
    return pd.read_csv(location)
