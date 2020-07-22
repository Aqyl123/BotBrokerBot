# FAKE MONITOR RECENT SALE
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# LIFETIME
fake_url = 'https://www.botbroker.io/bots/94/chart?key_type=lifetime&days=365'
response = scraper.get(fake_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

fakeL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
fakeR_url = 'https://botbroker.io/bots/94/chart?key_type=renewal&days=365'
response = scraper.get(fakeR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

fakeR = 'No recent sales.' if not result else f'${df2[1][0]}'
