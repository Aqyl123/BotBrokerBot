# DROP O'CLOCK RECENT SALES
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# LIFETIME
docL_url = 'https://botbroker.io/bots/95/chart?key_type=lifetime&days=365'
response = scraper.get(docL_url)
response.raise_for_status()
try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

docL = 'No recent sales' if not result else f'${df2[1][0]}'

# RENEWAL
docR_url = 'https://botbroker.io/bots/95/chart?key_type=renewal&days=365'
response = scraper.get(docR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

docR = 'No recent sales' if not result else f'${df2[1][0]}'