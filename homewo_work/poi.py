def find_missing(numbers:list, arr:int) ->int:
    expected_sum = arr*(arr+1)//2
    return expected_sum-sum(numbers)
    
    
    
print(find_missing([1,2,4,5],5))
print(find_missing([1,2,3,4,6],6))