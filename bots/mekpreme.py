# MEKPREME RECENT SALE
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# LIFETIME
mekpreme_url = 'https://www.botbroker.io/bots/24/chart?key_type=lifetime&days=365'
response = scraper.get(mekpreme_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

mek = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
mekpremeR_url = 'https://botbroker.io/bots/24/chart?key_type=renewal&days=365'
response = scraper.get(mekpremeR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

mekR = 'No recent sales.' if not result else f'${df2[1][0]}'