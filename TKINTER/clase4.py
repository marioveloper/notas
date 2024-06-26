from logging import root
from tkinter import *

root = Tk()

root.title('Entrada')
root.geometry('325x200')

nombre = StringVar()
apellido = StringVar()

nombre.set('escribe aqui tu nombre')
apellido.set('escribe aqui')

def saludar():
    print('hola ' + nombre.get() + ' ' + apellido.get() + ' como estas')

etiqueta1 = Label(root, text='escribe tu nombre aqui: ')
etiqueta1.place(x=10,y=10)
entrada1 =Entry(root, textvariable=nombre)
entrada1.place(x=170, y=10)

etiqueta2 = Label(root, text='escribe tu apellido aqui: ')
etiqueta2.place(x=10,y=40)
entrada2 =Entry(root, textvariable=apellido)
entrada2.place(x=170, y=40)

boton = Button(root, text='Saludar', command=saludar)
boton.place(x=155, y=100)

root.mainloop()