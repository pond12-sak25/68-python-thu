try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result:, '{result}'")
except Exception as e:
    print(f"Result:, '{e}'")
print("End")
    