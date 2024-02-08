name = ['Dima', 'Vasya', 'Igor', 'Kirill']
book = ', '.join(name)

def data():
    data = open('namebook.txt', 'a', encoding='utf-8')
    for book in enumerate(name, 1):
        print(*book)
        data.write(str(book))
data()
