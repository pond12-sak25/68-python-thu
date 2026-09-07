
while True:
    row = int(input("Enter the number of row: "))
    cols = int(input("Enter the number columns: "))
    for i in range(row):
        for j in range(cols):
            print("*", end=" ")
        print()