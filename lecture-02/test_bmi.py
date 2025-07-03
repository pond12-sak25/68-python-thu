weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
height = height/100
bmi = weight / (height **2)

print("Your BMI is", bmi)
