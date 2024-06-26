num = 6

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)


for i in range(0, num):
    print(fibonacci(i))