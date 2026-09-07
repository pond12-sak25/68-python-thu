max = 5
total = 0

print("This program will calculate the average of 5 numbers.")
print(max, "numbers will be entered.")

for counter in range(max):
    number = int(input("Enter a number: "))
    total = total+number
print("The average of the numbers is:", total )