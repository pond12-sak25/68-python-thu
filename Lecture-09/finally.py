try:
    number = float(input("Enter a number: "))
    demoninator = float(input("Enter a denominator: "))
    result = number / demoninator
    print(f"Result: {result}")
    
except ZeroDivisionError :
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("Execution completed.")
    
print("End")
  