# RESTOCK WORLD RECENT SALES
import requests
import pandas as pd
from pandas import DataFrame

# RENEWAL
rwR_url = 'https://botbroker.io/bots/13/chart?key_type=renewal&days=365'
response = requests.get(rwR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

rwR = 'No recent sales' if not result else f'${df2[1][0]}'