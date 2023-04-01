import os
import pandas as pd
from binance.client import Client
from ta.trend import MACD
from ta.volatility import BollingerBands
import time

# Set API keys and secret
api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_SECRET_KEY')
client = Client(api_key, api_secret)

# Set trading parameters
symbol = 'BTCUSDT'
quantity = 0.001  # Buy/sell quantity
macd_short = 12  # MACD short period
macd_long = 26  # MACD long period
signal_period = 9  # MACD signal period
bb_period = 20  # Bollinger Bands period
bb_std = 2  # Bollinger Bands standard deviation
buy_price = 0.0  # Last buy price

# Trading loop
while True:
    try:
        # Get historical data
        klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
        data = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'trades', 'taker_buy_base', 'taker_buy_quote', 'ignore'])
        data = data.set_index('timestamp')
        data.index = pd.to_datetime(data.index, unit='ms')
        data = data[['open', 'high', 'low', 'close', 'volume']]

        # Calculate MACD and Bollinger Bands
        macd = MACD(data['close'], window_slow=macd_long, window_fast=macd_short, window_sign=signal_period)
        data['macd'] = macd.macd()
        data['macd_signal'] = macd.macd_signal()
        data['macd_histogram'] = macd.macd_diff()
        bb = BollingerBands(data['close'], window=bb_period, window_dev=bb_std)
        data['bb_high'] = bb.bollinger_hband()
        data['bb_low'] = bb.bollinger_lband()

        # Buy if MACD crosses above signal line and price is above upper Bollinger Band
        if macd.macd()[-1] > macd.macd_signal()[-1] and data['close'][-1] > data['bb_high'][-1]:
            order = client.create_order(
                symbol=symbol,
                side=Client.SIDE_BUY,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity)
            buy_price = data['close'][-1]
            print('Bought at', buy_price)

        # Sell if MACD crosses below signal line or price is below lower Bollinger Band
        elif (macd.macd()[-1] < macd.macd_signal()[-1] or data['close'][-1] < data['bb_low'][-1]) and buy_price > 0:
            order = client.create_order(
                symbol=symbol,
                side=Client.SIDE_SELL,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity)
            buy_price = 0.0
            print('Sold at', data['close'][-1])

    except Exception as e:
        print('Error:', e)

    # Wait for 1 minute
    time.sleep(60)
