text = input()
letters = 0
for i in text:
    if i != ' ':
        letters += 1

text = text.split()
palabra = len(text)

print(letters/palabra)