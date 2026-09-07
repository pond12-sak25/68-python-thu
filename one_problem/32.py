from typing import List

def calculate_median(lst: List[int]) -> float:
    lst.sort()
    n = len(lst)
    mid = n // 2
    if n % 2 == 1:
        return float(lst[mid])
    else:
        return (lst[mid - 1] + lst[mid]) / 2

# Example
print(calculate_median([8, 4, 7, 4, 6, 2, 10, 9, 3, 7, 1]))  # 6
