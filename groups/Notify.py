# NOTIFY RECENT SALES
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# LIFETIME
notify_url = 'https://botbroker.io/bots/32/chart?key_type=lifetime&days=365'
response = scraper.get(notify_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

notifyL = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
notifyR_url = 'https://botbroker.io/bots/32/chart?key_type=renewal&days=365'
response = scraper.get(notifyR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

notifyR = 'No recent sales' if not result else f'${df2[1][0]}'