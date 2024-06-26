from tkinter import *

#ventana
root = Tk()
root.title('CALCULADORA')
root.geometry('300x300')

entrada1 = Entry(root)
entrada1.grid(row=1, columnspan=6, sticky=W+E)

#variables
i=0

#funciones
def obtenerNumeros(n):
    global i
    entrada1.insert(i, n)
    i+=1

def obtenerOperacion(operator):
    global i
    tamano = len(operator)
    entrada1.insert(i, operator)
    i+=tamano

def limpiar():
    entrada1.delete(0, END)

def borrar():
    entrada1_estado = entrada1.get()
    if(len(entrada1_estado)):
        entrada1_nuevo = entrada1_estado[:-1]
        limpiar()
        entrada1.insert(0, entrada1_nuevo)
    else:
        limpiar()

def calcular():
    entrada = entrada1.get()
    try:
        expresion = parser.expr(entrada).compile()
        resultado = eval(expresion)
        limpiar()
        entrada1.insert(0, resultado)
    except:
        print('An exception occurred')

#fila uno
Button(root, text='AC', command=lambda:limpiar()).grid(row=2, column=0, sticky=W+E)
Button(root, text='<-', command=lambda:borrar()).grid(row=2, column=1, sticky=W+E)
Button(root, text='%', command=lambda:obtenerOperacion('%')).grid(row=2, column=2, sticky=W+E)
Button(root, text='/', command=lambda:obtenerOperacion('/')).grid(row=2, column=3, sticky=W+E)
Button(root, text='^', command=lambda:obtenerOperacion('**')).grid(row=2, column=4, sticky=W+E)

Button(root, text='1', command=lambda:obtenerNumeros(1)).grid(row=3, column=0, sticky=W+E)
Button(root, text='2', command=lambda:obtenerNumeros(2)).grid(row=3, column=1, sticky=W+E)
Button(root, text='3', command=lambda:obtenerNumeros(3)).grid(row=3, column=2, sticky=W+E)
Button(root, text='x', command=lambda:obtenerOperacion('*')).grid(row=3, column=3, sticky=W+E)
Button(root, text='^2', command=lambda:obtenerOperacion('**2')).grid(row=3, column=4, sticky=W+E)

Button(root, text='4', command=lambda:obtenerNumeros(4)).grid(row=4, column=0, sticky=W+E)
Button(root, text='5', command=lambda:obtenerNumeros(5)).grid(row=4, column=1, sticky=W+E)
Button(root, text='6', command=lambda:obtenerNumeros(6)).grid(row=4, column=2, sticky=W+E)
Button(root, text='-', command=lambda:obtenerOperacion('-')).grid(row=4, column=3, sticky=W+E)
Button(root, text='(', command=lambda:obtenerOperacion('(')).grid(row=4, column=4, sticky=W+E)

Button(root, text='7', command=lambda:obtenerNumeros(7)).grid(row=5, column=0, sticky=W+E)
Button(root, text='8', command=lambda:obtenerNumeros(8)).grid(row=5, column=1, sticky=W+E)
Button(root, text='9', command=lambda:obtenerNumeros(9)).grid(row=5, column=2, sticky=W+E)
Button(root, text='+', command=lambda:obtenerOperacion('+')).grid(row=5, column=3, sticky=W+E)
Button(root, text=')', command=lambda:obtenerOperacion(')')).grid(row=5, column=4, sticky=W+E)

Button(root, text='0', command=lambda:obtenerNumeros(0)).grid(row=6, column=0, columnspan=2, sticky=W+E)
Button(root, text='.', command=lambda:obtenerOperacion('.')).grid(row=6, column=2, sticky=W+E)
Button(root, text='=').grid(row=6, column=3, columnspan=2, sticky=W+E)




#ejecutando
root.mainloop()