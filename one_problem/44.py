def calculate_investment_growth(principal: float, annual_rate: float, years: int):
    results = []
    for year in range(1, years + 1):
        amount = principal * ((1 + annual_rate/100) ** year)
        results.append(round(amount, 2))
    return results[:5]

# Example
print(calculate_investment_growth(1000, 5, 5))
