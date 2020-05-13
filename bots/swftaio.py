# SWFTAIO RECENT SALE
import requests
import pandas as pd
from pandas import DataFrame

# LIFETIME
swftL_url = 'https://botbroker.io/bots/22/chart?key_type=lifetime&days=365'
response = requests.get(swftL_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

swftL = 'No recent sales.' if not result else f'${df2[1][0]}'

# RENEWAL
swft_url = 'https://botbroker.io/bots/22/chart?key_type=renewal&days=365'
response = requests.get(swft_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

swft = 'No recent sales.' if not result else f'${df[1][0]}'