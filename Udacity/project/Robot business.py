# this is a refactor of elevator2.py
# various pieces of code were moved into functions instead of while loops.
# everything after ride_elevator function definition was written by me exclusively.
# items list moved into a function definition, 
# this means the list has to be called as a parameter in earlier function definitions.
# 

import time
import random

def print_pause(string):
    time.sleep(0.05)
    print(string)    

def intro():
    print_pause("Humanity as it was once has ceased to exist.")
    print_pause("You are a robot and have just arrived to start your new assignment at the human generator plant.")
    print_pause("You make your way directly to the elevator and find several buttons.")
    print_pause("Here are your options:")
    print_pause("1. Lobby")
    print_pause("2. Robot Resources")
    print_pause("3. Engineering")

def first_floor(items: list):
    print_pause("The door closes and then opens. Your circuitry computes...")
    time.sleep(random.randrange(4))
    print_pause("You are now in the lobby.\n...")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already given you your \n"
                    "ID chip, so there is nothing more to do here now.")
    if "ID card" not in items:
        print_pause("The clerk greets you and gives you your ID chip.")
        items.append("ID card")
    ride_elevator(items)

def second_floor(items: list):
    print_pause("After a moment, you find yourself in the Robot Resources department.")
    print_pause("The Administrator of the floor greets you.")
    if "handbook" in items:
        print_pause("But she has already given you your handbook.")
    else:
        if "ID card" not in items:
            print_pause("The administrator has something for you, but says she can't\n"
                    "give it to you until you go get your ID chip.")
        if "ID card" in items:
            print_pause("She looks at your ID chip.\n"
                        "She hands you a datachip containing the employee handbook.")
            items.append("handbook")
    ride_elevator(items)

def third_floor(items: list):
    print_pause("After a few moments, you find yourself in the Engineering department.")
    print_pause("Ahead, there is a door. It is locked and you must use your ID chip to get through")
    if "ID card" in items:
        print_pause("You scan your ID chip to get through the door.")
        print_pause("You make your way through to the front staging area.")
        print_pause("Your program manager greets you, beginning to scan your circuitry.\n"
                    "He explains that you need to have a copy of the employee\n"
                    "handbook in order to start work.")
        if "handbook" in items:
            print_pause("Fortunately, you recieved this from the Robot Resources department!")
            print_pause("Congration! You are ready to start your new job as")
            print_pause("the assistant to the vice president of Engineering!")
            items.append("assistant")
            part_two(items)
    else:
        print_pause("Unfortunately, the door is locked and you can't get in. ")
        print_pause("It looks like you need some kind of key card to open the door. ")
        print_pause("You head back to the elevator.")
    ride_elevator(items)

def ride_elevator(items: list):
    floor = input("Please enter the number for the floor you would like to visit:\n")
    if floor == "1":
        first_floor(items)
    elif floor == "2":
        second_floor(items)
    elif floor == "3":
        third_floor(items)
    print_pause("You know what you need to do. Please choose another floor.")

def growing_room(items: list):
    print_pause("You have made it to the growing room.")
    print_pause("This is where the humans are grown for use in energy production.")

    print_pause("You make your way out of the growing room.")
    pick_room(items)

def generator_room(items: list):
    print_pause("You make your way to the generator room.")
    print_pause("Inside you connect with the central generator monitoring system (CGMS).")
    room_choice = input("Please select a room to adjust power:\n"
                        "1. Growing Room.\n"
                        "2. Machine Room.\n")
    power_level = input("Please select a power level 1-10:")
    for p in range(10):
        if power_level == p:
            


    # power levels for the growing room and machine room can be set here.
    print_pause("You make your way out of the generator room.")
    pick_room(items)

def machine_room(items: list):
    print_pause("You have made it to the machine room.")
    #some upgrades will happen in this room, power coupler can be installed.
    if "medal" in items:
        # you turn the medal in for the power coupler.
    print_pause("You make your way out of the machine room.")
    pick_room(items)

def tool_room(items: list):
    print_pause("You have made it to the tool room.")
    print_pause("You make your way out of the tool room.")
    pick_room(items)

def pick_room(items: list):
    print_pause("You remember the map, circuits computing your options...")
    print_pause("1. Growing Room")
    print_pause("2. Generator Room")
    print_pause("3. Machine Room")
    print_pause("4. Tool Room")
    room_choice = input("Please enter a number from 1-4, or ??? if unsure:")
    while room_choice == "???":
        room_choice = random.randint(1, 4)
    if room_choice == "1":
        growing_room(items)
    elif room_choice == "2":
        machine_room(items)
    elif room_choice == "3":
        generator_room(items)
    elif room_choice == "4":
        tool_room(items)

def part_two(items: list):
    choice = input("would you like to continue playing? (y/n):\n")
    if choice == "y":
        print_pause("Finally, your first day at your new job can begin.")
        print_pause("You make your way out of the front staging area into a long hallway.")
        print_pause("There is a map on this wall.")
        print_pause("You study the map, your circuitry memorizing the options.")
        print_pause("You turn to continue down the hallway.")
        pick_room(items)
    elif choice == "n":
        print_pause("Program terminated.")
        exit()

def play_game():
    items = []
    intro()
    ride_elevator(items)
    part_two(items)

play_game()
