# s = "Karl"

# def start_K(s):
#     return s[0] == "K"

# print(start_K(s))

# for n in range(0, 10, 2):
#     print(n)

# word = "dog"
# for n in range(10):
#   print(word[n])
# the line print(word[n]) uses indexing to print the characters,
# this can be avoided by changing the loop to ```for n in range(len(word))
#                                                    print(n)```
# thereby eliminating the need to use indexing to print the letters

word = "definitely"
length = len(word)

word[:length]
word[:length - 2]
word[length - 8:]
word[length -8:length - 2]