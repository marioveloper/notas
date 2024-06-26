from tkinter import *

root = Tk()

root.title('menu')#poner titulo

root.geometry('400x300')#dimensionar ventana
root.iconbitmap('01.ico')#icono
root.resizable(0,0)#cambiar tamano
root.config(bg='goldenrod3')#cambiar color

#logica app
menuBar = Menu(root)
root.config(menu=menuBar)

archivoMenu = Menu(menuBar, tearoff='off')

archivoMenu.add_command(label='nuevo')
archivoMenu.add_command(label='abrir')
archivoMenu.add_command(label='guardar')
archivoMenu.add_command(label='cerrar')
archivoMenu.add_separator()
archivoMenu.add_command(label='salir', command=root.quit)

editMenu = Menu(menuBar, tearoff=0)

editMenu.add_command(label='cortar')
editMenu.add_command(label='copiar')
editMenu.add_command(label='pegar')

ayudaMenu = Menu(menuBar, tearoff='off')

ayudaMenu.add_command(label='ayuda')
ayudaMenu.add_separator()

menuBar.add_cascade(label='Archivo', menu=archivoMenu)
menuBar.add_cascade(label='Editar', menu=editMenu)
menuBar.add_cascade(label='Ayuda', menu=ayudaMenu)

root.mainloop()#ejecutar