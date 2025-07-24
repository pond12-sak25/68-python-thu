def is_armstrong_number(num):
    digit_length = len(str(num))
    total = 0
    is_arms = False
    for i in num:
        total += int(i) ** digit_length
    if total == int(num):
        is_arms = True
    return is_arms, total

value = input("Enter a number: ")
result, total_sum  =  is_armstrong_number (value)
print(f"{result} {value} = {total_sum}")
        