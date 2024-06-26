def secuencia(num):
    contador = 1
    while num != 1:
        if num%2 == 0:
            num = int(num / 2)
            contador+=1
        else:
            num *=3
            num +=1
            contador+=1
    return contador

def mayor(num1, num2):
    numero = 0
    for i in range(num1,num2):
        if secuencia(i)>=numero:
            numero = secuencia(i)
    return numero


num = int(input('numeros '))
num2 = int(input('numeros '))

print(mayor(num, num2))

