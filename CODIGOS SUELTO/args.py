def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1,2,3,4,5,6)

def myfunc(x, y=7, *args, **kwargs):
    print(kwargs)

myfunc(2, 3, 4, 5, 6, a=7, b=8)