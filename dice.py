
from random import randint

def roll(units, sides, modifier):
    units = int(units)
    sides = int(sides)
    value = 0 + int(modifier)

    for n in range(units):
        roll = randint(1, sides)
        # print(f'Rolling {n} of {units}D{sides}: {roll}')
        value += roll
    return value

# - - - - String argument dice roller - - - - # 

# ''' 
# The purpose of this function is to allow the program to call dice.roll('1d6+1') to manage the rolls.
# Regular expression appear to reduce Quadratic Time Complexity for large or heavily populated sectors.
# Credit to Gareth Rees https://garethrees.org/ 
# '''

# import re

# def roll(dice):
    
#     """
#     Roll 6-side dice and return their sum. 
#     The argument must be a string
#     describing the roll, for example '2d6+3' to roll 
#     two 6-sided dice and add three.
#     """
    
#     match = re.match(r'([1-9]\d*)d([1-9]\d*)([+-]\d+)?$', dice)
    
#     if not match:
#         raise ValueError(f"Expected dice but got {dice!r}")
    
#     n, sides, bonus = match.groups()
#     sides = int(sides)

#     return sum(randint(1, sides) for _ in range(int(n))) + int(bonus or 0)
