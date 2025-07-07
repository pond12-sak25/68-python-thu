House_worked = float(input("Enter the number of hours worked: ")) 
rate = float(input("Enter the pay rate: "))

if House_worked >= 40:
    Gross_Pay = ((House_worked-40)*1.5*rate) + (40*rate)
else:
    Gross_pay= (House_worked * rate)
    
    overtime_hours = House_worked - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    # sum of regular pay and overtime pay
    Pay = Gross_pay + overtime_pay
