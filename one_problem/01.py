try:
    def find_multiples_of_three(start: int, end: int) -> list:
        if start>end :
         return[]
        return [num for num in range(start,end+1)if num % 3 ==0]


    
    






    result = find_multiples_of_three(10,25)
    print(result)
except:
 print("no")
    