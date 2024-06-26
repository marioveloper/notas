def concatenate(*args):
    string = ''
    for i in args:
        string += i + '+'
    string = string[:-1]
    return string

print(concatenate('I', 'love', 'Python', '!'))