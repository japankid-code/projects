def is_substring(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            return True
        index += 1
    return False

print(is_substring('bad', 'abracadabra')) # return False
print(is_substring('dab', 'abracadabra')) # return True

def count_substring(string, substring):
    index = 0
    total = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            total += 1
            index += len(substring)
        else:
            index += 1
    return total

print(count_substring('love, love, love, all you need is love', 'love')) # prints 4
print(count_substring('AAAA', 'AA')) # prints 2


def locate_first(string, target):
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            return index
        else:
            index += 1
    return -1

print(locate_first('cookbook', 'ook')) # returns 1
print(locate_first('all your bass are belong to us', 'base')) # returns -1

def locate_all(string, target):
    index = 0
    matches = []
    while index < len(string):
        if string[index : index + len(target)] == target:
            matches.append(index)
            index += len(target)
        else:
            index += 1
    return matches

print(locate_all('cookbook', 'ook')) # returns list [1, 5]
print(locate_all('all your base are belong to us, base', 'base')) # returns list [9, 32]

# these search functions are already built into python
# 'in' and 'not in' for is_substring
1 in [1, 2, 3] # returns true
[1, 2] not in [1, 2, 3] # returns true
[1, 3] in [1, 2, 3] # returns false
[1, 3] in [1, 2, 3, [1, 3]] # returns true
# for locate_first, we use method find, as in:
'abracadabra'.find('cad')
# to count all occurrences, use method count, as in:

