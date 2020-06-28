# POLARIS RECENT SALE
import requests
import pandas as pd
from pandas import DataFrame

# LIFETIME
polaris_url = 'https://www.botbroker.io/bots/18/chart?key_type=lifetime&days=365'
response = requests.get(polaris_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

polarisL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
polarisR_url = 'https://botbroker.io/bots/18/chart?key_type=renewal&days=365'
response = requests.get(polarisR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

polarisR = 'No recent sales.' if not result else f'${df2[1][0]}'