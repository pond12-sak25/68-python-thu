phonebook = {'aniracha': '123-456-7890', 'bob': '987-654-3210', 'charlie': '555-555-5555'}
print(phonebook)

print(phonebook['aniracha'])
print(phonebook.get('bob'))

key = 'ploto'
if key in phonebook:
    print(phonebook['ploto'])
else:
    print(key+" not found in phonebook")

phonebook['dave'] = '444-444-4444'
phonebook['ploto'] = '111-111-1111'
phonebook['aniracha'] = '123-456-7899'  # Update existing entry
print(phonebook)

del phonebook['dave']  # Remove entry
print(phonebook)