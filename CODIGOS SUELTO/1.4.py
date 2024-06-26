'''Escriba un programa en Python que compute el futuro valor de una cantidad de dinero,
a partir del capital inicial, el tipo de interés y el número de años (solución).
Entrada: capital=10000; interés=3.5; años=7
Salida: 12722.792627665729'''

capital_inicial = int(input('Capital: '))
ano = int(input('ano: '))
interes = float(input('Interes: '))

capital_final = capital_inicial*(1+interes*ano/100)

print(capital_final)