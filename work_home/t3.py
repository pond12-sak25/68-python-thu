def find_non_multiples(start: int, end: int) -> list:
   if start <= end:
       return []
num = []
for i in range(10, 25):
   if (i % 4) % 5 and i % 3   != 0:
    if (i % 2)  != 0:
     num.append(i)
print (num )
   

