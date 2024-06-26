'''
    entrada:
        'nombre'
        2 agentees
        'Adam Caroline Rebecca Frank'
'''

#name = input('Name: ')
name = 'Eric'
#agents = int(input('Agentes: '))
agents = 5
#names = input('Others: ')
names = 'Adam Caroline Rebecca Frank Julio QUintan'

names += ' '
names += name
names = names.split()
names.sort()
time = 0
pos = names.index(name)
for i in range(0,len(names), agents):
    if names[i] == name:
        break
    time += 20
