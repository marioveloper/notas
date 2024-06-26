numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

numbers2 = tuple(range(10))
a,b,c,*d, e = numbers2
print(d)