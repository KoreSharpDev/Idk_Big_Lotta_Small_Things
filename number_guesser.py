# Followed 5 Mini Python Projects - For Beginners: https://youtu.be/DLn3jOsNRVE by Tech With Tim: https://www.youtube.com/@TechWithTim

import random

min = 0
max = input("Max number: ")

Correct = False
while not Correct:
    if max.isdigit():
        max = int(max)
        if max <= 0:
            print("[ERROR: JKDCHB-349865462781245671246956] Please input a number larger than 0 next time.")
            Correct = False
            max = input("Max number: ")
        else:
            Correct = True
    else:
        print("[ERROR: CCEJSY-43934164213567546542754254] Please input a number next time.")
        Correct = False
        max = input("Max number: ")


random_number = (random.randint(int(min), int(max)))
print(random_number)
guesses = 1

while True:
    user_guess = input("Guess the number between " + str(min) + " and " + str(max) + ": ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("[ERROR: DH-4836476372846748756437678542357857546754874547564754735347865437864357865438654376324965976342976549623963549786354789#%#$!^@#$%$#^%$$!^%$%^$%^$#%$!@%^$%@!$%!#$%^&@$&@$#%^$#@%^&$@!%^$@%^$!@%^&$#@!%^$%^#$@^%$^&%$^#&%$^#@!$^@$*#%^@!54*@$] Please type a number next time :)")
        continue

    if user_guess == random_number:
        if guesses <= 1:
            print("RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! RIGGED!!! ")
        if guesses > 1:
            print("IT TOOK " + str(guesses) + " GUESSES!!!!")
            for i in range (guesses):
                print("L!!! ")
    else:
        guesses += 1
        print("WWRROOONG!!! KHAHAHAHAAHHAHAHAHHAHAHAAHHAHAHAHHAHAHAHAHAHAHHAHAHAHAHHAHAHAHAHHAHAHAHAHHAHAHAHHAHAHAHAHHAHAHAHAHHAHAHAHAHHHAHAHHAAHAAHAHHAHAHAHHHAAHHHAAAHHAAHAHHHAAHAHAHHAHAHAHAHHAHAHAHAHHAAAH")
        if user_guess < random_number:
            print("TRY GUESSING HIGHER NEXT TIME IDIOT!!!!!!! KAHHAHAHAHHAHAHAHAHHAA!!!!!!")
        if user_guess > random_number:
            print("TRY GUESSING LOWER NEXT TIME IDIOT!!!!!!! KAHHAHAHAHHAHAHAHAHHAA!!!!!!")