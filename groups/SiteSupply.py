# SITE SUPPLY RECENT SALES
import requests
import pandas as pd
from pandas import DataFrame

# LIFETIME
ss_url = 'https://botbroker.io/bots/23/chart?key_type=lifetime&days=365'
response = requests.get(ss_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

ssL = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
ssR_url = 'https://botbroker.io/bots/23/chart?key_type=renewal&days=365'
response = requests.get(ssR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

ssR = 'No recent sales' if not result else f'${df2[1][0]}'