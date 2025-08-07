phonebook = {'Alice': '123-456-7890', 'Bob': '987-654-3210', 'Charlie': '555-555-5555'}

phonebook['bell'] = [1, 3, 5]  # Add a new entry

elements = len(phonebook)  # Get the number of entries
print('These are ', elements, ' entries in the phonebook.')

for key in phonebook:  # Iterate through keys
    print('key,  phone number is: ', phonebook[key])  # Print each key-value pair
    phonebook['bell'] [1] = 9
print(phonebook)  # Print the modified phonebook