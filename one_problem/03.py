def find_non_multiples(start: int, end: int) -> list:
    if start > end:  # ตรวจสอบ input
        return []
    return [num for num in range(start, end + 1) if num % 3 != 0 and num % 4 != 0 and num % 5 != 0]

# Example Test
print(find_non_multiples(10, 25))  # [11, 13, 17, 19, 23]
