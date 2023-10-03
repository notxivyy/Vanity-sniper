import requests as client
from sys import platform
import os, time
Clear = None
if platform == "linux" or platform == "linux2":
    Clear = lambda: os.system("clear")
elif platform == "darwin":
    Clear = lambda: os.system("clear")
elif platform == "win32":
    Clear = lambda: os.system("cls")
requests = client.Session()
def header(token):
  return  {
        'authority': 'discord.com',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc5ODgyLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMDMwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
        'x-discord-locale': 'en',
        'x-debug-options': 'bugReporterEnabled',
        'accept-language': 'en',
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9011 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
         }

def main():
 eval("Clear()")
 guildid=input('-> Server Id: ')
 vainty = input('-> Vanity: ')
 toknan = input('-> Token: ')
 delay = float(input('-> Delay: '))
 headier = header(toknan);r=requests.get(f"https://discord.com/api/v10/guilds/{guildid}", headers=headier)
 if r.status_code==200:
   while 1==1:
     pluh = requests.get(f'https://discord.com/api/v10/invites/{vainty}', headers=headier)
     if pluh.status_code != 200:
       rir = requests.patch('https://discord.com/api/v10/guilds/'+guildid+'/vanity-url',headers=headier, json={'code': vainty})
       try:
         rir.raise_for_status()
         print('Successfully Was Claimed.')
         return
       except:
         print('Tried to claim but failure')
     else:
       print('Invite Unavailable, Didnt try to claim.')
     time.sleep(delay)
   
main()
input('Press Entre To Exit: ')
