import time

def print_pause(string):
    print(string)
    time.sleep(0.25)

def intro():
    print_pause("Humanity as it was once has ceased to exist.")
    print_pause("You are a robot and have just arrived at your new assignment for the human processing plant.")
    print_pause("You make your way directly to the elevator.")

def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("An integer plz :)")

def choose_floor():
    response = valid_input("Please enter the number for the floor you would like to visit: \n", 
                          ["1. Lobby", "2. Engineering", "3. Robo Resources"])
    if 1 in response:
        print_pause("After a few moments, you realize that nothing happened \n")
        print_pause("and you were already in the lobby.")
    elif 2 in response:
        print_pause("After a moments, you find yourself in the Robo Resources department")
    elif 3 in response:
        print_pause("After a few moments, you find yourself in the Engineering department.")
    print_pause("But, this is not the right floor for you.")

def elevator():
    intro()
    choose_floor()

elevator()