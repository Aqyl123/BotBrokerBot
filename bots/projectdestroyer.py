# PROJECT DESTROYER RECENT SALE
import requests
import pandas as pd
from pandas import DataFrame

# LIFETIME
projectdestroyer_url = 'https://www.botbroker.io/bots/5/chart?key_type=lifetime&days=365'
response = requests.get(projectdestroyer_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

pdL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
projectdestroyerR_url = 'https://botbroker.io/bots/5/chart?key_type=renewal&days=365'
response = requests.get(projectdestroyerR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

pdR = 'No recent sales.' if not result else f'${df2[1][0]}'