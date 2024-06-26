'''
    quieres tomar una lista de numeros y encontrar la suma
    de todos los numeros pares en la lista

    pregunta = encuentra la suma de todos los numeros pares
    en la lista

    entrada: una linea con el tamano de la lista(N)
            los N elementos de la lista
    salida: un entero q representa la suma d elos pares

    ej entrad: 9
            1
            2
            3
            4
            5
            6
            7
            8
            9
    ej Salidad:20

'''
lista = []
N = int(input())
sum = 0

for i in range(0, N):
    aux = int(input())
    lista.append(aux)

for i in lista:
    if i%2 == 0:
        sum += i

print(sum)