a = {3, 4, 14, 8, 53, 62, 7}
b = {3, 5, 4, 2, 22, 62, 8, 14}
print(a, b)
c = a.copy()
print(c)
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
dl = a.difference(b)
print(dl)
dr = b.difference(a)
print(dr)
q = a.union(b).difference(a.intersection(b))
print(q)

