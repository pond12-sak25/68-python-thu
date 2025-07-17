keep_going = 'y'
while keep_going== 'y':
    sale = float(input("Enter the sale amount: "))
    commission_rate = float(input("Enter the commission rate: "))
    commissio = sale * commission_rate
    print(f"Commission: {'commission':.2f}")
    keep_going= input("Do you want continue?(y/n):")