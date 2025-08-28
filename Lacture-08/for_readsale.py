with open('sales.txt', 'r') as infile:
    total_sales = 0.0
    for line in infile:
         amout = float(line.strip())
         total_sales += amout
         print(f'Sales amount: {amout:,.2f}')
    print(f'Total sales: {total_sales:,.2f}')