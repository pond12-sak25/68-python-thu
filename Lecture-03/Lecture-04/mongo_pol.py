
while True:
    row = int(input("Enter the number of row: "))
    cols = int(input("Enter the number columns: "))
    for row in range(row):
        for col in range(cols):
            print("*", end=" ")
        print()