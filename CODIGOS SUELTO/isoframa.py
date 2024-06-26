from logging import root
from tkinter import *
import random

root = Tk()
root.title('juego')

#variables
intentos = 0
minimo = 1
maximo = 25
numero = random.randint(minimo, maximo)
mensajePrincipal = f'he pensado un numero entre {minimo} y {maximo}, a ver si adivinas cual'
#bloque principal

#

def comprobar():

    texto = Label(root, text=mensajePrincipal)
    texto.pack()

    texto = Label(root, text=comprobar)
    texto.pack()


root.mainloop()#ejecutar