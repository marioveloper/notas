from tkinter import *
from tkinter import messagebox

from matplotlib.pyplot import text

root = Tk()

root.title('listbox, agregar')#poner titulo

root.geometry('400x300')#dimensionar ventana
root.iconbitmap('01.ico')#icono
root.resizable(0,0)#cambiar tamano
root.config(bg='goldenrod3')#cambiar color

#logica app
#funcion
def agregar():
    listaProductos.insert(END, entrada.get())
#listbox

productos = Label(root, text='Productos')
productos.pack()

listaProductos = Listbox(root, width=50)
listaProductos.insert(0, 'Carne')
listaProductos.insert(1, 'Pollo')
listaProductos.insert(2, 'Verdura')
listaProductos.insert(3, 'Jugo')
listaProductos.pack()

#eliminar productos
listaProductos.delete(0)

entrada = Entry(root, bd=2)
entrada.pack()

boton = Button(root, text='agragar producto', command=agregar)
boton.pack()









#ventanas emergentes
def cerrar():
    messagebox.askquestion('Cerrar', message='esta seguro?')

def licencia():
    messagebox.showinfo('version', message='version 1.0')

def error():
    messagebox.showerror('!ERROR!', message='se encontro un error grave')

def atencion():
    messagebox.showwarning('Atencion', message='se borrara el actual')
#logica menu clase 8

menuBar = Menu(root)
root.config(menu=menuBar)

archivoMenu = Menu(menuBar, tearoff='off')

archivoMenu.add_command(label='nuevo')
archivoMenu.add_command(label='abrir', command=atencion)
archivoMenu.add_command(label='guardar', command=error)
archivoMenu.add_command(label='cerrar', command=cerrar)
archivoMenu.add_separator()
archivoMenu.add_command(label='salir', command=root.quit)

editMenu = Menu(menuBar, tearoff=0)

editMenu.add_command(label='cortar')
editMenu.add_command(label='copiar')
editMenu.add_command(label='pegar')

ayudaMenu = Menu(menuBar, tearoff='off')

ayudaMenu.add_command(label='licencia', command=licencia)
ayudaMenu.add_separator()

menuBar.add_cascade(label='Archivo', menu=archivoMenu)
menuBar.add_cascade(label='Editar', menu=editMenu)
menuBar.add_cascade(label='Ayuda', menu=ayudaMenu)

root.mainloop()#ejecutar