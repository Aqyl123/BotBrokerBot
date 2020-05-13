# CALICOS RECENT SALES
import requests
import pandas as pd
from pandas import DataFrame

# RENEWAL
calicosR_url = 'https://botbroker.io/bots/25/chart?key_type=renewal&days=365'
response = requests.get(calicosR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

calicosR = 'No recent sales' if not result else f'${df2[1][0]}'