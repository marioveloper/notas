'''1. Escriba un programa en Python que realice las siguientes 9 multiplicaciones. ¿Nota
algo raro? (solución)
1 · 1
11 · 11
111 · 111
...
111111111 · 111111111'''

num1 = 1
for digito in range(1, 10):
    #print(num1)
    print(num1*num1)
    num1 = int(str(num1)+'1')