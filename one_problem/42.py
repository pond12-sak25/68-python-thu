def calculate_jumps(d: int, s: int) -> int:
    return (d + s - 1) // s

# Example
print(calculate_jumps(20, 7))  # 3
