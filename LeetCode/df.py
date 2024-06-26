def FirstFactorial(num):
    num = int(num)
    fact = 1
    while num > 1:
        fact = fact*num
        num = num-1
# code goes here
    return fact

# keep this function call here
print(FirstFactorial(input()))