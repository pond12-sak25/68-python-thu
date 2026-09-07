def find_multiples_of_three_and_four (start: int, end: int) -> list:
     if start <= end:
       return []
num = []
for i in range(10, 50):
   if (i % 3) % 4   == 0:
    if i % 4 == 0:
     num.append(i)
print (num )
   