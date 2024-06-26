import re
#================Metacaracteres sencillos==============#

# . coincide con todo excepto una nueva linea

pattern = r'gr.y'

if re.match(pattern, 'grey'):
    print('Match 1.1')
if re.match(pattern, 'gray'):
    print('match 1.2')
if re.match(pattern, 'blue'):
    print('match 1.3')

# ^ y & coinciden con el start y end de una cadena respectivamente
pattern2 = r'^gr.y$'
if re.match(pattern2, 'grey'):
    print('match 2.1')
if re.match(pattern2, 'gray'):
    print('match 2.2')
if re.match(pattern2, 'stingray'):
    print('match 2.3')

#==============Clases de caracter========================#

# clases de caracter para coincidir con un conjunto
#se crean colocando los caracteres que coinciden dentro de []
# con el serach coincide con cualquier cadena q posea uno de esos caracteres
pattern3 = r'[aeiou]'

if re.search(pattern3, 'grey'):
    print('match 3.1')
if re.search(pattern3, 'qwertyuio'):
    print('match 3.2')
if re.search(pattern3, 'rhythm myths'):
    print('match 3.3')

#tambien pueden ser rangos [a-z], [0-9] [A-Za-z]
pattern4 = r'[A-Z][A-Z][0-9]'

if re.search(pattern4, 'LS8'):
    print('match 4.1')
if re.search(pattern4, 'E3'):
    print('match 4.2')
if re.search(pattern4, '1ab'):
    print('match 4.3')

# ^ se coloca al principio para ivertir la expresion

pattern5 = r'[^A-Z]'

if re.search(pattern5, 'this is all qiuet'):
    print('match 5.1')
if re.search(pattern5, 'AbcdEfG123'):
    print('match 5.2')

#===================mas metacaracteres=========================#

# * cero o mas repeticiones
#puede ser un solo caracter, una clase o un grupo de caracteres entre parentesis
pattern6 = r'egg(spam)*'
if re.match(pattern6, 'egg'):
    print('match 6.1')
if re.match(pattern6, 'eggspamspamegg'):
    print('match 6.2')

if re.match(pattern6, 'spam'):
    print('match 6.3')

# + lo mismo que el anterio lo q una o mas repeticiones
pattern7 = r'g+'

if re.match(pattern7, 'g'):
    print('match 7.1')
if re.match(pattern7, 'gggggggg'):
    print('match 7.2')
if re.match(pattern7, 'abc'):
    print('match 7.3')

# ? lo mismo que el anterio lo q cero o una repeticion
pattern8 = r'ice(-)?cream'

if re.match(pattern8, 'ice-cream'):
    print('match 8.1')
if re.match(pattern8, 'icecream'):
    print('match 8.2')
if re.match(pattern8, 'sausages'):
    print('match 8.3')
if re.match(pattern8, 'ice--ice'):
    print('match 8.4')

# {x,y} numero de repeticiones entre x y y
#si falta el primer numero se asume q es cero
#si falta el segundo se continua hasta el infinito
pattern9 = r'9{1,3}$'

if re.match(pattern9, '9'):
    print('match 9.1')
if re.match(pattern9, '999'):
    print('match 9.2')
if re.match(pattern9, '9999'):
    print('match 9.3')

#=============Grupos=============================#

# un grupo puede ser creado al colocar una parte de una expresion
# entre parentesis ()
#esto siginifica q puede ser pasado como argumento a metacaracteres como ? y *

patterng = r'egg(spam)*'

if re.match(patterng, 'egg'):
    print('match g.1')
if re.match(patterng, 'eggspamspamspamegg'):
    print('match g.2')
if re.match(patterng, 'spam'):
    print('match g.3')

#el contenido de un grupo en una coincidencia puede ser
#acceddido con la funcioin group()
#una llamada de group(0) o group() devuelve toda la coincidencia
#una llamada a group(n) devuelve el n-esimo grupo

patterng2 = r'a(bc)(de)(f(g)h)i'

match_g1 = re.match(patterng2, 'abcdefghijklmnop')
if match_g1:
    print(match_g1.group())
    print(match_g1.group(0))
    print(match_g1.group(1))
    print(match_g1.group(2))
    print(match_g1.group(3))

#grupos con nombre se ponen de la fomra (?P<nombre>...)
patterng3 = r'(?P<first>abc)(?:def)(ghi)'

match_g2 = re.match(patterng3, 'abcdefghi')
if match_g2:
    print(match_g2.group())
    print(match_g2.groups())

# | significa 'o' rojo o azul por ejemplo

patterng4 = r'gr(a|e)y'

if re.match(patterng4, 'gray'):
    print('match g4.1')
if re.match(patterng4, 'grey'):
    print('match g4.2')
if re.match(patterng4, 'griy'):
    print('match g4.3')

#=============secuencias espaciales===============#

#se usan con una barra invertida seguida de un nuemro entre 1 y 99
# \1 \17 \99
#councide con la expresion del grupo de ese numero
pattern10 = r'(.+) \1'

match10_1 = re.match(pattern10, 'word word')
if match10_1:
    print('match 10.1')

match10_2 = re.match(pattern10, '?! ?!')
if match10_2:
    print('match 10.2')

match10_3 = re.match(pattern10, 'abc cde')
if match10_3:
    print('match 10.3')

# \d digitos
# \s espacios en blanco
# \w caracteres alfanumericos
# tineen sus respactivas versiones en mayusculas \D \S \W
#significan lo contrario, pro ejemplo \D coincide con cualquier
#caracter q no sea un digito

pattern11 = r'(\D+\d)'

if re.match(pattern11, 'Hi 999!'):
    print('match 11.1')
if re.match(pattern11, '1, 23, 456!'):
    print('match 11.2')
if re.match(pattern11, ' ! $?'):
    print('match 11.3')

# \A y \Z principio y final de una cadena
# \b cadena vacia entre caracteres \w y \W
# \B una cadena vacia en cualquier otro caso

pattern12 = r'\b(cat)\b'

if re.search(pattern12, 'The cat sat!'):
    print('match 12.1')
if re.search(pattern12, 'Wes>cat<tered?'):
    print('match 12.2')
if re.search(pattern12, 'Wescattered'):
    print('match 12.3')