import os
money = 60
command = ''
MenuList = ['MOONS', 'STORE', 'BESTIARY', 'STORAGE', 'OTHER']
OtherList = ['VIEW MONITOR', 'SWITCH']

from datetime import datetime

current_day_of_week = datetime.now().strftime("%A")

def clear_terminal():
    os.system('cls')
    print()

def SimplePage(text):
    clear_terminal()
    print(f'>{money} Coins')
    print()
    print('-----------------------------')
    print()
    print(text)
    print()
    CommandCheck()

def CommandCheck():
    command = input()
    if command in MenuList:
        if command == 'MOONS':
            MoonsPage()
            return
        if command == 'STORE':
            StorePage()
            return
        if command == 'BESTIARY':
            BestiaryPage()
            return
        if command == 'STORAGE':
            StoragePage()
            return
        if command == 'OTHER':
            OtherPage()
            return
    elif command in OtherList:
        words = command.split()
        if command == "VIEW MONITOR":
            SimplePage('Toggling radar cam')
            return
        elif words[0] == 'SWITCH' and not command == 'SWITCH':
            SimplePage('[There was no object supplied with the action, or your word was typed incorrectly or does not exist.]')
            return
        elif command.startswith('SWITCH'):
            SimplePage('Switching player view')
            return
        


def OtherPage():
    clear_terminal()
    print(f'>{money} Coins')
    print()
    print('-----------------------------')
    print()
    print('Other commands:')
    print()
    print(">VIEW MONITOR \nTo toggle on AND off the main monitor's map cam")
    print()
    print('>SWITCH [Player name] \nTo switch view to a player on the main monitor.')
    print()
    print('PING [Radar booster name] \nTo make a radar booster make a noise.')
    print()
    print('>SCAN \nTo scan for the number of items left of the current planet.')
    print('\n')
    CommandCheck()

def StoragePage():
    clear_terminal()
    print(f'>{money} Coins')
    print()
    print('-----------------------------')
    print()
    print('While moving furniture with [B], you can press [X] to send it to storage. You can call it back from storage here.')
    print()
    print('These are the items in storage:')
    print()
    print('[No items stored. While moving an object with B, press X to store it.]')
    CommandCheck()

def BestiaryPage():
    clear_terminal()
    print(f'>{money} Coins')
    print()
    print('-----------------------------')
    print()
    print('Bestiary')
    print()
    print('To access a creature file, type "INFO" after its name.')
    print('-----------------------------')
    print()
    print('No data colllected on wildlife. Scans are required.')
    CommandCheck()

def StorePage():
    clear_terminal()
    print(f'>{money} Coins')
    print()
    print('-----------------------------')
    print()
    print('Welcome to the Company store. \nUse words BUY and INFO on any item. \nOrder tools in bulk by typing a number.')
    print()
    print('-----------------------------')
    print()
    print('*Walkie-talkie   //   Price: 12 Coins')
    print('* Flashlight   //   Price: 15 Coins')
    print('* Shovel   //   Price: 30 Coins')
    print('* Lockpicker   //   Price: 20 Coins')
    print('* Pro-flashlight   //   Price: 25 Coins')
    print('* Stun grenade   //   Price: 40 Coins')
    print('* Boombox   //   Price: 60 Coins')
    print('* TZP-Inhalant   //   Price: 120 Coins')
    print('* Zap gun   //   Price: 400 Coins')
    print('* Jetpack   //   Price: 700 Coins')
    print('* Extension ladder   //   Price: 60 Coins')
    print('* Radar-booster   //   Price: 50 Coins')
    print()
    print('SHIP UPGRADES:')
    print('* Loud horn   //   Price: 150 Coins')
    print('* Teleporter   //   Price: 375 Coins')
    print('* Inverse Teleporter   //   Price: 425 Coins')
    print()
    print('The selection of ship decor rotates per-quota. Be sure to check back next week:')
    print('-----------------------------')
    print('Romantic table   //   120 Coins')
    print('Pajama suit   //   900 Coins')
    print('Television   //   130 Coins')
    print('Shower   //   180 Coins')
    print('Cozy lights   //   140 Coins')
    CommandCheck()

def MoonsPage():
    clear_terminal()
    print(f'>{money} Coins')
    print()
    print('-----------------------------')
    print()
    print('Welcome to the exomoons catalougue. \nTo route the autopilot to a moon, use the word ROUTE. \nTo learn about any moon, use the word INFO.')
    print()
    print('-----------------------------')
    print()
    print('* The Company Building   //   Buying at 30%')
    print()
    print('* Experimentation')
    print('* Assurance  (Rainy)')
    print('* Vow')
    print()
    print('* Offense  (Flooded)')
    print('* March  (Flooded)')
    print()
    print('* Rend  (Eclipsed)')
    print('* Dine  (Eclipsed)')
    print('* Titan  (Foggy)')
    CommandCheck()

def MainMenu():
    clear_terminal()
    print(f'>{money} Coins')
    print()
    print('-----------------------------')
    print()
    print('>MOONS \nTo see the lists of moons the autopilot can route to.')
    print()
    print(">STORE \nTo see the company store's selection of useful items.")
    print()
    print('>BESTIARY \nTo see the list of wildlife on record.')
    print()
    print('>STORAGE \nTo access objects placed into storage.')
    print()
    print('>OTHER \nTo see the other list of commands.')
    print('\n')
    CommandCheck()

clear_terminal()
print(f'>{money} Coins')
print()
print('-----------------------------')
print()
print('Welcome to the FORTUNE-9 OS \n           Courtesy of the Company')
print()
print(f'Happy {current_day_of_week}.')
print()
print('Type "Help" for a list of commands.')
print('\n\n\n')
CommandCheck()