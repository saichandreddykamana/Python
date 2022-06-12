import random

password_length = input("Enter password length (Min-length = 5): ")
password_strength = input("Enter strength of the password (1 - only characters, 2 - only characters and "
                          "numbers, 3 - characters, numbers and symbols) :")

numbers = list('0123456789')
random.shuffle(numbers)
symbols = list('~!@#$%^&*()_+=-}]{[;:></?')
random.shuffle(symbols)
characters = list('aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ')
random.shuffle(characters)
password = ''
i = 0
while i <= int(password_length):
    if int(password_strength) == 2:
        characters = characters + numbers
    if int(password_strength) == 3:
        characters = characters + numbers + symbols
    print(characters)
    length = len(characters)
    index = random.randint(0, length - 1)
    password += characters[index]
    i += 1
print('-------------------------------------------------------------')
print('Generated Password : ', password)
