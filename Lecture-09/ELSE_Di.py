def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Exception caught:", e)
        
    else:
        return f"Result: {result}"
    return result
a,b = map(int, input("Enter two numbers (a b): ").split())
print(divide(a, b))
print("End")