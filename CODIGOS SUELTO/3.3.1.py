'''4. Escriba un programa en Python que acepte un entero n y compute el valor de n + nn
+ nnn (solución).
Entrada: 5
Salida: 615'''

numero = int(input('NUmero: '))

decena = str(numero)*2

centena = str(numero)*3

print(numero+int(decena)+int(centena))