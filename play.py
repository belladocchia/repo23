import time

def introduction():
    print("Welcome to this silly thing!")
    time.sleep(1)
    name = input("What's your name, mah dude? ")
    print("Hi, " + name + "!")
    time.sleep(1)
    print("You are standing in a cursed forest.")
    time.sleep(1)
    print("There are two paths in front of you.")
    time.sleep(1)

def choose_path(name):
    print("Which path will you choose?")
    time.sleep(1)
    print("1. The safe, boring path")
    print("2. The fun, dangerous path")

    choose_path = input("Enter 1 or 2 to make your choice: ")
    if choose_path == "1":
        print("You (boring) walk down the safe path.")
        time.sleep(1)
        print("You come across a river.")
        time.sleep(1)
        swim = input("Do you swim across the river? (yes/no) ")
        if swim == "yes":
            print("Well that's it because you're boring.")
            time.sleep(1)
        else:
            print("You decide not to swim across the river and turn back, as expected.")
            time.sleep(1)
    elif choose_path == "2":
        print("You skip merrily down the fun path, because you're cool.")
        time.sleep(1)
        print("You come across a clearing (What?! Fricken sick, bro.)")
        time.sleep(1)
        print("In the clearing, you find a treasure chest. (Dope!)")
        time.sleep(1)
        open_chest = input("Do you open the chest? (yes/no) ")
        if open_chest == "yes":
            print("You open the chest and find a mirror that shows you the raddest dude!")
            time.sleep(1)
        else:
            print("Maybe you should have picked the boring path, bro.")
            time.sleep(1)
            
def conclusion(name):
    print("Okay, buddy! You're done here.")
    time.sleep(5)

if __name__ == "__main__":
    name = introduction()
    choose_path(name)
    conclusion(name)
    exit()