text = input()
dict = {}
for i in range(0, len(text)):
    if i in dict:
        dict[i]+=1
    else:
        dict+={i:0}

print(dict)