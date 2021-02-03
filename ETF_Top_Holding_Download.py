import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

# can be from any ETF
holding_data = yf.download("TSLA ROKU TDOC SQ TCEHY GBTC SPOT API NFLX FSLY", start="2014-01-01", end="2020-12-31")

# see the downloaded dataframe
holding_data.head()

# plot the data into a chart
holding_data['Close'].plot(title="AKRW Top Holding Price")

# now let's export the downloaded data to a spreadsheet
import os
os.chdir("/Users/ ")
holding_data.to_csv('AKRW_Top_Holding_Data.csv', encoding='utf-8')
