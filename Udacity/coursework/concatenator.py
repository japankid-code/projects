# def ly_ifier(w):
#     print(w + 'ly')

# ly_ifier("kittenish")

def part1():
    name = input("What's your name?\n\n")
    print("\nHi, " + name + "! It's very nice to meet you.\n")
    color = input("What is your favorite color?\n\n")
    print("\nAh, " + color + ", what a lovely color!")

# the second time here uses f strings
def part2():
    name = input("What's your name?\n\n")
    print(f"\nHi, {name}! It's very nice to meet you.\n")
    color = input("What is your favorite color?\n\n")
    print(f"\nAh, {color}, what a lovely color!")

part2()