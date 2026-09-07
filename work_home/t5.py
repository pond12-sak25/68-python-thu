def find_divisors(n: int) -> List[int]:
    numbes = []
    for i in range(1,n+1,1):
       if n % i ==0:
        numbes.append(i)
    return numbes
           
    




 
print(find_divisors(20))