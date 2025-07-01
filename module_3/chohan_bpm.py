"""
Name: Brittaney Perry-Morgan
Date: Sunday, June 8th, 2025
Assignment: Module 3.2 Brownfield + Flowchart
Purpose: This program implements a modified version of the traditional Japanese dice game Cho-Han.
         Players bet on whether the sum of two dice will be even (CHO) or odd (HAN). The program
         includes a house fee, special bonuses, and user interface improvements.

Changes from chohan.py:
- Changed all user input prompts from '>' to 'bpm:' for both bet amount and CHO/HAN selection.
- Increased the house fee from 10% (pot // 10) to 12% (int(round(pot * 0.12))).
- Added a notice in the game introduction about a 10 mon bonus for rolling a total of 2 or 7.
- Implemented logic to award a 10 mon bonus and display a special message if the dice total is 2 or 7.
- Improved input validation and simplified logic for user choices.
- Refactored some code for clarity and Pythonic style (e.g., using 'in' for comparisons, simplified if/else).
- Updated documentation and comments to reflect all changes.
- Saved as chohan_bpm.py with your initials.

"""

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, adapted by BrP (brittaneyperry-morgan)

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

NOTICE: If you roll a total of 2 or 7, you get a 10 mon bonus!
''')

purse = 5000
while True:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('bpm: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('bpm: ').upper()
        if bet in ['CHO', 'HAN']:
            break

        else:
            print('Please enter either "CHO" or "HAN".')
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    if dice_total in [2, 7]:
        print(f'BONUS! The total of the roll was {dice_total}. You get a 10 mon bonus!')
        purse += 10

    rollIsEven = (dice_total) % 2 == 0
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        house_fee = int(round(pot * 0.12))
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot
        print('You lost!')

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
