def print_diamond_pattern(n: int) -> None:
    half = n // 2
    for i in range(half):
        stars = "*" * (half - i)
        hyphens = "-" * (2 * i)
        print(stars + hyphens + stars)
    for i in range(half-2, -1, -1):
        stars = "*" * (half - i)
        hyphens = "-" * (2 * i)
        print(stars + hyphens + stars)

# Example
print_diamond_pattern(10)
