def find_multiples_of_three(start: int, end: int) -> list:
    
   if start > end:
       return []
num = []
for i in range(10, 26):
   if (i % 3 ) == 0:
    num.append(i)
print (num )
   

     