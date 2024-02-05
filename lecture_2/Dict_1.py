dictionary = {}
dictionary = {'up': ''}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)
print(dictionary['left'])
#'left': '◄═'
dictionary['left'] = '<='          #'◄═'
print(dictionary['left'])
del dictionary['right']
print(dict(dictionary))

