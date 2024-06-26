import random

dimension = 3

mundo = [[0 for j in range(dimension+2)] for i in range(dimension+2)]
mundo2 = [[0 for j in range(dimension+2)] for i in range(dimension+2)]

for i in range(1, dimension+1):
    for j in range(1, dimension+1):
        mundo[i][j] = random.randint(0,1)

for i in range(1, dimension+1):
    for j in range(1, dimension+1):
        item = mundo[i][j]
        vecinos = mundo[i-1][j-1]+mundo[i-1][j]+mundo[i-1][j+1]+mundo[i][j-1]+mundo[i][j+1]+mundo[i+1][j-1]+mundo[i+1][j]+mundo[i+1][j+1]

        #si esta vivo
        if item == 1:
            #si tiene 2 o 3 vecinos vive
            if vecinos == 2 or vecinos == 3:
                mundo2[i][j] = 1
            #sino muere
            else:
                mundo2[i][j] = 0
        #si esta muerto
        else:
            #si tiene 3 vecinos nace
            if vecinos == 3:
                mundo2[i][j] == 1

print('mundo1')
for row in mundo:
    print(row)

print('mundo2')
for row in mundo2:
    print(row)