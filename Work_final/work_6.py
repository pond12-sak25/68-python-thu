
def check_prime(n: int) -> str:
    nobox = [] 
    i=1
    while i <= number:
        if n % i ==0:
            nobox.append(i)
        i+=1
        
    return nobox  
     





number = int(input("Enter num: "))
print(check_prime(number)) 

