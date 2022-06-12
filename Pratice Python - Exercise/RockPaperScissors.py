import random

play = True
replay = 'no'
print("----GAME RULES----")
print(
    """ 
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
    """
)
print("-----------")
while play:
    user_input = str(input("Enter rock or paper or scissor : ")).lower()
    items = ['rock', 'paper', 'scissor']
    computer_input = items[random.randint(0, 2)]
    print('USER VALUE : %s, COMPUTER VALUE : %s' % (user_input, computer_input))
    if user_input == items[0] and computer_input == items[2]:
        print('User wins!')
    elif user_input == items[2] and computer_input == items[1]:
        print('User wins!')
    elif user_input == items[1] and computer_input == items[0]:
        print('User wins!')
    elif user_input == computer_input:
        print("Match Draw")
    else:
        print('Computer wins')
    replay = input("Want to play one more game? (yes/no): ")
    if replay == 'yes':
        continue
    print("GAME END!!!")
    break
