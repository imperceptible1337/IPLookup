# libraries
from requests import get
import argparse
import json
import os
import re

# define arguments for argparse
parser = argparse.ArgumentParser(description='Get basic information on an IP\nexample: main.py 1.1.1.1 or main.py m')
parser.add_argument('ip_selection', type=str, help="Your target IP\nm for your IP")
options = parser.parse_args()

ip_selection = options.ip_selection

# set the target IP to the IP the user entered
if ip_selection != "m":
    ip = ip_selection
# but if the user entered 'm', then set the target IP to their IP
else:
    your_ip = get("https://api.ipify.org").text
    ip = your_ip

# get the information for the IP
url = get(f'http://ip-api.com/json/{ip}?fields=continent,continentCode,country,countryCode,region,regionName,city,zip,timezone,currency,isp,org,as,asname,mobile,proxy,hosting')
data = json.loads(url.text)

print('Query :', ip)

for key, value in data.items():
    print(key.capitalize(), ':', value)
