import time
import random

def print_pause(string):
    time.sleep(1)
    print(string)
    

def intro():
    print_pause("Humanity as it was once has ceased to exist.")
    print_pause("You are a robot and have just arrived at your new assignment for the human processing plant.")
    print_pause("You make your way directly to the elevator and find several buttons.")
    print_pause("Here are your options:")
    print_pause("1. Lobby")
    print_pause("2. Engineering")
    print_pause("3. Robot Resources")

intro()

while True:
    floor = input("Please enter the number for the floor you would like to visit:\n")
    if floor == "1":
        print_pause("The door closes and then opens. Your circuitry computes...")
        time.sleep(random.randrange(4))
        print_pause("You have been in the lobby this whole time.\n...")
    if floor == "2":
        print_pause("After a moment, you find yourself in the Robot Resources department")
    if floor == "3":
        print_pause("After a few moments, you find yourself in the Engineering department.")
    print_pause("But, this is not the right floor for you. Please choose another floor.")