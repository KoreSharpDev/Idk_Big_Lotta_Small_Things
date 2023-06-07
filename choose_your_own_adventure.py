# Followed 5 Mini Python Projects - For Beginners: https://youtu.be/DLn3jOsNRVE by Tech With Tim: https://www.youtube.com/@TechWithTim
# Idk if all the paths lead to the_end but eh, I'm too lazy
# Also you can judge me all you want, I don't care uwu
# I probably should've used more functions tbh
# It wouuld've made cencoring it easier -`o`-

def the_end(cod):
    print("You died of " + cod)
    print("Thend")
    exit()


namae = input("Enter your name: ")
print("Welcome", namae + ".")
print("Get ready for an adventure!!")
print()

print("You wake up in a janitor closet, you can go back to sleep, or search the room.")
option = ["sleep", "search"]
num_of_options = len(option)

i = 0
while i < num_of_options:
    print(option[i])
    i += 1
answer = input("What do you do? ")

if answer == option[0]:
    print("You sleep.")
    print("...")
    print()
    print("You wake up to getting r'd by a school girl with a MASSIVE c")
    option = ["fight", "accept"]
    i = 0
    while i < num_of_options:
        print(option[i])
        i += 1
    answer = input("What do you do? ")
    if answer == option[0]:
        print("You try to fight back but they are strong")
        print("Additionally, you just woke up and your pretty sweepy -_-")
        print("You recieve blunt force trauma after getting slammed into the brick wall and pass out")
        the_end("blood loss from injury from MASSIVE c")
    if answer == option[1]:
        print("You accept your fate and let her r you")
        print("You get slammed into a brick wall while she r's and insults you")
        print("You recieve blunt force trauma after getting slammed into the brick wall and pass out")
        the_end("blood loss from injury from MASSIVE c")

if answer == option[1]:
    print("You search the room.")
    print("There is a broom and an exit")
    option = ["pick up broom", "sleep", "e xit"]
    num_of_options = len(option)

    i = 0
    while i < num_of_options:
        print(option[i])
        i += 1
    answer = input("What do you do? ")
    if answer == option[0]:

        if answer == option[0]:
            print("You pick up the broom, it's heavy and you're quite weak")
            print("Picking up the broom makes you very tired")
            print("You sleep.")
            print("...")
            print()
            print("You wake up to getting r'd by a school girl with a MASSIVE c")
            option = ["fight", "accept"]
            num_of_options = len(option)
            i = 0
            while i < num_of_options:
                print(option[i])
                i += 1
            answer = input("What do you do? ")
            if answer == option[0]:
                print("You try to fight back but they are strong")
                print("Additionally, you just woke up and your pretty sweepy -_-")
                print("You recieve blunt force trauma after getting slammed into the brick wall and pass out")
                the_end("blood loss from injury from MASSIVE c")
            if answer == option[1]:
                print("You accept your fate and let her r you")
                print("You get slammed into a brick wall while she r's and insults you")
                print("You recieve blunt force trauma after getting slammed into the brick wall and pass out")
                the_end("blood loss from injury from MASSIVE c")
        if answer == option[1]:
            if answer == option[0]:
                print("You sleep.")
                print("...")
                print()
                print("You wake up to getting r'd by a school girl with a MASSIVE c")
                option = ["fight", "accept"]
                i = 0
                while i < num_of_options:
                    print(option[i])
                    i += 1
                answer = input("What do you do? ")
                if answer == option[0]:
                    print("You try to fight back but they are strong")
                    print("Additionally, you just woke up and your pretty sweepy -_-")
                    print("You recieve blunt force trauma after getting slammed into the brick wall and pass out")
                    the_end("blood loss from injury from MASSIVE c")
                if answer == option[1]:
                    print("You accept your fate and let her r you")
                    print("You get slammed into a brick wall while she r's and insults you")
                    print("You recieve blunt force trauma after getting slammed into the brick wall and pass out")
                    the_end("blood loss from injury from MASSIVE c")
        if answer == option[2]:
            print("You try to exit, but you use all of your energy trying to push the door open. It's not locked, your just tired and weak")
            print("You sleep.")
            print("...")
            print()
            print("You wake up to getting r'd by a school girl with a MASSIVE c")
            option = ["fight", "accept"]
            i = 0
            while i < num_of_options:
                print(option[i])
                i += 1
            answer = input("What do you do? ")
            if answer == option[0]:
                print("You try to fight back but they are strong")
                print("You recieve blunt force trauma after getting slammed into the brick wall and pass out")
                the_end("blood loss from injury from MASSIVE c")
            if answer == option[1]:
                print("You accept your fate and let her r you")
                print("You get slammed into a brick wall while she r's and insults you")
                print("You recieve blunt force trauma after getting slammed into the brick wall and pass out")
                the_end("blood loss from injury from MASSIVE c")