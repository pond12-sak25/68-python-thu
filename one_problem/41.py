from typing import List

def calculate_discounted_prices(prices: List[float], discount_percentage: float) -> List[float]:
    return [round(p * (1 - discount_percentage / 100), 2) for p in prices]

# Example
print(calculate_discounted_prices([100.0, 250.0, 75.0], 20.0))
# [80.0, 200.0, 60.0]
