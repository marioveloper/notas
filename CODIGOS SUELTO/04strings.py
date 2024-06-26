myStr = "Hello World"

#print(dir(myStr))#todo lo q se puede hacer con el,

print(myStr.upper())
print(myStr.lower())
print(myStr.title())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'Bye').upper())
print(myStr.count('l'))
print(myStr.startswith('Hello'))
print(myStr.endswith('s'))
print(myStr.split())
print(myStr.split('o'))
print(myStr.find('W'))
print(len(myStr))
print(myStr.index('o'))
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[9])

print('un texto ' + myStr)
print(f'un texto {myStr}')
print('un texto {0}'.format(myStr))