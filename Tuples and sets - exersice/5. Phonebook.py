phone = input()
phonebook = {}
while len(phone) > 1:
    name, number = phone.split('-')
    phonebook[name] = number
    phone = input()
n = int(phone)

for i in range(n):
    i = input()
    if i not in phonebook:
        print(f'Contact {i} does not exist.')
    else:
        print(f'{i} -> {phonebook[i]}')

