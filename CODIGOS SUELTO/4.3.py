'''2. Escriba un programa en Python que acepte 3 números y calcule el mínimo (solución).
Entrada: 7, 4, 9
Salida: 4'''

num1 = int(input('numero1 '))
num2 = int(input('numero2 '))
num3 = int(input('numero3 '))

if num1<num2 and num1<num3:
    print(f'{num1} es el menor')
if num2<num1 and num2<num3:
    print(f'{num2} es el menor')
if num3<num2 and num3<num1:
    print(f'{num3} es el menor')