'''Escriba un programa en Python que pida (por separado) dos valores numéricos y un operando
(suma, resta, multiplicación, división) y calcule el resultado de la operación, usando para ello
la sentencia match-case.
Controlar que la operación no sea una de las cuatro predefinidas. En este caso dar un mensaje
de error y no mostrar resultado final.
Ejemplo
• Entrada: 4, 3, +
• Salida: 4+3=7'''

num1 = int(input('digite un numero '))
num2 = int(input('digite otro numero '))
operacion = input('que opreacion realizar ')

match operacion:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)