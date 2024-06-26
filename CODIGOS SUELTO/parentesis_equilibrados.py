def balanced(expression):
    count = 0
    list = []

    for i in expression:
        if i == '(':
            list.insert(0, i)
            count += 1
        if i == ')':
            list.pop(0)
            count -= 1
            if count < 0:
                return False
        if count == 0:
            return True
        else:
            return False

expres = '(a() eee))'
print(balanced(expres))