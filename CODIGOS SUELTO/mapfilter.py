#named function
def add_five(x):
    return x+5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#lambda
nums2 = [66, 77, 88, 99]

result2 = list(map(lambda x: x+10, nums2))
print(result2)