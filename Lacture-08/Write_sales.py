num_days = int(input('For how many days do you have sales? '))
outfile = open('sales.txt', 'w')
with open ('sales.txt', 'w') as sales_file:
    for day in range(1, num_days + 1):
        sales = float(input(f'Enter the sales for day {day}: '))
        sales_file.write(str(sales) + '\n')
        
print('data written to sales.txt.')