# PEACHY PINGS RECENT SALES
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# LIFETIME
peachy_url = 'https://botbroker.io/bots/14/chart?key_type=lifetime&days=365'
response = scraper.get(peachy_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

peachyL = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
peachyR_url = 'https://botbroker.io/bots/14/chart?key_type=renewal&days=365'
response = scraper.get(peachyR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

peachyR = 'No recent sales' if not result else f'${df2[1][0]}'