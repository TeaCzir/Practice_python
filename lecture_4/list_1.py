a = [2, 3, 7, 1, 5, 13, 17, 22, 38]
def f(a):
    return a
print(f(a))

def s(a):
    res = list()
    for i in a:
        if i % 2 == 0:
            res.append((i, i**2))
    print(res)
def d(a):
    res = list()
    for i in a:
        if i % 2 == 0:
            res.append(i)
    print(res)
d(a)   
s(a)

