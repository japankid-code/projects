import time
import random
items = []

def print_pause(string):
    time.sleep(0.5)
    print(string)
    

def intro():
    print_pause("Humanity as it was once has ceased to exist.")
    print_pause("You are a robot and have just arrived to start your new assignment at the human processing plant.")
    print_pause("You make your way directly to the elevator and find several buttons.")

intro()

while True:
    print_pause("Here are your options:")
    print_pause("1. Lobby")
    print_pause("2. Robot Resources")
    print_pause("3. Engineering")
    floor = input("Please enter the number for the floor you would like to visit:\n")
    if floor == "1":
        print_pause("The door closes and then opens. Your circuitry computes...")
        time.sleep(random.randrange(4))
        print_pause("You are now in the lobby.\n...")
        if "ID card" in items:
            print_pause("The clerk greets you, but she has already given you your \n"
                        "ID chip, so there is nothing more to do here now.")
        if "ID card" not in items:
            print_pause("The clerk greets you and gives you your ID chip.")
            items.append("ID card")
    elif floor == "2":
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
    elif floor == "3":
        print_pause("After a few moments, you find yourself in the Engineering department.")
        print_pause("Ahead, there is a door. It is locked and you must use your ID chip to get through")
        if "ID card" in items:
            print_pause("You scan your ID chip to get through the door.")
            print_pause("Your program manager greets you, beginning to scan your circuitry.\n"
                        "He explains that you need to have a copy of the employee\n"
                        "handbook in order to start work.")
            if "handbook" in items:
                print_pause("Fortunately, you recieved this from the Robot Resources department!")
                print_pause("Congration! You are ready to start your new job as")
                print_pause("the assistant to the vice president of Engineering!")
                exit()
        else:
            print_pause("Unfortunately, the door is locked and you can't get in. ")
            print_pause("It looks like you need some kind of key card to open the door. ")
            print_pause("You head back to the elevator.")



    print_pause("You know what you need to do. Please choose another floor.")