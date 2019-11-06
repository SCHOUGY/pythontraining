def check_if_repeat(string):
    index = []
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
            index.append(char)
    for char in index:
        if dict[char] == 1:
            return char
    return None


char = check_if_repeat(input("I will find the first non-repeating character, give me input: "))
print(char)
