def print_number_pattern(rows: int) -> None:
    for i in range(1, rows + 1):
        dashes = "-" * (rows - i)
        numbers = "".join(str(j) for j in range(i, 0, -1))
        print(dashes + numbers)

# Example
print_number_pattern(5)
