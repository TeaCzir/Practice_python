
def filter(f, col):               # where - где.  col - седло. filter - фильтр.
    return [x for x in col if f(x)]

data = [2, 3, 7, 1, 5, 13, 17, 22, 38]
print(data)
res = map(int, data)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)

res = list(map(lambda x: (x, x**2), res))
print(res)