from typing import Tuple

def calculate_profit(sales: Tuple[float, float, float, float, float],
                     costs: Tuple[float, float, float, float, float]) -> Tuple[Tuple[float, float, float, float, float], float]:
    annual_profits = tuple(s - c for s, c in zip(sales, costs))
    total_profit = sum(annual_profits)
    return annual_profits, total_profit

# Example
print(calculate_profit((10000,15000,20000,25000,30000), (7000,8000,9000,11000,12000)))
