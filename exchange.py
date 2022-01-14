import requests
import pandas as pd
import matplotlib.pyplot as plt
import ctypes
import os
import logging
from datetime import date, datetime, timedelta

dir = os.cwd()
os.chdir(dir)

# Variables
prev30days = date.today() - timedelta(30)
end_date = date.today()
currency1 = 'GBP'
currency2 = 'USD'

# output log
logging.basicConfig(filename='output.log')

# Forex URL
url = 'https://fxmarketapi.com/apipandas'

# API Key
api_key = os.environ.get('access_token_forex_api')

# API Parameters
params = {
    'currency' : currency1+currency2,
    'start_date' : prev30days,
    'end_date' : end_date,
    'api_key' : api_key
}

# Contact API, read the response into a dataframe
response = requests.get(url=url, params=params)
df = pd.read_json(response.text)

# Print to terminal
today_date = df.index[-1].strftime('%Y-%m-%d')
latest_value = df.open[-1]
prev_value = df.open[-2]
print(f'{today_date}: The exchange rate is {latest_value}')

# Pop up window
ctypes.windll.user32.MessageBoxW(0, f'{today_date}: The exchange rate is {latest_value}. Yesterday it was {prev_value}.', 'Exchange Rate')

# # def popup(title, text, style): 
# #     return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# ##  Styles:
# ##  0 : OK
# ##  1 : OK | Cancel
# ##  2 : Abort | Retry | Ignore
# ##  3 : Yes | No | Cancel
# ##  4 : Yes | No
# ##  5 : Retry | Cancel 
# ##  6 : Cancel | Try Again | Continue

# Define up and down
up = df[df.close >= df.open]
down = df[df.close < df.open]


# colours
col1 = 'green'
col2 = 'red'

# Plot the up values
plt.figure(figsize=(15,6))
plt.bar(up.index, up.close - up.open, width =.4, bottom = up.open, color=col1)
plt.bar(up.index, up.high - up.close, width =.05, bottom = up.close, color=col1)
plt.bar(up.index, up.low - up.open, width = 0.05, bottom = up.open, color=col1)

# Plot the down values
plt.bar(down.index, down.close - down.open, width =.4, bottom = down.open, color=col2)
plt.bar(down.index, down.high - down.open, width =.05, bottom = down.open, color=col2)
plt.bar(down.index, down.low - down.close, width = 0.05, bottom = down.close, color=col2)

# Format the graph
plt.xticks(rotation = 90, ha='right')
plt.ylabel('Exchange Rate', fontsize=12)
plt.title(f'Showing exchange rate: {currency1} to {currency2} over last 30 days', loc='left', fontweight='bold')
plt.style.use('seaborn')
plt.tight_layout()
plt.savefig(f'{date.today()}.png')

# Show the graph
plt.show()







