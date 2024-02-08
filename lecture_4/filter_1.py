data = [25, 1, 15, 7, 78, 215, 34, 75, 17, 14, 45, 32]
print(data)
data = list(filter(lambda x: x % 10 == 5, data))
print(data)