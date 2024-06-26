from logging import root
from tkinter import *

from importlib_metadata import EntryPoint

root = Tk()

root.title('Radiobuttons')
root.geometry('400x300')
root.config(bg='goldenrod3')
root.resizable(0,0)

opcion = IntVar()
numero = IntVar()

def operacion():
    num = numero.get()
    if opcion.get() == 1:
        total = num*5
    elif opcion.get() == 2:
        total = num*10
    elif opcion.get() == 3:
        total = num*20
    elif opcion.get() == 4:
        total = num*30
    elif opcion.get() == 5:
        total = num*40
    else:
        total = num*num
    print(f'El total es: {str(total)}')

etiqueta1 = Label(root, text='escribe un numero', bg='goldenrod3')
etiqueta1.place(x=20, y=20)

entrada1 = Entry(root, bg='goldenrod4', bd=5, textvariable=numero)
entrada1.place(x=150, y=20)

etiqueta2 = Label(root, text='elige la cantidad', bg='goldenrod3')
etiqueta2.place(x=20, y=50)

x5 = Radiobutton(root, text='x5', value=1, bg='goldenrod3', bd=2, variable=opcion)
x5.place(x=20, y=80)

x10 = Radiobutton(root, text='x10', value=2, bg='goldenrod3', bd=2, variable=opcion)
x10.place(x=70, y=80)

x20 = Radiobutton(root, text='x20', value=3, bg='goldenrod3', bd=2, variable=opcion)
x20.place(x=120, y=80)

x30 = Radiobutton(root, text='x30', value=4, bg='goldenrod3', bd=2, variable=opcion)
x30.place(x=170, y=80)

x40 = Radiobutton(root, text='x40', value=5, bg='goldenrod3', bd=2, variable=opcion)
x40.place(x=220, y=80)

boton = Button(root, text='realizar operacion', bg='goldenrod3', bd=5, command=operacion)
boton.place(x=100, y=140)

root.mainloop()