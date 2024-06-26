'''Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.
Ejemplos válidos de isogramas:
• lumberjacks
• background
• downstream
• six-year-old'''

cadena = list(input('introduce algo '))
for i in cadena:
    if i == ' ':
        cadena.remove(i)

isograma = True
for i in cadena:
    if i in cadena[:]:
        isograma = False

if isograma:
    print('es un isograma')
else:
    print('no es un isogrma')

print(cadena)
