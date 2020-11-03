
#  ___      _            _     _____                                     
# / _ \    | |          | |   /  ___|                                    
#/ /_\ \ __| | ___ _ __ | |_  \ `--. _   _ _ __  _ __ ___ _ __ ___   ___ 
#|  _  |/ _` |/ _ \ '_ \| __|  `--. \ | | | '_ \| '__/ _ \ '_ ` _ \ / _ \
#| | | | (_| |  __/ |_) | |_  /\__/ / |_| | |_) | | |  __/ | | | | |  __/
#\_| |_/\__,_|\___| .__/ \__| \____/ \__,_| .__/|_|  \___|_| |_| |_|\___|
#                 | |                     | |                            
#                 |_|                     |_|      
# -----------------------------------------------------------------------------
                      
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# LIFETIME
adept_url = 'https://www.botbroker.io/bots/30/chart?key_type=lifetime&days=365'
response = scraper.get(adept_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

adept = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
adeptR_url = 'https://botbroker.io/bots/30/chart?key_type=renewal&days=365'
response = scraper.get(adeptR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

adeptR = 'No recent sales.' if not result else f'${df2[1][0]}'

#______       _ _         
#| ___ \     | | |        
#| |_/ / __ _| | | _____  
#| ___ \/ _` | | |/ / _ \ 
#| |_/ / (_| | |   < (_) |
#\____/ \__,_|_|_|\_\___/ 
# -----------------------------------------------------------------------------                         

# LIFETIME
balko_url = 'https://www.botbroker.io/bots/8/chart?key_type=lifetime&days=365'
response = scraper.get(balko_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

balko = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
balkoR_url = 'https://botbroker.io/bots/8/chart?key_type=renewal&days=365'
response = scraper.get(balkoR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

balkoR = 'No recent sales.' if not result else f'${df2[1][0]}'

# _____       _                         _      
#/  __ \     | |                       | |     
#| /  \/_   _| |__   ___ _ __ ___  ___ | | ___ 
#| |   | | | | '_ \ / _ \ '__/ __|/ _ \| |/ _ \
#| \__/\ |_| | |_) |  __/ |  \__ \ (_) | |  __/
# \____/\__, |_.__/ \___|_|  |___/\___/|_|\___|
#        __/ |                                 
#       |___/                                  
# -----------------------------------------------------------------------------  

# LIFETIME
cybersole_url = 'https://www.botbroker.io/bots/6/chart?key_type=lifetime&days=365'
response = scraper.get(cybersole_url)
response.raise_for_status()

try:
    result = response.json()
    df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
    result = None

cyber = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
cybersoleR_url = 'https://botbroker.io/bots/6/chart?key_type=renewal&days=365'
response = scraper.get(cybersoleR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

cyberR = 'No recent sales' if not result else f'${df2[1][0]}'

#______          _          
#|  _  \        | |         
#| | | |__ _ ___| |__   ___ 
#| | | / _` / __| '_ \ / _ \
#| |/ / (_| \__ \ | | |  __/
#|___/ \__,_|___/_| |_|\___|
# -----------------------------------------------------------------------------                            
                           
# LIFETIME
dashe_url = 'https://www.botbroker.io/bots/4/chart?key_type=lifetime&days=365'
response = scraper.get(dashe_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

dashe = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
dasheR_url = 'https://botbroker.io/bots/4/chart?key_type=renewal&days=365'
response = scraper.get(dasheR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

dasheR = 'No recent sales.' if not result else f'${df2[1][0]}'

#___  ___ _____ _   ________                        
#|  \/  ||  ___| | / /| ___ \                       
#| .  . || |__ | |/ / | |_/ / __ ___ _ __ ___   ___ 
#| |\/| ||  __||    \ |  __/ '__/ _ \ '_ ` _ \ / _ \
#| |  | || |___| |\  \| |  | | |  __/ | | | | |  __/
#\_|  |_/\____/\_| \_/\_|  |_|  \___|_| |_| |_|\___|
# -----------------------------------------------------------------------------  

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

# _   _      _           _       
#| \ | |    | |         | |      
#|  \| | ___| |__  _   _| | __ _ 
#| . ` |/ _ \ '_ \| | | | |/ _` |
#| |\  |  __/ |_) | |_| | | (_| |
#\_| \_/\___|_.__/ \__,_|_|\__,_|
# -----------------------------------------------------------------------------                                
                                
# LIFETIME
nebula_url = 'https://www.botbroker.io/bots/96/chart?key_type=lifetime&days=365'
response = scraper.get(nebula_url)
response.raise_for_status()

try:
    result = response.json()
    df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
    result = None

nebulaL = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
nebulaR_url = 'https://www.botbroker.io/bots/96/chart?key_type=renewal&days=365'
response = scraper.get(nebulaR_url)
response.raise_for_status()

try:
    result = response.json()
    df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
    result = None

nebulaR = 'No recent sales' if not result else f'${df2[1][0]}'

#______ _                 _                  
#| ___ \ |               | |                 
#| |_/ / |__   __ _ _ __ | |_ ___  _ __ ___  
#|  __/| '_ \ / _` | '_ \| __/ _ \| '_ ` _ \ 
#| |   | | | | (_| | | | | || (_) | | | | | |
#\_|   |_| |_|\__,_|_| |_|\__\___/|_| |_| |_|
# -----------------------------------------------------------------------------                                              
                                            
# LIFETIME
phantom_url = 'https://botbroker.io/bots/2/chart?key_type=lifetime&days=365'
response = scraper.get(phantom_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

phantom = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
phantomR_url = 'https://botbroker.io/bots/2/chart?key_type=renewal&days=365'
response = scraper.get(phantomR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

phantomR = 'No recent sales.' if not result else f'${df2[1][0]}'

#______     _            _     
#| ___ \   | |          (_)    
#| |_/ /__ | | __ _ _ __ _ ___ 
#|  __/ _ \| |/ _` | '__| / __|
#| | | (_) | | (_| | |  | \__ \
#\_|  \___/|_|\__,_|_|  |_|___/
# -----------------------------------------------------------------------------                              
                              
# LIFETIME
polaris_url = 'https://www.botbroker.io/bots/18/chart?key_type=lifetime&days=365'
response = scraper.get(polaris_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

polarisL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
polarisR_url = 'https://botbroker.io/bots/18/chart?key_type=renewal&days=365'
response = scraper.get(polarisR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

polarisR = 'No recent sales.' if not result else f'${df2[1][0]}'

#______     _               
#| ___ \   (_)              
#| |_/ / __ _ ___ _ __ ___  
#|  __/ '__| / __| '_ ` _ \ 
#| |  | |  | \__ \ | | | | |
#\_|  |_|  |_|___/_| |_| |_|
# -----------------------------------------------------------------------------                           
                           
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

#______          _           _    ______          _                             
#| ___ \        (_)         | |   |  _  \        | |                            
#| |_/ / __ ___  _  ___  ___| |_  | | | |___  ___| |_ _ __ ___  _   _  ___ _ __ 
#|  __/ '__/ _ \| |/ _ \/ __| __| | | | / _ \/ __| __| '__/ _ \| | | |/ _ \ '__|
#| |  | | | (_) | |  __/ (__| |_  | |/ /  __/\__ \ |_| | | (_) | |_| |  __/ |   
#\_|  |_|  \___/| |\___|\___|\__| |___/ \___||___/\__|_|  \___/ \__, |\___|_|   
#              _/ |                                              __/ |          
#             |__/                                              |___/           
# -----------------------------------------------------------------------------  

# LIFETIME
projectdestroyer_url = 'https://www.botbroker.io/bots/5/chart?key_type=lifetime&days=365'
response = scraper.get(projectdestroyer_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

pdL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
projectdestroyerR_url = 'https://botbroker.io/bots/5/chart?key_type=renewal&days=365'
response = scraper.get(projectdestroyerR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

pdR = 'No recent sales.' if not result else f'${df2[1][0]}'

# _____           _   _   _           _   
#/  ___|         | | | | | |         | |  
#\ `--.  ___ ___ | |_| |_| |__   ___ | |_ 
# `--. \/ __/ _ \| __| __| '_ \ / _ \| __|
#/\__/ / (_| (_) | |_| |_| |_) | (_) | |_ 
#\____/ \___\___/ \__|\__|_.__/ \___/ \__|
# -----------------------------------------------------------------------------                                           
                                         
# LIFETIME
scottbot_url = 'https://www.botbroker.io/bots/92/chart?key_type=lifetime&days=365'
response = scraper.get(scottbot_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

scottbotL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
scottbotR_url = 'https://botbroker.io/bots/92/chart?key_type=renewal&days=365'
response = scraper.get(scottbotR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

scottbotR = 'No recent sales.' if not result else f'${df2[1][0]}'

# _____       _      
#/  ___|     | |     
#\ `--.  ___ | | ___ 
# `--. \/ _ \| |/ _ \
#/\__/ / (_) | |  __/
#\____/ \___/|_|\___|
# -----------------------------------------------------------------------------                    
                    
# LIFETIME
sole_url = 'https://www.botbroker.io/bots/47/chart?key_type=lifetime&days=365'
response = scraper.get(sole_url)
response.raise_for_status()

try:
    result = response.json()
    df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
    result = None

soleL = 'No recent sales' if not result else f'${df[1][0]}'

# RENEWAL
soleR_url = 'https://botbroker.io/bots/47/chart?key_type=renewal&days=365'
response = scraper.get(soleR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

soleR = 'No recent sales' if not result else f'${df2[1][0]}'

# _____       _           _      __                   
#/  ___|     | |         | |    / _|                  
#\ `--. _ __ | | __ _ ___| |__ | |_ ___  _ __ ___ ___ 
# `--. \ '_ \| |/ _` / __| '_ \|  _/ _ \| '__/ __/ _ \
#/\__/ / |_) | | (_| \__ \ | | | || (_) | | | (_|  __/
#\____/| .__/|_|\__,_|___/_| |_|_| \___/|_|  \___\___|
#      | |                                            
#      |_|                                            
# -----------------------------------------------------------------------------

# RENEWAL
splashforce_url = 'https://botbroker.io/bots/11/chart?key_type=renewal&days=365'
response = scraper.get(splashforce_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

splashforce = 'No recent sales' if not result else f'${df[1][0]}'

# _____           __ _   
#/  ___|         / _| |  
#\ `--.__      _| |_| |_ 
# `--. \ \ /\ / /  _| __|
#/\__/ /\ V  V /| | | |_ 
#\____/  \_/\_/ |_|  \__|
# -----------------------------------------------------------------------------                        
                        
# LIFETIME
swftL_url = 'https://botbroker.io/bots/22/chart?key_type=lifetime&days=365'
response = scraper.get(swftL_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

swftL = 'No recent sales.' if not result else f'${df2[1][0]}'

# RENEWAL
swft_url = 'https://botbroker.io/bots/22/chart?key_type=renewal&days=365'
response = scraper.get(swft_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

swft = 'No recent sales.' if not result else f'${df[1][0]}'

# _____     _                
#|_   _|   | |               
#  | | ___ | |__  _ __ _   _ 
#  | |/ _ \| '_ \| '__| | | |
#  | | (_) | | | | |  | |_| |
#  \_/\___/|_| |_|_|   \__,_|
# -----------------------------------------------------------------------------                             
                            
# LIFETIME
tohru_url = 'https://www.botbroker.io/bots/17/chart?key_type=lifetime&days=365'
response = scraper.get(tohru_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

tohruL = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
tohruR_url = 'https://botbroker.io/bots/17/chart?key_type=renewal&days=365'
response = scraper.get(tohruR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

tohruR = 'No recent sales.' if not result else f'${df2[1][0]}'

# _   _      _           
#| | | |    | |          
#| | | | ___| | _____  __
#| | | |/ _ \ |/ _ \ \/ /
#\ \_/ /  __/ | (_) >  < 
# \___/ \___|_|\___/_/\_\
# -----------------------------------------------------------------------------                        
                        
# LIFETIME
velox_url = 'https://www.botbroker.io/bots/91/chart?key_type=lifetime&days=365'
response = scraper.get(velox_url)
response.raise_for_status()

try:
    result = response.json()
    df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
    result = None

velox = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
veloxR_url = 'https://botbroker.io/bots/91/chart?key_type=renewal&days=365'
response = scraper.get(veloxR_url)
response.raise_for_status()

try:
    result = response.json()
    df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
    result = None

veloxR = 'No recent sales.' if not result else f'${df2[1][0]}'

# _    _           _   _     
#| |  | |         | | | |    
#| |  | |_ __ __ _| |_| |__  
#| |/\| | '__/ _` | __| '_ \ 
#\  /\  / | | (_| | |_| | | |
# \/  \/|_|  \__,_|\__|_| |_|
# -----------------------------------------------------------------------------                             
                            
# LIFETIME
wrath_url = 'https://www.botbroker.io/bots/49/chart?key_type=lifetime&days=365'
response = scraper.get(wrath_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

wrath = 'No recent sales.' if not result else f'${df[1][0]}'

# RENEWAL
wrathR_url = 'https://botbroker.io/bots/49/chart?key_type=renewal&days=365'
response = scraper.get(wrathR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

wrathR = 'No recent sales.' if not result else f'${df2[1][0]}'

#___  ___ _____ _   __  ___  _____ _____ 
#|  \/  ||  ___| | / / / _ \|_   _|  _  |
#| .  . || |__ | |/ / / /_\ \ | | | | | |
#| |\/| ||  __||    \ |  _  | | | | | | |
#| |  | || |___| |\  \| | | |_| |_\ \_/ /
#\_|  |_/\____/\_| \_/\_| |_/\___/ \___/ 
# -----------------------------------------------------------------------------

# RENEWAL
mekaio_url = 'https://botbroker.io/bots/97/chart?key_type=renewal&days=365'     
response = scraper.get(mekaio_url)
response.raise_for_status()

try:
	result = response.json()
	df = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

mekaio = 'No recent sales.' if not result else f'${df[1][0]}'                                      