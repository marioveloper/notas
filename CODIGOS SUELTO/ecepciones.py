#fnilly se ejecuta si o si
try:
    print(1.1)
except ZeroDivisionError:
    print(1.2)
finally:
    print(1.3)

try:
    print(2.1)
except ZeroDivisionError:
    print(2.2)
finally:
    print(2.3)

#try, except puede tener un else que se ejecuta cuando moo ocurre ningun error
try:
    print(3.1)
except ZeroDivisionError:
    print(3.2)
else:
    print(3.3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4.2)
else:
    print(4.3)

#se pueden lanzar excepciones cunado se cumple alguna condicion
#con la declaracion raise

num = 102
#if num > 100:
#    raise ValueError

#se pueden levantar con argumentos q den detalles sobre ellas
name = '123'
raise NameError('invlaid name')