from typing import Tuple

def calculate_coins(amount: int) -> Tuple[int, int, int, int]:
    tens = amount // 10
    amount %= 10
    fives = amount // 5
    amount %= 5
    twos = amount // 2
    amount %= 2
    ones = amount
    return (tens, fives, twos, ones)

# Example
print(calculate_coins(28))  # (2, 1, 1, 1)
