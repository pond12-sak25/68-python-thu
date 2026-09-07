from typing import Dict, List, Tuple

def calculate_median(provinces: Dict[str, int]) -> List[Tuple[str, int]]:
    values = sorted(provinces.values())
    n = len(values)
    mid = n // 2
    if n % 2 == 1:
        median = values[mid]
    else:
        median = (values[mid - 1] + values[mid]) / 2

    return [(country, count) for country, count in provinces.items() if count == median]

# Example
print(calculate_median({'Thailand':76, 'Laos':17, 'Vietnam':58, 'Japan':47, 'China':23}))
# [('Japan', 47)]
