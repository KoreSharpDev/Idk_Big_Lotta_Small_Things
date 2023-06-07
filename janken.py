# Followed 5 Mini Python Projects - For Beginners: https://youtu.be/DLn3jOsNRVE by Tech With Tim: https://www.youtube.com/@TechWithTim
# There is no draw option :(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
# And I'm too lazy to add it :))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

import random

user_wins = 0
comp_wins = 0

options = ["paper", "rock", "scissors"]

# options[int]

while True:
    user_input = input("Type Paper/Rock/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # 0 = paper
    # 1 = rock
    # 2 = scissors
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You winned!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You winned!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You winned!")
        user_wins += 1
        continue

    else:
        print("You losed :(")
        comp_wins += 1

print("You won", user_wins, "times.")
print("The computer won", comp_wins, "times.")
print("FUCK YOU!!")

