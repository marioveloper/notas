'''Dada una cadena de texto, indique el número de vocales que tiene.
Ejemplo
• Entrada: Supercalifragilisticoespialidoso
• Salida: 15'''

entrada = input('escriba ')
cantidad = 0
for letters in entrada:
    if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u'\
        or letters == 'A' or letters == 'E' or letters == 'I' or letters == 'O' or letters == 'U':
        cantidad+=1
print(f'{cantidad} vocales')