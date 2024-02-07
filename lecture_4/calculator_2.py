def calc1(a, b):
    return a + b

def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

math(calc1, 4, 3)
math(calc2, 8, 7)