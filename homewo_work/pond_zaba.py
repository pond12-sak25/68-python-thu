def find_pair(nums:list,target:int)-> list:
    result = []
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]*nums[j]==target:
                result.append([nums[i],nums[j]])
                
    return  result
print(find_pair([2,4,5,7],14))