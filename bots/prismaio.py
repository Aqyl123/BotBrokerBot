# PRISM RECENT SALE
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# RENEWAL
prism_url = 'https://botbroker.io/bots/10/chart?key_type=renewal&days=365'
response = scraper.get(prism_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

prism = 'No recent sales.' if not result else f'${df[1][0]}'