try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError :
    print("Eror:Result.")
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Result:, {result}")
print("End")
    