def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

# print(sum_str('q','e','l'))
# print(sum_str('q','e','l', 'e', 'k','a'))
print(sum_str(f'{2}, {8}, {9}, {4}'))
print(sum_str('2', '8', '9', '4'))