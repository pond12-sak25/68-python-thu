student = {"name": "Alice", "age": 25, "major": "Computer Science", "grade": "A"}

student['age'] = 26  # Modify age
student["major"] = "Data Science"  # Modify major
print(student)

del student['grade']  # Remove grade
print(student)

removed_major = student.pop('major')  # Remove major with a default value
print(removed_major)
print(student)