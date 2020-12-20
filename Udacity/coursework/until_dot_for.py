def until_dot_for(s):
    for index in range(len(s)):
        if s[index] == '.':
            return s[:index]
    return s

until_dot_for("This is a sentence. This is another.")