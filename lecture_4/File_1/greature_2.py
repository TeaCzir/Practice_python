name = 'Dima Vasya Igor Kirill'
contacts = name.strip()  
print(*contacts)
contact = open('nameb.txt', 'a', encoding='utf-8')
contact.write(f'{name}')
print(name)


                     # .split('\n\n')
#for contact in enumerate(contacts_list, 1):



