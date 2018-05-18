import sys
import os
import random
from random import randint


print('''For help type in help.
When typing a command please ignore spaces
and special characters \"such as -\" in the input
''')
while True:
    userInput = input()
    if userInput == 'help':
        print('''Enter the name of the node and level to show statistics of
For example, Typing in "BcoinMine 1" without quotes will
show the statistics of Bcoin Mine level 1
The names of the nodes are as follow:
BcoinMine
BcoinMixer
netConnection
Core
Database
ServerFarm
BlackICE
CodeGate
Guardian
Scanner
Sentry
Turret
Compiler
Evolver
ProgramLibrary
For program statistics and Stealth calculator please refer to
pyprograms.py and stealthcalc.py
''')
    elif userInput == 'BcoinMine 1':
        print('''Showing statistics for BcoinMine level 1:
Firewall: 150
Production speed (Hourly): 16B
Production limit (Total): 24B
Exfiltration (Transfer) per second: 1B
Construction cost: $250
Completion time (1 building thread): 1 Minute
Requires core level: 1
''')
    elif userInput == 'BcoinMine 2':
        print('''Showing statistics for BcoinMine level 2:
Firewall: 165
Production speed (Hourly): 24B
Production limit (Total): 48B
Exfiltration (Transfer) per second: 1B
Upgrade cost: $500
Completion time (1 building thread): 5 Minutes
Requires core level: 2
''')
    elif userInput == 'BcoinMine 3':
        print('''Showing statistics for BcoinMine level 3:
Firewall: 185
Production speed (Hourly): 32B
Production limit (Total): 72B
Exfiltration (Transfer) per second: 2B
Construction cost: $1,000
Completion time (1 building thread): 1 Hour
Requires core level: 2
''')
    elif userInput == 'BcoinMine 4':
        print('''Showing statistics for BcoinMine level 4:
Firewall: 205
Production speed (Hourly): 42B
Production limit (Total): 192B
Exfiltration (Transfer) per second: 3B
Construction cost: $2,000
Completion time (1 building thread): 4 Hours
Requires core level: 2
''')
    elif userInput == 'BcoinMine 5':
        print('''Showing statistics for BcoinMine level 5:
Firewall: 230
Production speed (Hourly): 52B
Production limit (Total): 252B
Exfiltration (Transfer) per second: 4B
Construction cost: $4,000
Completion time (1 building thread): 6 Hours
Requires core level: 2
''')
    elif userInput == 'BcoinMine 6':
        print('''Showing statistics for BcoinMine level 6:
Firewall: 255
Production speed (Hourly): 64B
Production limit (Total): 384B
Exfiltration (Transfer) per second: 5B
Construction cost: $8,000
Completion time (1 building thread): 12 Hours
Requires core level: 3
''')
    elif userInput == 'BcoinMine 7':
        print('''Showing statistics for BcoinMine level 7:
Firewall: 280
Production speed (Hourly): 76B
Production limit (Total): 912B
Exfiltration (Transfer) per second: 11B
Construction cost: $16,000
Completion time (1 building thread): 16 Hours
Requires core level: 3
''')
    elif userInput == 'BcoinMine 8':
        print('''Showing statistics for BcoinMine level 8:
Firewall: 310
Production speed (Hourly): 88B
Production limit (Total): 1,056B
Exfiltration (Transfer) per second: 12B
Construction cost: $32,000
Completion time (1 building thread): 24 Hours
Requires core level: 4
''')
    elif userInput == 'BcoinMine 9':
        print('''Showing statistics for BcoinMine level 9:
Firewall: 345
Production speed (Hourly): 105B
Production limit (Total): 1,260B
Exfiltration (Transfer) per second: 14B
Construction cost: $64,000
Completion time (1 building thread): 30 Hours
Requires core level: 4
''')
    elif userInput == 'BcoinMine 10':
        print('''Showing statistics for BcoinMine level 10:
Firewall: 385
Production speed (Hourly): 120B
Production limit (Total): 1,440B
Exfiltration (Transfer) per second: 15B
Construction cost: $128,000
Completion time (1 building thread): 36 Hours
Requires core level: 5
''')
    elif userInput == 'BcoinMine 11':
        print('''Showing statistics for BcoinMine level 11:
Firewall: 425
Production speed (Hourly): 130B
Production limit (Total): 3,120B
Exfiltration (Transfer) per second: 31B
Construction cost: $200,000
Completion time (1 building thread): 42 Hours
Requires core level: 5
''')
    elif userInput == 'BcoinMine 12':
        print('''Showing statistics for BcoinMine level 12:
Firewall: 470
Production speed (Hourly): 150B
Production limit (Total): 3,600B
Exfiltration (Transfer) per second: 34B
Construction cost: $250,000
Completion time (1 building thread): 48 Hours
Requires core level: 6
''')
    elif userInput == 'BcoinMine 13':
        print('''Showing statistics for BcoinMine level 13:
Firewall: 525
Production speed (Hourly): 180B
Production limit (Total): 4,320B
Exfiltration (Transfer) per second: 39B
Construction cost: $300,000
Completion time (1 building thread): 60 Hours
Requires core level: 6
''')
    elif userInput == 'BcoinMine 14':
        print('''Showing statistics for BcoinMine level 14:
Firewall: 580
Production speed (Hourly): 210B
Production limit (Total): 5,040B
Exfiltration (Transfer) per second: 43B
Construction cost: $400,000
Completion time (1 building thread): 72 Hours
Requires core level: 7
''')
    elif userInput == 'BcoinMine 15':
        print('''Showing statistics for BcoinMine level 15:
Firewall: 645
Production speed (Hourly): 250B
Production limit (Total): 8,000B
Exfiltration (Transfer) per second: 64B
Construction cost: $500,000
Completion time (1 building thread): 92 Hours
Requires core level: 7
''')
    elif userInput == 'BcoinMine 16':
        print('''Showing statistics for BcoinMine level 16:
Firewall: 720
Production speed (Hourly): 300B
Production limit (Total): 9,600B
Exfiltration (Transfer) per second: 72B
Construction cost: $550,000
Completion time (1 building thread): 96 Hours
Requires core level: 8
''')
    elif userInput == 'BcoinMine 17':
        print('''Showing statistics for BcoinMine level 17:
Firewall: 780
Production speed (Hourly): 350B
Production limit (Total): 11,200B
Exfiltration (Transfer) per second: 80B
Construction cost: $600,000
Completion time (1 building thread): 104 Hours
Requires core level: 8
''')
    elif userInput == 'BcoinMine 18':
        print('''Showing statistics for BcoinMine level 18:
Firewall: 885
Production speed (Hourly): 450B
Production limit (Total): 14,500B
Exfiltration (Transfer) per second: 98B
Construction cost: $700,000
Completion time (1 building thread): 112 Hours
Requires core level: 9
''')
    elif userInput == 'BcoinMine 19':
        print('''Showing statistics for BcoinMine level 19:
Firewall: 980
Production speed (Hourly): 550B
Production limit (Total): 22,000B
Exfiltration (Transfer) per second: 141B
Construction cost: $800,000
Completion time (1 building thread): 120 Hours
Requires core level: 9
''')
    elif userInput == 'BcoinMine 20':
        print('''Showing statistics for BcoinMine level 20:
Firewall: 1,090
Production speed (Hourly): 650B
Production limit (Total): 26,000B
Exfiltration (Transfer) per second: 157B
Construction cost: $900,000
Completion time (1 building thread): 128 Hours
Requires core level: 9
''')
    elif userInput == 'BcoinMine 21':
        print('''Showing statistics for BcoinMine level 21:
Firewall: 1,210
Production speed (Hourly): 800B
Production limit (Total): 38,400B
Exfiltration (Transfer) per second: 220B
Construction cost: $1,000,000
Completion time (1 building thread): 136 Hours
Requires core level: 9
''')

#this doesn't work for some reason... lol
else:
    print('''The command you entered does not exist.
''')
