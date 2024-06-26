#los archivos se abren con la funcion open('nombre_del_archivo.extension')
#se puede especificar el modo
# r significa: lectura
# w significa: reescribir el contenido de un archivo
# a significa: modo append, para anadir nuevo contenido al final del archivo
# b significa: modo binario(para archivos q no son de texto como sonido, imgen, etc...)
#se pueden combinar dos modos ej: open('filename.txt', 'wb') para escritura binaria
# se cierran con el metodo close()
archivo = open('books.txt')
archivo.close()

#el metodo read() se usa para leer el contenido de un archivo
file = open('books.txt')
cont = file.read()
print(cont)
print(file.read(5))
file.close()
#para leer una cantidsd de archivo se puede pasar el numero de bytes a leer
file = open('books.txt')
print(file.read(5))
print(file.read(7))
print(file.read())
file.close()

#para recuperar cada linea de un archivo puedes usar el metodo readlines()
file = open('books.txt')
for line in file.readlines():
    print(line)
file.close()
