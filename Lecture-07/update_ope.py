set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}

set1 & set2  # Intersection
print("After & operation:", set1 )

set1 = {1, 2, 3, 4, 5}

set1 -= set2  # Difference
print("After -= operation:", set1)

set1 = {1, 2, 3, 4, 5}

set1 ^= set2  # Symmetric difference
print("After ^= operation:", set1)