
def fib(n):
    if n in [1,2]:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(8))
print()
list_1 = []
for i in range(1, 14):
    list_1.append(fib(i))
    print(list_1)
print()    
print(list_1)

       