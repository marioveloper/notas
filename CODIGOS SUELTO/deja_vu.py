'''
    no estas prestando atencion y accidentalmente
    escribes un monton de letras aleatoreas en el teclado
    quires saber si haz escrito alguna letra doble
    o si todas son unicas

    pregunta: si estas recibiendo un string de letras aleatorias
    tienes q evaluar si hay letras repetidas en el string

    entrada: un string de letras
    salida: 'Deja Vu' si alguna letra es repetida
            'Unique' si no hay repeticiones

    ej entrada: aaaaaaghhhhhhhjkllll
    ej salida : Deja Vu
'''

#string = 'aaaaaaghhhhhhhjkllll'
string = 'eqsdfghjkloiuytrw'
def dejavu(string):
    for i in range(0,len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return 'Deja Vu'
    return 'Unique'

print(dejavu(string))