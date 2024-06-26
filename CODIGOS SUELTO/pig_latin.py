'''
tienes dos amigos hablando latin cerdo ono con el otro
pig latin es la misma palabra en el mismo orden
solo q tomas la primera letra de cada palabra
y la ones al final y anades 'ay' al final

ej: road = oadray

pregunta: toma una sentencia en ingles y conviertela
a Pig Latin

Entrada: un string en ingels con lo q necesitas transformarr

Salida: el mismo string en pig Latin

ej entrada: nevermind youve got them
ej salida : evermindnay ouveyey otgey hemtay
'''

string = 'nevermind youve got them'
string = string.split()
pig_latin = ''
word = ''
for i in string:
    word = i[1:]
    word += i[0]
    word += 'ay'
    pig_latin += ' '
    pig_latin += word

pig_latin = pig_latin[1:]