# s = "Tenochtitlan"
# index = 0 
# while index < len(s):
#     index += 1 
#     print(s[:index])

# s = "abracadabra"
# index = len(s)
# while index > 0:
#     print(s[:index])
#     index -= 1


def until_dot_for(s):
    for index in range(len(s)):
        if s[index] == '.':
            return s[:index]
    return s

until_dot_for("This is a sentence. This is another.")

def until_dot_while(string):
    index2 = 0
    while index2 < len(string) and string[index2] != ".":
        index2 += 1
    print(string[:index2])

until_dot_while("This is a sentence. This is another.")