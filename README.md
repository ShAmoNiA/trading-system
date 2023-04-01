# trading-system

This is an automated trading system for cryptocurrencies based on technical analysis. The strategy is based on a Moving Average Crossover (MAC) and uses Bollinger Bands to determine when to buy and sell. This project uses Python and the Binance API to access real-time market data and execute trades.

## Requirements
Python 3.x
Binance API key and secret
## Installation
Clone this repository: git clone https://github.com/ShAmoNiA/trading-system.git

Install required packages: pip install -r requirements.txt

Set API key and secret as environment variables:

Windows: setx BINANCE_API_KEY "your_api_key" and setx BINANCE_SECRET_KEY "your_secret_key"

Linux/Mac: export BINANCE_API_KEY="your_api_key" and export BINANCE_SECRET_KEY="your_secret_key"

## Usage
Open a terminal and navigate to the project directory.
Run the script:
```
python trading_system.py
```
The program will continuously monitor the cryptocurrency market and execute trades based on the trading strategy.

To stop the program, press Ctrl + C.
## Customization
You can customize the trading strategy by changing the trading parameters in the trading_system.py file:

1.symbol: Cryptocurrency symbol to trade (e.g. BTCUSDT for Bitcoin/USDT pair).

2.quantity: Buy/sell quantity.

3.macd_short: MACD short period.

4.macd_long: MACD long period.

5.signal_period: MACD signal period.

6.bb_period: Bollinger Bands period.

7.bb_std: Bollinger Bands standard deviation.

You can also modify the buy/sell conditions by changing the if statements in the trading loop.

## Disclaimer
This project is for educational purposes only and should not be used for real trading without thorough testing and understanding of the risks involved. I am not responsible for any losses incurred as a result of using this software.
