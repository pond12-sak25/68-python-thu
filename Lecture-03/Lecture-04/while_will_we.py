keep_going = 'y'
while keep_going == 'y':


    sales = float(input("Enter the sales amount: "))
    comm_rare = float(input("Enter the commission rate: "))
    commission = sales * comm_rare
    print("The commission is: ", format(commission, ".2f"))

    sales = float(input("Enter the sales amount: "))
    comm_rare = float(input("Enter the commission rate: "))
    commission = sales * comm_rare
    print("The commission is: ", format(commission, ".2f"))

    sales = float(input("Enter the sales amount: "))
    comm_rare = float(input("Enter the commission rate: "))
    commission = sales * comm_rare
    print("The commission is: ", format(commission, ".2f"))

    keep_going = input("Do you want to continue? (y/n): ")