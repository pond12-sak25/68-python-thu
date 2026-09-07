def find_multiples_of_three_and_four(start: int, end: int) -> list:
    if start > end:  # ตรวจสอบ input
        return []
    return [num for num in range(start, end + 1) if num % 12 == 0]  
    

# Example Test
print(find_multiples_of_three_and_four(10, 50))  # [12, 24, 36, 48]
