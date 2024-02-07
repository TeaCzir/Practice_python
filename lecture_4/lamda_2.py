# def calc1(a, b):
#     return a + b

#calc1 = lambda a, b: a + b

def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(lambda a, b: a + b, 7, 53)
math(calc2, 8, 7)