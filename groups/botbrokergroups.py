import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

#______                               ___  _           _       
#| ___ \                             / _ \| |         | |      
#| |_/ / ___  _   _ _ __   ___ ___  / /_\ \ | ___ _ __| |_ ___ 
#| ___ \/ _ \| | | | '_ \ / __/ _ \ |  _  | |/ _ \ '__| __/ __|
#| |_/ / (_) | |_| | | | | (_|  __/ | | | | |  __/ |  | |_\__ \
#\____/ \___/ \__,_|_| |_|\___\___| \_| |_/_|\___|_|   \__|___/
# ----------------------------------------------------------------------
                                                              
# RENEWAL
bounceR_url = 'https://botbroker.io/bots/88/chart?key_type=renewal&days=365'
response = scraper.get(bounceR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

bounceR = 'No recent sales' if not result else f'${df2[1][0]}'

# _____       _ _               
#/  __ \     | (_)              
#| /  \/ __ _| |_  ___ ___  ___ 
#| |    / _` | | |/ __/ _ \/ __|
#| \__/\ (_| | | | (_| (_) \__ \
# \____/\__,_|_|_|\___\___/|___/
# ----------------------------------------------------------------------                               
                               
# RENEWAL
calicosR_url = 'https://botbroker.io/bots/25/chart?key_type=renewal&days=365'
response = scraper.get(calicosR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

calicosR = 'No recent sales' if not result else f'${df2[1][0]}'

#______                   _____ _ _____ _            _    
#|  _  \                 |  _  ( )  __ \ |          | |   
#| | | |_ __ ___  _ __   | | | |/| /  \/ | ___   ___| | __
#| | | | '__/ _ \| '_ \  | | | | | |   | |/ _ \ / __| |/ /
#| |/ /| | | (_) | |_) | \ \_/ / | \__/\ | (_) | (__|   < 
#|___/ |_|  \___/| .__/   \___/   \____/_|\___/ \___|_|\_\
#                | |                                      
#                |_|                                      
# ---------------------------------------------------------------------- 

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

# _____         _           _          _ 
#|  ___|       | |         | |        | |
#| |____  _____| |_   _  __| | ___  __| |
#|  __\ \/ / __| | | | |/ _` |/ _ \/ _` |
#| |___>  < (__| | |_| | (_| |  __/ (_| |
#\____/_/\_\___|_|\__,_|\__,_|\___|\__,_|
# ----------------------------------------------------------------------                                        
                                        
# RENEWAL
excludedR_url = 'https://botbroker.io/bots/90/chart?key_type=renewal&days=365'
response = scraper.get(excludedR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

excludedR = 'No recent sales' if not result else f'${df2[1][0]}'

#______    _         ___  ___            _ _             
#|  ___|  | |        |  \/  |           (_) |            
#| |_ __ _| | _____  | .  . | ___  _ __  _| |_ ___  _ __ 
#|  _/ _` | |/ / _ \ | |\/| |/ _ \| '_ \| | __/ _ \| '__|
#| || (_| |   <  __/ | |  | | (_) | | | | | || (_) | |   
#\_| \__,_|_|\_\___| \_|  |_/\___/|_| |_|_|\__\___/|_|   
# ----------------------------------------------------------------------                                                       
                                                        
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

# _____ _   _  ___  ______ 
#|  __ \ | | |/ _ \ | ___ \
#| |  \/ | | / /_\ \| |_/ /
#| | __| | | |  _  ||  __/ 
#| |_\ \ |_| | | | || |    
# \____/\___/\_| |_/\_|    
# ----------------------------------------------------------------------                          
                          
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

#___  ___ _____ _   __ _   _       _   _  __         _____  _   _ 
#|  \/  ||  ___| | / /| \ | |     | | (_)/ _|       /  __ \| \ | |
#| .  . || |__ | |/ / |  \| | ___ | |_ _| |_ _   _  | /  \/|  \| |
#| |\/| ||  __||    \ | . ` |/ _ \| __| |  _| | | | | |    | . ` |
#| |  | || |___| |\  \| |\  | (_) | |_| | | | |_| | | \__/\| |\  |
#\_|  |_/\____/\_| \_/\_| \_/\___/ \__|_|_|  \__, |  \____/\_| \_/
#                                             __/ |               
#                                            |___/                
# ----------------------------------------------------------------------                          

# LIFETIME
mekn_url = 'https://botbroker.io/bots/28/chart?key_type=lifetime&days=365'
response = scraper.get(mekn_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

meknL = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
meknR_url = 'https://botbroker.io/bots/28/chart?key_type=renewal&days=365'
response = scraper.get(meknR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

meknR = 'No recent sales' if not result else f'${df2[1][0]}'

# _   _       _   _  __       
#| \ | |     | | (_)/ _|      
#|  \| | ___ | |_ _| |_ _   _ 
#| . ` |/ _ \| __| |  _| | | |
#| |\  | (_) | |_| | | | |_| |
#\_| \_/\___/ \__|_|_|  \__, |
#                        __/ |
#                       |___/ 
# ----------------------------------------------------------------------

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

#______               _            ______ _                 
#| ___ \             | |           | ___ (_)                
#| |_/ /__  __ _  ___| |__  _   _  | |_/ /_ _ __   __ _ ___ 
#|  __/ _ \/ _` |/ __| '_ \| | | | |  __/| | '_ \ / _` / __|
#| | |  __/ (_| | (__| | | | |_| | | |   | | | | | (_| \__ \
#\_|  \___|\__,_|\___|_| |_|\__, | \_|   |_|_| |_|\__, |___/
#                            __/ |                 __/ |    
#                           |___/                 |___/     
# ----------------------------------------------------------------------

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

#______          _             _      _    _            _     _ 
#| ___ \        | |           | |    | |  | |          | |   | |
#| |_/ /___  ___| |_ ___   ___| | __ | |  | | ___  _ __| | __| |
#|    // _ \/ __| __/ _ \ / __| |/ / | |/\| |/ _ \| '__| |/ _` |
#| |\ \  __/\__ \ || (_) | (__|   <  \  /\  / (_) | |  | | (_| |
#\_| \_\___||___/\__\___/ \___|_|\_\  \/  \/ \___/|_|  |_|\__,_|
# ----------------------------------------------------------------------                                                               
                                                               
# RENEWAL
rwR_url = 'https://botbroker.io/bots/13/chart?key_type=renewal&days=365'
response = scraper.get(rwR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

rwR = 'No recent sales' if not result else f'${df2[1][0]}'

# _____       _              
#/  ___|     | |             
#\ `--.  __ _| |__  _ __ ___ 
# `--. \/ _` | '_ \| '__/ _ \
#/\__/ / (_| | |_) | | |  __/
#\____/ \__,_|_.__/|_|  \___|
# ----------------------------------------------------------------------                             
                            
# LIFETIME
sabre_url = 'https://www.botbroker.io/bots/89/chart?key_type=lifetime&days=365'
response = scraper.get(sabre_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

sabreL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
sabreR_url = 'https://botbroker.io/bots/89/chart?key_type=renewal&days=365'
response = scraper.get(sabreR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

sabreR = 'No recent sales.' if not result else f'${df2[1][0]}'

# _____ _ _         _____                   _       
#/  ___(_) |       /  ___|                 | |      
#\ `--. _| |_ ___  \ `--. _   _ _ __  _ __ | |_   _ 
# `--. \ | __/ _ \  `--. \ | | | '_ \| '_ \| | | | |
#/\__/ / | ||  __/ /\__/ / |_| | |_) | |_) | | |_| |
#\____/|_|\__\___| \____/ \__,_| .__/| .__/|_|\__, |
#                              | |   | |       __/ |
#                              |_|   |_|      |___/ 
# ----------------------------------------------------------------------

# LIFETIME
ss_url = 'https://botbroker.io/bots/23/chart?key_type=lifetime&days=365'
response = scraper.get(ss_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

ssL = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
ssR_url = 'https://botbroker.io/bots/23/chart?key_type=renewal&days=365'
response = scraper.get(ssR_url)
response.raise_for_status()
try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

ssR = 'No recent sales' if not result else f'${df2[1][0]}'

# _____ _____ __  
#|____ |  ___/  | 
#    / /___ \`| | 
#    \ \   \ \| | 
#.___/ /\__/ /| |_
#\____/\____/\___/
# ----------------------------------------------------------------------                 
                 
# RENEWAL
threefiveoneR_url = 'https://botbroker.io/bots/16/chart?key_type=renewal&days=365'
response = scraper.get(threefiveoneR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

threefiveoneR = 'No recent sales' if not result else f'${df2[1][0]}'