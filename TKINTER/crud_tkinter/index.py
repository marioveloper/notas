from tkinter import ttk
from tkinter import *
import sqlite3
from unicodedata import name

from click import command
from matplotlib.pyplot import grid, text
from numpy import delete, record

class Product:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Product Aplication')

        #crear frame
        frame = LabelFrame(self.wind, text='Register a new product')
        frame.grid(row = 0,column = 0, columnspan=3, pady=20)

        #entrada nombre
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)


        #entrada precio
        Label(frame, text='Price: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        #boton agregar producto
        ttk.Button(frame, text='Save product', command=self.add_product).grid(row=3, columnspan=2, sticky=W+E)

        #salida de mensajes
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)



        #tabla
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1', text='Price', anchor=CENTER)

        ttk.Button(text='DELETE', command=self.delete_product).grid(row=5, column=0, sticky=W+E)
        ttk.Button(text='EDIT', command=self.edit_product).grid(row=5, column=1, sticky=W+E)

        self.get_products()


    def run_query(self, query, parameters = ()):#funcion para conectar a la bd
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_products(self):
        #limpiar la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #ejecutar consulta
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        #insertar datos en tabla
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

    def validation(self):
        return len(self.name.get()) !=0 and len(self.price.get()) !=0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text']='El Producto {} ha sido agregado'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text']='nombre y precio requeridos'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Selecciona un indice'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'El producto {} ha sido elimindado'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Selecciona un indice'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar Producto'
        #old name
        Label(self.edit_wind, text='Old name: ').grid(row = 0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=name), state = 'readonly').grid(row=0, column=2)
        #new name
        Label(self.edit_wind, text='New Name').grid(row=1, column=1)
        new_name=Entry(self.edit_wind)
        new_name.grid(row=1, column=2)

        #old price
        Label(self.edit_wind, text='Old Price: ').grid(row = 2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_price), state = 'readonly').grid(row=2, column=2)
        #new price
        Label(self.edit_wind, text='New Price').grid(row=3, column=1)
        new_price=Entry(self.edit_wind)
        new_price.grid(row=3, column=2)

        #boton
        Button(self.edit_wind, text='Update', command=lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row=4, column=2, sticky=W+E)

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters= (new_name, new_price, name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'El preoducto {} ha sido actualizado satisfactoriamente'.format(name)
        self.get_products()

if __name__ == '__main__':#ejecuta la ventana
    window = Tk()
    aplication = Product(window)
    window.mainloop()