'''Escriba un programa en Python que acepte una ruta remota de recurso samba, y lo
separe en nombre(IP) del equipo y ruta (solución).
Entrada: //1.1.1.1/eoi/python
Salida: equipo=1.1.1.1; ruta=/eoi/python'''

entrada = input('direccion: ')

entrada = entrada.lstrip('/')
posicion = entrada.find('/')
equipo = entrada[:posicion]
ruta = entrada[posicion:]
print(f'equipo: {equipo}, ruta: {ruta}')