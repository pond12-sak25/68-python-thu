num_emps = int(input('How many employees? '))
with open('employees.txt', 'w') as emp_file:
    for count in range(1, num_emps +1 ):
        print("enter data for` employee #", count, sep='')
        name = input('Name: ')
        id_num = input('ID: ')
        dept = input('Department: ')
        
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        print()  # print a blank line between employees
        