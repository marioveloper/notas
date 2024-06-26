from logging import root
from tkinter import *
from turtle import left

from matplotlib.pyplot import text

#ventana
root = Tk()
#root.geometry('400x300')
root.config(bg='goldenrod3')
root.resizable(0,0)
root.title('checkbutton')

#variables
imagen = PhotoImage(file='screenshot-route.gif')
queso = IntVar()
lechuga = IntVar()
#funciones

def orden():
    lista = ''
    if (queso.get()):
        lista += 'Con queso'
    else:
        lista += 'Sin queso'
    if (lechuga.get()):
        lista += ' y con lechuga'
    else:
        lista += ' y sin lechuga'
    imprimir.config(text = lista)
#logica
Label(root, image=imagen).pack(side=LEFT)

frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg='goldenrod3')

Label(frame, text='como quieres', bg='goldenrod3', font='Courier 10').pack(anchor='w')
Checkbutton(frame, text='con queso', variable=queso, onvalue=1, offvalue=0, bg='goldenrod3', font='Courier 10', command=orden).pack(anchor='w')
Checkbutton(frame, text='con lechuga', variable=lechuga, onvalue=1, offvalue=0, bg='goldenrod3', font='Courier 10', command=orden).pack(anchor='w')

imprimir = Label(frame, bg='goldenrod3')
imprimir.pack()

root.mainloop()