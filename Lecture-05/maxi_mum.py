def find_max(*args):
    """Find the maximum value from a list of arguments."""
    if not args:
        return None  # Return None if no arguments are provided
    max_value = args[0]  # Start with the first argument as the maximum
    for num in args:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found
    return max_value
result = find_max(5, 6, 9, 1, 2)
print(f'The maximum value is {result}')