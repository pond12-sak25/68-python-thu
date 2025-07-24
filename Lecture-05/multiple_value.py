def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum

numbers = [10, 20, 30, 40, 50]
total, average, minimum, maximum = calculate_stats(numbers)
print(f'Total is {total},')
print(f'Average is{average}')
print(f'Minimum is {minimum}')
print(f'Maximum is {maximum}')