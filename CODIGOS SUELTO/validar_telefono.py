import re
pattern = '[1,8,9]\d\d\d\d\d\d\d$'
str = '12345678'

match = re.match(pattern, str)
if match:
    print(match.group())
