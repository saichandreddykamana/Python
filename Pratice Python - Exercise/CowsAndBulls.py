import random


def diff_integers(num):
    num_str = {x for x in str(num)}
    if len(num_str) < 4:
        return diff_integers(random.randint(1000, 9999))
    return num


computer_num = diff_integers(random.randint(1000, 9999))
guess = 0
previous_guesses = set()
while True:
    cows = bulls = 0
    if len(previous_guesses) > 0 and guess != 1:
        print("List of previous guesses : ", previous_guesses)
    user_number = input("Enter 4-digit Number (Note : Number should not contain same digits): ")
    guess += 1
    previous_guesses.add(user_number)
    usr_str = {x for x in str(user_number)}
    if len(usr_str) == 4 and user_number.isdigit():
        if str(user_number) == str(computer_num):
            print("Well Done!! Right Answer")
            print("Total Number of guesses : ", guess)
            break
        else:
            answer = list('XXXX')
            for x in range(0, 4):
                user_str, computer_str = str(user_number), str(computer_num)
                if user_str[x] == computer_str[x]:
                    bulls += 1
                    answer[x] = user_str[x]
                if computer_str.count(user_str[x]) == 1 and computer_str[x] != user_str[x]:
                    cows += 1
            print("Bulls : " + str(bulls) + " , " + "Cows : " + str(cows))
            print("YOUR NUMBER : " + user_str + " UNLOCKED DIGIT : " + ''.join(answer))
