from logging import root
from tkinter import *
from tkinter import messagebox
from turtle import color

root = Tk()
root.title('Agenda')
root.geometry('700x500')
colorFondo = '#006'
coloLetra = '#FFF'
root.configure(background=colorFondo)

nombre = StringVar()
apellido = StringVar()
correo = StringVar()
telefono = StringVar()
eliminar = StringVar()

tituloEtiqueta = Label(root, text='Mi Aplicacion', fg=coloLetra, bg=colorFondo)
tituloEtiqueta.place(x=270, y=10)

nombreEtiqueta = Label(root, text='Nombre', fg=coloLetra, bg=colorFondo)
nombreEtiqueta.place(x=50, y=50)

entrada1 = Entry(root, textvariable=nombre)
entrada1.place(x=150, y=50)

apellidoEtiqueta = Label(root, text='Apellido', fg=coloLetra, bg=colorFondo)
apellidoEtiqueta.place(x=50, y=80)

entrada2 = Entry(root, textvariable=apellido)
entrada2.place(x=150, y=80)

telefonoEtiqueta = Label(root, text='Telefono', fg=coloLetra, bg=colorFondo)
telefonoEtiqueta.place(x=50, y=110)

entrada3 = Entry(root, textvariable=telefono)
entrada3.place(x=150, y=110)

correoEtiqueta = Label(root, text='Correo', fg=coloLetra, bg=colorFondo)
correoEtiqueta.place(x=50, y=140)

entrada4 = Entry(root, textvariable=correo)
entrada4.place(x=150, y=140)

eliminarEtiqueta = Label(root, text='Telefono', fg=coloLetra, bg=colorFondo)
eliminarEtiqueta.place(x=370, y=50)

spinTelefono = Spinbox(root, textvariable=eliminar)
spinTelefono.place(x=450, y=50)

botonGuardar = Button(root, text='Guardar', fg=coloLetra, bg=colorFondo)
botonGuardar.place(x=170, y=200)

botonEliminar = Button(root, text='Eliminar', fg=coloLetra, bg=colorFondo)
botonEliminar.place(x=490, y=80)



root.mainloop()