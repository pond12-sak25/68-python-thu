column = int(input("Enter the number of column: "))
for i in range(1,100):
    print(f'(i:3)', end=" ")
    if i % column == 0:
        print()