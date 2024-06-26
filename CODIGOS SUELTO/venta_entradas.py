# la entrada de un adulto cuesta 20
# la de un nino menor de 18 cuesta 5

data = {
    '100-90': 25,
    '42-01': 48,
    '55-09': 12,
    '128-64': 71,
    '002-22': 18,
    '321-54': 19,
    '097-32': 33,
    '065-135': 64,
    '99-043': 80,
    '111-99': 11,
    '123-019': 5,
    '109-890': 72,
}
age = int(input())

total = 0
ganancia = 0

for value in data.values():
    if value >= 18:
        total += 20
    if value < 18:
        total += 5

    if value >= age:
        ganancia += 20
    if value < age:
        ganancia += 5

crec = int(((ganancia-total)/total)*100)
print(crec)