import requests
import pandas as pd
import matplotlib.pyplot as plt
import ctypes
import os

# Forex URL
url = 'https://fxmarketapi.com/apipandas'

# API Key
api_key = os.environ.get('access_token_forex_api')

# API Parameters
params = {
    'currency' : 'GBPUSD',
    'start_date' : '2021-01-08',
    'end_date' : '2022-01-10',
    'api_key' : api_key
}

# Contact API, read the response into a dataframe
response = requests.get(url=url, params=params)
df = pd.read_json(response.text)

# Dataframe needs to be flattened to plot
flat_df = pd.DataFrame(df.to_records())
flat_df = flat_df.rename(columns={'index' : 'date'})
flat_df.to_csv('exchange_values.csv')

# Print to terminal
today_date = flat_df['date'].iloc[-1].strftime('%Y-%m-%d')
latest_value = flat_df['open'].iloc[-1]
prev_value = flat_df['open'].iloc[-2]
print(f'{today_date}: The exchange rate is {latest_value}')

# Pop up window
ctypes.windll.user32.MessageBoxW(0, f'{today_date}: The exchange rate is {latest_value}. Yesterday it was {prev_value}.', 'Exchange Rate')

# def popup(title, text, style): 
#     return ctypes.windll.user32.MessageBoxW(0, text, title, style)

##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | Cancel 
##  6 : Cancel | Try Again | Continue

# Assign axis to values
x = flat_df['date']
y = flat_df['open']

# Plot the graph
fig = plt.figure(figsize=(15,6))
plt.xticks(rotation=90)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Exchange Rate', fontsize=12)
plt.plot(x, y)
plt.style.use('seaborn')
plt.tight_layout()
plt.savefig(f'{today_date}.png')

