class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value error: {value} is not allowed.")
        
def check_positive(value):
    if num < 0:
        raise NegativeValueError(num)
    else:
        print(f"{num} is a positive number.")
try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
except NegativeValueError as e:
    print(e)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
finally:
    print("Execution completed.")