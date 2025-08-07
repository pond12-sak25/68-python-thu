fruits = {'apple', 'banana', 'cherry' }

fruits.add('orange')
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.discard('grapes')  # No error if 'grapes' is not present
print(fruits)

removed_item = fruits.pop()  # Removes and returns an arbitrary element
print(removed_item)
print(fruits)

fruits.clear()  # Removes all elements from the set
print(fruits)