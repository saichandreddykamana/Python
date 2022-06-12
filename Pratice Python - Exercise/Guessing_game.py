# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# Extras:
# -------
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

guess = 1
number = random.randint(1, 9)
play = True

while play:
    user_number = input('Enter number between 1 and 9 (including 1 and 9) and enter "quit" to exit game : ')
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number < 0 or user_number > 9:
            continue
        else:
            if user_number < number:
                guess += 1
                print('Guessed Too Low')
            elif user_number > number:
                guess += 1
                print('Guessed Too High')
            else:
                print('Guessed Exactly')
                print('Total Number of guesses : ', guess)
                while user_number != 'yes' and user_number != 'no':
                    user_number = input("Want to play again (yes/no)? ")
                if user_number.lower() == 'yes':
                    number = random.randint(1, 9)
                    guess = 0
                    continue
                play = False
    else:
        if user_number.lower() == 'quit':
            play = False
            print('Computer Guessed Number : ', number)
            print('Total Number of guesses : ', guess)
            print('Game Ends')
            continue
