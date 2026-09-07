from collections import Counter
def find_count(s:str)->dict:
    counts = Counter(s)
    return {char: count for char, count in counts.items()if count >1}

print(find_count("aaabbcddddd"))
print(find_count("aaabbcddddd"))
