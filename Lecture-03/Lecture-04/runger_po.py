
print('KPH\tMPH')
print('-----------------')

for kph in range(50,140,10):
    mph = kph * 0.6214
    print ('{:.1f}\t{:.1f}'.format(kph,mph))