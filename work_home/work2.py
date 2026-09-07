def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    single_list = []
    seen = set()
    max_length = 0
    result = []

    for group in words:
        for word in group:
            if word in seen:
                while single_list and word in seen:
                    seen.remove(single_list.pop(0))
            single_list.append(word)
            seen.add(word)

            # อัปเดตทุกครั้งหลังเพิ่ม
            if len(single_list) > max_length:
                max_length = len(single_list)
                result = [single_list[:]]
            elif len(single_list) == max_length:
                result.append(single_list[:])

    return max_length, result


# ทดสอบ
words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# คาดหวัง: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# คาดหวัง: (4, [['mouse', 'cat', 'bird', 'dog']])
