import re

str = 'Please contact info@sololearn.com for assistance'

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

match = re.search(pattern, str)
if match:
    print(match.group())