import time
import random

def print_pause(string):
    print(string)
    time.sleep(0.25)

def intro():
    print_pause("Humanity as it was once has ceased to exist.")
    print_pause("You are a robot and have just arrived at your new assignment for the human processing plant.")
    print_pause("You make your way directly to the elevator.")

intro()

# def valid_input(prompt, options):
#     while True:
#         response = input(prompt).lower()
#         for option in options:
#             if option in response:
#                 return response
#         print_pause("An integer plz :)")

while True:
    print_pause("")
    print_pause("1. Lobby\n" 
                "2. Engineering\n" 
                "3. Robot Resources\n")
    floor = input("Please enter the number for the floor you would like to visit:\n")
    if "1" == floor:
        print_pause("The door closes and then opens, and you realize...")
        time.sleep(random.randrange(4))
        print_pause("You already are in the lobby.\n")
    elif "2" == floor:
        print_pause("After a moment, you find yourself in the Robot Resources department")
    elif "3" == floor:
        print_pause("After a few moments, you find yourself in the Engineering department.")
    print_pause("But, this is not the right floor for you. Please choose another floor.")