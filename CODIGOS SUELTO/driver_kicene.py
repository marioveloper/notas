'''
    entrada: Eric
            2
            Adam Caroline Rebecca Frank
'''

name = 'Eric'
agents = 2
lista = 'Adam Caroline Rebecca Frank'
lista += ' '+ name
lista = lista.split()
lista.sort()
pos = lista.index('Eric')+1
time = 20

while pos > agents:
    time += 20
    pos -= agents
print(time)