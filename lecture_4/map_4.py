# def calc1(a, b):
#     return a + b

#calc1 = lambda a, b: a + b

# def select(f, col):              # select - выбирать. math - математика.
#     return [f(x) for x in col]

def where(f, col):               # where - где.  col - седло.
    return [x for x in col if f(x)]

data = [2, 3, 7, 1, 5, 13, 17, 22, 38]

res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)