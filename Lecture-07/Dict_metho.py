student = {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

print(student.keys())  # Print all keys
print(student.values())  # Print all values
print(student.items())  # Print all key-value pairs

print(student.get('name'))  # Get value for 'name' key
print(student.get('grade', 'Not Found'))  # Get value for 'grade' key

major = student.pop("major")
print(major)  # Print the removed item
print(student)  # Print the modified student dictionary

last_item = student.popitem()  # Remove and return the last item
print(last_item)  # Print the last removed item
print(student)  # Print the modified student dictionary

student.clear()  # Clear the dictionary
print(student)  # Print the cleared dictionary