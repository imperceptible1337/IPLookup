from colorama import Fore
from requests import get
import colorama
colorama.init()
import requests
import json
import os

os.system('cls' if os.name=='nt' else 'clear')

print(f'          {Fore.YELLOW}< {Fore.WHITE}-------- {Fore.YELLOW}>')
print(f'{Fore.YELLOW}< {Fore.WHITE}- {Fore.CYAN}Made by "{Fore.RED}nameless#2056{Fore.CYAN}" {Fore.WHITE}- {Fore.YELLOW}>')
print(f'          {Fore.YELLOW}< {Fore.WHITE}-------- {Fore.YELLOW}>')
print()

IP_SELECTION = input(f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Enter an IP, or enter {Fore.WHITE}m{Fore.CYAN} for your IP {Fore.YELLOW}> {Fore.RED}')
if IP_SELECTION != "m":
    IP = IP_SELECTION
else:
    YOUR_IP = get("https://api.ipify.org").text
    IP = YOUR_IP
URL = requests.get(f'http://ip-api.com/json/{IP}?fields=continent,continentCode,country,countryCode,region,regionName,city,zip,timezone,currency,isp,org,as,asname,reverse,mobile,proxy,hosting')
DATA = json.loads(URL.text)
DATA = json.dumps(DATA)

os.system('cls' if os.name=='nt' else 'clear')

print(f'          {Fore.YELLOW}< {Fore.WHITE}-------- {Fore.YELLOW}>')
print(f'{Fore.YELLOW}< {Fore.WHITE}- {Fore.CYAN}Made by "{Fore.RED}nameless#2056{Fore.CYAN}" {Fore.WHITE}- {Fore.YELLOW}>')
print(f'          {Fore.YELLOW}< {Fore.WHITE}-------- {Fore.YELLOW}>')
print(f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Query {Fore.YELLOW}> {Fore.GREEN} {IP}')
print()
print(DATA[2:-2].replace('", "', '\n').replace('": "', ' > ').replace(', "', '\n').replace('": ', ' > ').replace('continent > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Continent {Fore.YELLOW}> {Fore.GREEN}').replace('continentCode > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Continent Code {Fore.YELLOW}> {Fore.GREEN}').replace('country > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Country {Fore.YELLOW}> {Fore.GREEN}').replace('countryCode > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Country Code {Fore.YELLOW}> {Fore.GREEN}').replace('region > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Region {Fore.YELLOW}> {Fore.GREEN}').replace('regionName > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Region Name {Fore.YELLOW}> {Fore.GREEN}').replace('city > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} City {Fore.YELLOW}> {Fore.GREEN}').replace('zip > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Zip Code {Fore.YELLOW}> {Fore.GREEN}').replace('timezone > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Time Zone {Fore.YELLOW}> {Fore.GREEN}').replace('currency > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Currency {Fore.YELLOW}> {Fore.GREEN}').replace('isp > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} ISP {Fore.YELLOW}> {Fore.GREEN}').replace('org > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} ORG {Fore.YELLOW}> {Fore.GREEN}').replace('as > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} AS {Fore.YELLOW}> {Fore.GREEN}').replace('asname > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} AS Name {Fore.YELLOW}> {Fore.GREEN}').replace('reverse > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Reverse {Fore.YELLOW}> {Fore.GREEN}').replace('mobile > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Mobile {Fore.YELLOW}> {Fore.GREEN}').replace('proxy', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Proxy {Fore.YELLOW}> {Fore.GREEN}').replace('hosting > ', f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}-{Fore.LIGHTBLUE_EX}]{Fore.CYAN} Hosting {Fore.YELLOW}> {Fore.GREEN}'))
