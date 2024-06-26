from cProfile import label
from tkinter import *

from matplotlib.pyplot import text

root = Tk()
root.title('posicionar')
root.geometry('400x300')

def saludo():
    print('hola te saludo')

etiqueta =Label(root, text='Etiqueta')
etiqueta.place(x=30, y=40)

etiqueta2 = Label(root, text='Etiqueta2')
etiqueta2.place(x=100, y=0)

boton = Button(root, text='tocame', command=saludo)
boton.place(x=100, y=100)
root.mainloop()