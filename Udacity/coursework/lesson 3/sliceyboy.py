def word_triangle(word):
    length = len(word)
    for n in range(length): # prints out a right side up triangle
        print(word[:n + 1])
    for n in range(length): # prints out an upside down triangle.
        print(word[:length - n])
    for n in range(length): # prints out a column with all the letties :)
        print(word[:n + 1], word[:length - n])

word_triangle(input("what word would u like to slice up??? "))