max = 5
total = 0.0
print('This program calculates the sum of')
print(max, 'number you will enter.')
for counter in range(max):
    number = int(input('Enter a number: ' ))
    total += number

    print('The total is', total)