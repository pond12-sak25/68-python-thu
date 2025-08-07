attendance_week = [
    ["Alice", "Bob", "Charlie", "David"],
    ["Alice", "Bob", "Charlie", "DAvid"],
    ["Alice", "Bob", "David"],
    ["Alice", "Charlie", "David"],
    ["Bob", "Charlie", "David"],

]

attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

present_students = set.intersection(*attendance_sets)

