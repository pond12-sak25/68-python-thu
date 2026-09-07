def check_prime(n: int) -> str:
    if n <= 1:
       return  'is not prim'
   
    boxboy = []
    for i in range(1,n+1,1):
        if n % i ==0:
            boxboy.append(i)
            
    if len(boxboy) ==2 :
        return "prim"
    else :
        return "not prim"
        

print (check_prime(18))
print(check_prime(17))
