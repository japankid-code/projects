# slicing never returns IndexError, a slice that tries to extract chars off the end
# of a string will instead just return what it can, even if that ends up being nothing.

word = "definitely"
length = len(word)

# print(word[:length])
# print(word[:length - 2])
# print(word[length - 8:])
# print(word[length -8:length - 2])

for n in range(length):
    print(n, word[0:n + 1])