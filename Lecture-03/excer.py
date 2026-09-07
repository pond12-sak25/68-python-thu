Work_hours = int(input("Enter your work hours :"))
payrate = (input("Enter your pay rate :"))
if Work_hours <= 40:
    print("Your pay is :", Work_hours * payrate)
else:
    print("You have worked overtime.")
    print("Your pay is :", 40 * payrate + (Work_hours - 40) * payrate * 1.5)
    
