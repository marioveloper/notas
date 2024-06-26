from tkinter import *

root = Tk()
root.title('botones')
root.geometry('400x300')

boton1 = Button(root, text="Minimizar", command=root.iconify, bg='blue')#iconify minimiza
boton1.pack(side=LEFT)

def imprimir():
    label1 = Label(root, text='imprimiendo')
    label1.pack()

boton2 = Button(root, text='imprimir', command=imprimir)
boton2.pack()





root.mainloop()