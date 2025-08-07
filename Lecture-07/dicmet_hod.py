phonebook = {'anirach': '777-777-7777', 'bob': '888-888-8888', 'charlie': '999-999-9999'
             ,'donald': '000-000-0000' , 'pluto': '111-111-1111'}

heroesdict = {}
heroesdict['hulk'] = '888-1111'
heroesdict['thor'] = '888-2222'
print(heroesdict.get('hulk', 'key not found'))  # Get value for 'hulk' key
print(heroesdict.get('hulk', 'key not found'))  # Get value for 'spiderman' key

for key, value in phonebook.items():  # Iterate through key-value pairs
    print(key ,value)  # Print each key-value pair

print(phonebook.keys())  # Print all keys
print(phonebook.values())  # Print all values

print(phonebook.pop('mick', 'element not found'))  # Print all key-value pairs
print(phonebook.pop('mickey', 'element not found'))  # Remove and return the last item
print(phonebook)  # Remove and return the last item
print(phonebook.popitem())  # Remove and return the last item
print(phonebook)  # Print the modified phonebook
phonebook.clear()  # Clear the dictionary
print('after clear: ')  # Print the cleared dictionary
print(phonebook)  # Print the cleared dictionary