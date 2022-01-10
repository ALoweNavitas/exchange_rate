from forex_python.converter import CurrencyRates
from datetime import datetime, date
import csv
import pandas as pd

c = CurrencyRates()
today_date = datetime.today().strftime('%Y-%m-%d')

exchange_rate = c.get_rate('GBP', 'USD')

print(f'{today_date}: The exchange rate is {exchange_rate}')

with open('exchange_rate\exchange_rates.txt', 'a') as log:
    log.write(f'{today_date}: The exchange rate is {exchange_rate}' + '\n')

with open('exchange_rate\exchange_rates.csv', 'a') as csvfile:
    fieldnames = ['date', 'value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # writer.writeheader()
    writer.writerow({'date' : today_date, 'value' : exchange_rate})

df = pd.read_csv('exchange_rate\exchange_rates.csv')
print(df.head())