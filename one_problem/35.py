def print_diamond_pattern(n: int) -> None:
    for i in range(1, n+1):
        print("*" * i)
    for i in range(n-1, 0, -1):
        print("*" * i)

# Example
print_diamond_pattern(3)
