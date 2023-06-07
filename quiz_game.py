# Followed 5 Mini Python Projects - For Beginners: https://youtu.be/DLn3jOsNRVE by Tech With Tim: https://www.youtube.com/@TechWithTim

print()
print("Welcome to my quiz! Khehehe...")

playing = input("Do you want to continue? (y/n): ")
if playing.lower() == 'y':
    print("Kehe...")
    print("じゃあ...")
elif playing.lower() == 'n':
    print("女々しい")
    quit()
else:
    print("Invalid input.")

score = 0

answer = input("What are you? ")
if answer == "1": # "A Sy S TOY FOR EVERYONE TO USE FOR FREE!!":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What do you love? ")
if answer == "1": # "PAINFUL a FROM ANYONE FOR FREE!!":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is your job? ")
if answer == "1": # "MY JOB IS TO SUBMISSIVELY FOLLOW ORDERS!!":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What's 100 + 19999938: ")
if answer == "1": # "20000038":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Bark ")
if answer == "1": # "ARF!!":
    print("Good girl")
    score += 1
else:
    print("Bad girl")
    print("You're gonna need more obedience training :))")

print("Score: " + str(score))
if score <= 0:
    print("OOh, you've been a REALLY bad girrll :))")
    print("For every answer you got wrong, slap your a 10 times as hard as you can :))")
elif score <= 3:
    print("You got a lot wrong...")
    print("For every answer you got wrong, slap your a 10 times as hard as you can :))")
elif score == 4:
    print(":/")
    print("Not good enough...")
    print("Slap your b's 10 times as hard as you can :))")
elif score >= 5:
    print(":)")
    print("Looks like you got them all right :)")
    print("So...")
    print("Let's test if you actual follow it in practice :)))")
    print("...")
    print("F your bussy then deepthroat your f :)")

print("You got " + str((score/5) * 100) + "%")