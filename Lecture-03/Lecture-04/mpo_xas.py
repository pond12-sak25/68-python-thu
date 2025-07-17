keep_going = 'y'
while keep_going.lower() == 'y':
    sale_cost = float(input("Enter the item's whoesale in bold: "))
    total = sale_cost * 2.5
    print("The Commission is: ${:.2f}".format(total))
    keep_going = input("Do you want to calculate another commission? (y/n):")