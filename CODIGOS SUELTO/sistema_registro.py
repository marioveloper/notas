try:
    name = input()

    if len(name) < 4:
        raise NameError
except:
    print('invalid name')
else:
    print('Account Created')