employee = int(input("Enter number of employee:"))

if employee < 50:
    print("Small company")
elif employee < 250:
    print("Medium company")
elif employee >= 250:
    print("Lage company")