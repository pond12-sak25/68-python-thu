def calculate_sum_and_average() :
    number = []

    for i in range(5):
        num = float(input(f"Enter {i+1} :"))
        number.append(num)

    total = sum(number)
    average = total / len(number)

    print (average)

calculate_sum_and_average()