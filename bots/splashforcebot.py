# SPLASHFORCE RECENT SALE
import requests
import pandas as pd
from pandas import DataFrame

# RENEWAL
splashforce_url = 'https://botbroker.io/bots/11/chart?key_type=renewal&days=365'
response = requests.get(splashforce_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

splashforce = 'No recent sales' if not result else f'${df[1][0]}'