# FAKE MONITOR RECENT SALE
import requests
import pandas as pd
from pandas import DataFrame

# LIFETIME
fake_url = 'https://www.botbroker.io/bots/94/chart?key_type=lifetime&days=365'
response = requests.get(fake_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

fakeL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
fakeR_url = 'https://botbroker.io/bots/94/chart?key_type=renewal&days=365'
response = requests.get(fakeR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

fakeR = 'No recent sales.' if not result else f'${df2[1][0]}'
