# Comprehension - понимание |
# | Compresion - сжатие. |
# | Reduction - сокращение.
list_1 = []
for i in range(1, 101):
    list_1.append(i)

list_1 = [i for i in range(1, 101)]
print(list_1)
list_1 = [i for i in range(1, 101) if i % 2 == 0]
print(list_1)
list_1 = [(i, i*i) for i in range(1, 30) if i % 2 == 0]
print(list_1)
list_1 = [(i * 2) for i in range(1, 10) if i % 2 == 0]
print(list_1)

