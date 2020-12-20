def until_dot_while(string):
    index = 0
    while index < len(string) and string[index] != ".":
        index += 1
    print(string[:index])

until_dot_while("This is a sentence. This is another.")