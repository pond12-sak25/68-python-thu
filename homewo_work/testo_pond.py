def find_all_pairs_with_product(num:list,target:int)-> list:
    pairs = []
    target = int(input("Enter Nume: "))
    for i in range(num):
        for j in range(i+1):
            if num[i] * num[j] == target:
                pairs.append((num[i], num[j]))
    return pairs


print(find_all_pairs_with_product([1, 2, 3, 4, 6], 6))
# Output: [[1, 6], [2, 3]]

print(find_all_pairs_with_product([2, 4, 5, 7], 14))
# Output: [[2, 7]]20

print(find_all_pairs_with_product([3, 5, 9, 10], 25))
# Output: []

print(find_all_pairs_with_product([1, 2, 3, 4, 5], 20))
# Output: [[4, 5]]















