phone = ['8 987 345 45 32', '8 753 724 45 21', '8 543 972 54 64', '8 792 543 13 78']
name = ['Сергей', 'Василий', 'Святослав', 'Кирил']
city = ['Шахты', 'Воскресенск', 'Ставрополь', 'Ростов']
contact = list(zip(name, phone, city))
print(contact)
contact_num = list(enumerate(contact))
print(contact_num)