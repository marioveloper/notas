'''
    hay un problema con tu teclado
    escribe simboles aleatorios en el texto q estas escribiendo
    necesitas limpair el texto

    pregunta: toma un texto que contiene simbolos aleatorios
    y tranformalo en texto q no contiene ninguno de ellos

    entrada: un string con simbolos aleatorios
    salida: un stign con los simbolos removidos

    ej entrada: #l$e#$#t@$#s go @an%^*d g**et #l##unch$$
    ej salida : lets go and get lunch
'''

#text = '#l$e#$#t@$#s go @an%^*d g**et #l##unch$$ 78'
text = 'H&i ########'
cleaned = ''
for i in text:
    if i.isalpha() or i == ' ' or i.isalnum():
        cleaned += i
print(cleaned)