def sum_namber(n, y = 'Hello'):
    print(y)
    summ = 0
    for i in range(1, n + 1):
        summ += i
    return summ
    print('stop')

a = sum_namber(5, 'Gwerti')  
print(a)