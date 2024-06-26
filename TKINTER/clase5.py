from logging import root
from tkinter import *

from importlib_metadata import EntryPoint

root = Tk()

root.title('Entrada')
root.geometry('325x250')
root.config(bg='black')
root.resizable(0,0)

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

#nombre.set('escribe aqui tu nombre')
#apellido.set('escribe aqui')

def saludar():
    saludo.set('hola ' + nombre.get() + ' ' + apellido.get())


etiqueta1 = Label(root, text='escribe tu nombre aqui: ',bd=4,bg='gray', font=('Curier 10'))
etiqueta1.place(x=10,y=10)
entrada1 =Entry(root, textvariable=nombre, bd=3, bg='gray')
entrada1.place(x=170, y=10)

etiqueta2 = Label(root, text='escribe tu apellido aqui: ', bd=4,bg='gray', font=('Curier 10'))
etiqueta2.place(x=10,y=40)
entrada2 =Entry(root, textvariable=apellido, bd=3, bg='gray')
entrada2.place(x=170, y=40)

entrada3 = Entry(root, bd=20, font=('Curier 10'), textvariable=saludo, state='disable')
entrada3.place(x=80, y=150)

boton = Button(root, text='Saludar', command=saludar, bd=5, bg='blue')
boton.place(x=150, y=100)

root.mainloop()