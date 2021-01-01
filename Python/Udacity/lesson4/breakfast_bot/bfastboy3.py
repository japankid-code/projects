import time

def print_pause(string):
    print(string)
    time.sleep(1)

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("Sorry, I don't understand.")

def get_order():
    response = valid_input("Please place your order.\n Would you like waffles or pancakes?\n", 
                          ["waffles", "pancakes"])
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    
def order_again():
    order_again = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                             ["yes", "no"])
    if "no" in order_again:
        print_pause("OK, goodbye!")
        raise SystemExit
    elif "yes" in order_again:
        print_pause("Very good, I'm happy to take another order.")
intro()
while True:
    get_order()    
    print_pause("Your order will be ready shortly.")
    order_again()