import pytesseract as tsc
import os
import scanner
elementos = os.listdir(os.getcwd()+'\img')
print(elementos)
for elemento in elementos:
    print(elemento)
    if elemento.split('.')[-1] in ('jpg', 'jpeg', 'png'):
        #texto = tsc.image_to_string('img\\'+elemento)
        #print(elemento, texto)
        #print(scanner.sacar_texto(elemento))
        texto = scanner.sacar_texto(elemento)
        texto = texto.split(' ')
        for i in texto:
            if len(i)==4 and i.isdigit():
                print(i)
