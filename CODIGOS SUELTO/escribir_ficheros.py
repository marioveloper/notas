#se utiliza el metodo write

file = open('newfile.txt', 'w')
file.write('this has been written to a file')
file.close()

#para anadir contenido a un archivo ya existente puedes abrirlo en modo a
file = open('newfile.txt', 'a')
file.write('\nthis has been added to the file')
file.close()

#write devuelve el numero de bytes escritos
msg = 'hello world'
file = open('newfile.txt', 'w')
amount_written = file.write(msg)
print(amount_written)
file.close