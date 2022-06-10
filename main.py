# libraries
from colorama import Fore
from requests import get
import colorama
import requests
import argparse
import json
import os

# initialize colorama
colorama.init()

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
data = json.dumps(data)

# print the information
print(f'{Fore.CYAN}Query {Fore.YELLOW}> {Fore.GREEN} {ip}')
print(data[2:-1].replace('", "', '\n').replace('": "', ' > ').replace(', "', '\n').replace('": ', ' > ').replace('continent > ', f'{Fore.CYAN}Continent {Fore.YELLOW}> {Fore.GREEN}').replace('continentCode > ', f'{Fore.CYAN}Continent Code {Fore.YELLOW}> {Fore.GREEN}').replace('country > ', f'{Fore.CYAN}Country {Fore.YELLOW}> {Fore.GREEN}').replace('countryCode > ', f'{Fore.CYAN}Country Code {Fore.YELLOW}> {Fore.GREEN}').replace('region > ', f'{Fore.CYAN}Region {Fore.YELLOW}> {Fore.GREEN}').replace('regionName > ', f'{Fore.CYAN}Region Name {Fore.YELLOW}> {Fore.GREEN}').replace('city > ', f'{Fore.CYAN}City {Fore.YELLOW}> {Fore.GREEN}').replace('zip > ', f'{Fore.CYAN}Zip Code {Fore.YELLOW}> {Fore.GREEN}').replace('timezone > ', f'{Fore.CYAN}Time Zone {Fore.YELLOW}> {Fore.GREEN}').replace('currency > ', f'{Fore.CYAN}Currency {Fore.YELLOW}> {Fore.GREEN}').replace('isp > ', f'{Fore.CYAN}ISP {Fore.YELLOW}> {Fore.GREEN}').replace('org > ', f'{Fore.CYAN}ORG {Fore.YELLOW}> {Fore.GREEN}').replace('as > ', f'{Fore.CYAN}AS {Fore.YELLOW}> {Fore.GREEN}').replace('asname > ', f'{Fore.CYAN}AS Name {Fore.YELLOW}> {Fore.GREEN}').replace('mobile > ', f'{Fore.CYAN}Mobile {Fore.YELLOW}> {Fore.GREEN}').replace('proxy', f'{Fore.CYAN}Proxy {Fore.YELLOW}> {Fore.GREEN}').replace('hosting > ', f'{Fore.CYAN}Hosting {Fore.YELLOW}> {Fore.GREEN}'))
