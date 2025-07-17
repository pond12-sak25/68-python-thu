print('MPH\tKPH')
print('-----------------')

for mph in range(50,140,10):
    kph = mph * 0.6214
    print ('{:.1f}\t{:.1f}'.format(mph,kph))