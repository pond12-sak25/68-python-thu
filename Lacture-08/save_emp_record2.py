num_emps = int(input("Enter  number of employees:"))
with open ("employees.txt" ,"w") as outfile:
     for i in range(num_emps):
         print("Enter details for employee", i+1)
         emp_name = input("Name: ")
         emp_id = input("ID: ")
         emp_dept = input("Department: ")
         outfile.write(f"{emp_name},{emp_id},{emp_dept} \n")
print(f"(num_emps) employee records saved to employees.txt")