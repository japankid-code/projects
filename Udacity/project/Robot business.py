# this is a refactor of elevator2.py
# various pieces of code were moved into functions instead of while loops.
# everything after ride_elevator function definition was written by me exclusively.
# items list moved into a function definition, 
# this means the list has to be called as a parameter in earlier function definitions.
# 

import time
import random

def print_pause(string):
    time.sleep(0.35)
    print(string)    

def dotdotdot(n):
    for wait in range(n):
        print_pause("...")

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
    time.sleep(random.randrange(8))
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
    print_pause("Ahead, there is a door. It is locked and you must use your ID chip to get through.")
    if "ID card" in items:
        print_pause("You scan your ID chip and make your way through the door.")
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

def science_room(items: list):
    print_pause("You have made it to the science room.")
    print_pause("This is where research is done to see how humans can benefit robots.")
    print_pause("Unfortunately, a sealed hatch is in your way and it is rusted shut.")
    # you will need the power bands to be able to fix the problem in this room
    if power not in items:
        print_pause("You would think a facility with a science room would be kept in top shape.")
        print_pause("But not this one.")
        dotdotdot(3)
        print_pause("You make your way out of the science room.")
    elif power in items:
        print_pause("Your power upgrade allows you to force open the rusted hatch")
        if power_level >= 0 and power_level <= 6: # power off
            print_pause("Someone forgot to turn on the lights this morning.")
            print_pause("You flip the switch next to the hatch.")
            print_pause("Nothing happens.")
            print_pause("It seems that the power is out, you will have to investigate.")
        if power_level >= 7 and power_level <= 10: # power on
            print_pause("")

    pick_room(items)

def generator_room(items: list):
    print_pause("You make your way to the generator room.")
    print_pause("Inside you connect to the central generator monitoring system.")
    print_pause("Please select a room to adjust power:\n"
                "1. Science Room.\n"
                "2. Machine Room.")
    print_pause("===ERROR 42 - UNABLE TO LOAD PROTOCOL===")
    print_pause("The power level input protocol has malfunctioned.")
    print_pause("As a result, both rooms will have their power level set from 1-10.")
    power_level = random.randint(1, 10)
    print_pause("Power level has been set to:")
    print_pause(power_level)
    print_pause("You make your way out of the generator room.")
    power_level
    pick_room(items)

def machine_room(items: list):
    print_pause("You have made it to the machine room.")
    dotdotdot(3)
    # you will need the squirt gun to put out the fire in this room after turning the power on.
    if "power" in items:
         print_pause("Your power upgrade")
    print_pause("You make your way out of the machine room.")
    pick_room(items)

def upgrades(n):
    n = int(input("Please choose an upgrade:\n"))
    if n == 1:
        print_pause("Unfortunately, the wrench is out of stock at the moment.")
    if n == 2:
        items.append("power")
    if n == 3:
        items.append("squirt_gun")

def tool_room(items: list):
    print_pause("You have made it to the tool room.")
    print_pause("There is a large vending machine with all kinds of upgrades.")
    if power_level >= 0 and power_level <= 6: # power off.
        print_pause("Unfortunately, it seems the machine is out of order")
        print_pause("A small, dim, flashing screen shows low energy levels for the device.")
        print_pause("In order to function, power level must be increased.")
        print_pause("""
     ___________________
    |  |+==============+| 
    |  ||              ||
    |oo||    power     ||
    |oo||   shortage   ||
    |oo||              ||
    |oo||              ||
    |oo|+==============+|
    |  || |==========| ||
    |  || |==========| ||
    |--|----------------|
    """)
    elif power_level >= 7 and power_level <= 10: # power on.
        print_pause('''
     ___________________
    |  |+==============+|
    |  ||              ||
    |oo|| 1 wrench     ||
    |oo|| 2 power fist ||
    |oo|| 3 squirter   ||
    |oo||              ||
    |  |+==============+|
    |  || |==========| ||
    |  || |==========| ||
    |__|----------------|
    ''')
        print_pause("You interface with the machine and realize it is trying to tell you something...")
        print_pause("The little guy would like to thank you for turning the power back on!")
        print_pause("You are granted one free upgrade! here are your options:")
        print_pause("1. Wrench attachment, quite handy.\n"
                    "2. Power adapter, for robot stuff.\n" 
                    "3. Squirt gun, all kinds of uses.")
        upgrades(first)
        if assistant in items:
            print_pause("Your assistant status entitles you to some credit toward an item as well.")
            upgrades(second)
        
        # first_upgrade = input("Please choose an upgrade:\n")
        # if first_upgrade == "1":
        #     items.append("wrench")
        # if first_upgrade == "2":
        #     items.append("power")
        # if first_upgrade == "3":
        #     items.append("squirt_gun")
        # if "assistant" in items:
        #     print_pause("Your assistant status entitles you to some credit toward an item.")
        #     second_upgrade = input("Please choose an upgrade:\n")
        #     if first_upgrade == "1":
        #         items.append("wrench")
        #     if first_upgrade == "2":
        #         items.append("power")
        #     if first_upgrade == "3":
        #         items.append("squirt_gun")
        #     if "administrator" in items:
        #         second_upgrade = 
            
    print(items)
    print_pause("You make your way out of the tool room.")
    pick_room(items)

def pick_room(items: list):
    def room_chooser(items: list):
        if room_choice == "1":
            science_room(items)
        elif room_choice == "2":
            generator_room(items)
        elif room_choice == "3":
            machine_room(items)
        elif room_choice == "4":
            tool_room(items)
        else:
            print_pause("INVALID INPUT PLEASE TRY AGAIN")
    print_pause("Your memory loads the map, circuits compute your options...")
    print_pause("1. Science Room")
    print_pause("2. Generator Room")
    print_pause("3. Machine Room")
    print_pause("4. Tool Room")
    room_choice = input("Please enter a number from 1-4, or ??? if unsure:\n")
    while room_choice == "???":
        room_choice = random.randint(1, 4)
        room_chooser(items)
    room_chooser(items)   

def part_two(items: list):
    # choice = input("would you like to continue playing? (y/n):\n")
    #if choice == "y":
    print_pause("Finally, your first day at your new job can begin.")
    print_pause("You make your way out of the front recieving area into a long hallway.")
    print_pause("You observe in the dimly lit corridor that there is a map on the wall.")
    print_pause("You study the map, your sensors memorizing the options.")
    print_pause("You turn to continue down the hallway.")
    pick_room(items)
    # elif choice == "n":
    #     print_pause("Program terminated.")
    #     exit()
    # else:
    #     print_pause("I did not understand, please re-enter response:\n")
    #     part_two(items)

def play_game():
    items = []
    intro()
    ride_elevator(items)
    part_two(items)

def shortcut():
    global power_level
    power_level = 0
    items = ["handbook", "ID chip", "assistant"]
    part_two(items)

shortcut()
