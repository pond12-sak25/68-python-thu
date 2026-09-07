age= int(input("Enter your age :"))
income = int(input("Enter your income :"))
if age >= 18 and age <= 65 and income >= 30000:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan")