grilla = [[0 for i in range(1,5)]  for i in range(1,5)]
grilla[0][1] = 2
grilla[0][2] = 2



def left_move(grilla):
    for i in range(0,4):
        for j in range(0,3):
            if grilla[i][j] == 0:
                grilla[i][j] = grilla[i][j+1]

left_move(grilla)
print(grilla)