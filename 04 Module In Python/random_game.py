# cd "I:/Project Udemy/DataScience/The Complete Python Developer/04 Module In Python"
# python random_game.py 1 10
# write in terminal

import sys
from random import randint

if len(sys.argv) != 3:
    print("Please provide two numbers as arguments when running the script.")
    sys.exit()

try:
    lower_bound = int(sys.argv[1])
    upper_bound = int(sys.argv[2])
except ValueError:
    print("Both arguments must be numbers.")
    sys.exit()

random_number = randint(lower_bound, upper_bound)

while True:
    try:
        number = int(
            input(
                f"Please choose a number that falls between {lower_bound} and {upper_bound}: "
            )
        )
        if number < lower_bound or number > upper_bound:
            print(
                f"Your number must be between {lower_bound} and {upper_bound}. Please try again."
            )
            continue
        if number == random_number:
            print("You're a genius!")
            break
    except ValueError:
        print("Please enter a number")
