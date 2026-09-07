def highest_sales_country(sales: dict[str, int]) -> tuple[str, int]:
    return max(sales.items(), key=lambda x: x[1])

# Example
sales_data = {
    "Thailand": 1500,
    "Laos": 1200,
    "Vietnam": 1800,
    "Japan": 1700,
    "China": 2000
}
print(highest_sales_country(sales_data))  # ("China", 2000)