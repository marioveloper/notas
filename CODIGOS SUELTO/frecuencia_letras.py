text = input()
letter = input()
part = 0
for i in text:
    if i == letter:
        part += 1

total = len(text)
porcent = int(part/total*100)

print(porcent)