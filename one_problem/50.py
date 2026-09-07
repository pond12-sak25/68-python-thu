from typing import List

def find_words_of_length(words: List[str], length: int) -> List[str]:
    return [word for word in words if len(word) == length]

# Example
print(find_words_of_length(["apple", "banana", "cherry", "date", "fig", "grape"], 5))
# ["apple", "grape"]
