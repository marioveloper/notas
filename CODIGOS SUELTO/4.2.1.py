'''1. Escriba un programa en Python que acepte la opción de dos jugadoras en
Piedra-Papel-Tijera y decida el resultado (solución).
Entrada: persona1=piedra; persona2=papel
Salida: Gana persona2: El papel envuelve a la piedra'''

entrada1 = input('player1: ')
entrada2 = input('player2: ')

if entrada1 == 'papel' and entrada2 == 'piedra':
    print('Gana player 1 el papel envuelve la piedra')
elif entrada1 == 'piedra' and entrada2 == 'tijera':
    print('Gana player 1 la piedra rompe la tijera')
elif entrada1 == 'tijera' and entrada2 == 'papel':
    print('Gana player 1 la tijera corta el papel')
elif entrada2 == 'papel' and entrada1 == 'piedra':
    print('Gana player 2 el papel envuelve piedra')
elif entrada2 == 'piedra' and entrada1 == 'tijera':
    print('Gana player 2 la piedra rompe la tijera')
elif entrada2 == 'tijera' and entrada1 == 'papel':
    print('Gana player 2 lA tijera corta el papel')
else:
    print('intorduzcan datos correctos')