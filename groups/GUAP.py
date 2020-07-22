# GUAP RECENT SALES
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# LIFETIME
guap_url = 'https://botbroker.io/bots/19/chart?key_type=lifetime&days=365'
response = scraper.get(guap_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

guapL = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
guapR_url = 'https://botbroker.io/bots/19/chart?key_type=renewal&days=365'
response = scraper.get(guapR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

guapR = 'No recent sales' if not result else f'${df2[1][0]}'