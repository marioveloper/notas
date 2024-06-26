try:
    f = open('books.txt')
    cont = f.read()
    print(cont)
finally:
    f.close()

# una alternativa a lo anterior es usar with
with open('books.txt') as f:
    print(f.read())