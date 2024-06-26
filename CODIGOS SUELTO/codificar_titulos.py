file = open('books.txt', 'r')
lines = file.readlines()
title = []
titlecod = ''
for line in lines:
    title = line.split()
    for i in title:
        titlecod += i[0]
    print(titlecod)
    titlecod = ''

file.close()