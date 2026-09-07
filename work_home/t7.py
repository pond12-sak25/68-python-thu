def prime_numbers_in_range(start: int, end: int) -> tuple:
    if start > end:
        return 
    
    boxboy = []
    for i in range(start,end+1):
        count = 0
        
        for j in range(1,i+1):
            if i%j ==0:
                count+= 1
        if count ==2:
           boxboy.append(i)    
    return tuple(boxboy)





print(prime_numbers_in_range(10,20))