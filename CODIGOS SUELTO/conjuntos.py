# los conjuntos son colecciones desordenadas q son indices unicos
# no tienen elementos duplicados
num_set = {1, 2, 3, 4, 5}

print(3 in num_set)

# admiten la funciones:
# add() anadir elementos al conjunto
# remove() eliminar un elemento especifico

nums = {1, 2, 3, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

#se pueden combinar mediante operaciones matematicas
# union | : combina los elementos de ambos
# interseccion & : solo los q estan en amobs
# difference - : los q estn en el primero q no estan en el seundo
# symetric difference ^ : en cualquiera de los dos pero no en ambos

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)