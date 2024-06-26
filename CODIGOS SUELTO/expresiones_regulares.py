import re

pattern = r'spam'

if re.match(pattern, 'spamspamspam'):#solo busca al principio
    print('match')
else:
    print('no match')

if re.search(pattern, 'eggsspamsausagespam'):
    print('match')
else:
    print('no match')

print(re.findall(pattern, 'esspamsausagespam'))
