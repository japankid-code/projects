import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(0.5)
print("Today we have two breakfasts available.")
time.sleep(0.5)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(0.5)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(0.5)

while True:
    while True: # loops until pancakes or waffles is entered
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(0.5)
            break #this one only breaks out of the inner loop on line 13
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(0.5)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(0.5)
    print("Your order will be ready shortly.")
    time.sleep(0.5)
    while True: # We want to loop until they enter a valid response.
        order_again = input("Would you like to place another order? "
                                "Please say 'yes' or 'no'.\n").lower()
        if 'no' in order_again:
            print("OK, goodbye!")
            time.sleep(0.5)
            break # Note that this only breaks out of the inner loop.
        elif 'yes' in order_again:
            print("Very good, I am happy to take another order.")
            time.sleep(0.5)
        else:
            print("sorry, do not understand :(")
    if 'no' in order_again:
        break # last break needed to exit the outer loop, the first while loop