try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result:, '{result}'")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

print("End")