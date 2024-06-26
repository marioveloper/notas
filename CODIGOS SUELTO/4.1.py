'''Dada una variable year con un valor entero, compruebe si dicho año es bisiesto o no lo es.
Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre
100, o bien si es divisible entre 400. Puedes hacer la comprobación en esta lista de años
bisiestos.
Ejemplo
• Entrada: 2008
• Salida: Es un año bisiesto
'''

ano = int(input('ano: '))
if ano % 400 == 0:
    print(f'{ano} es bisiesto')
elif ano % 4 == 0 and ano % 100 != 0:
    print(f'{ano} es bisiesto')
else:
    print(f'{ano} no es bisiesto')