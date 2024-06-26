'''Sabiendo que la longitud de una lista se calcula igual que la longitud de una cadena de texto,
obtenga el número de palabras que contiene la siguiente cadena de texto:
quote = 'Before software can be reusable, it first has to be usable' '''

quote = 'Before software can be reusable, it first has to be usable'

quote_list = quote.split()
print(len(quote_list))