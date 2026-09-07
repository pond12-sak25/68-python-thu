def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    box = []
    
    ## 1. รวม list 2 มิติ -> 1 มิติ
    for rows in words:
        for word in rows:
            box.append(word)

    max_length = 0
    results = []

    # 2. ลองเริ่มช่วงจากทุกตำแหน่ง
    for start in range(len(box)):
        seen = set()

        # 3. เดินต่อจากตำแหน่ง start
        for o in range(start, len(box)):
            
            # ถ้าซ้ำ ให้หยุดช่วงนี้
            if box[o] in seen:
                break

            # เก็บคำที่เจอ
            seen.add(box[o])

            # ความยาวช่วงปัจจุบัน
            length = o - start + 1

            # เจอช่วงที่ยาวกว่าเดิม
            if length > max_length:
                max_length = length
                results.clear()
                results.append(box[start:o + 1])

            # เจอช่วงที่ยาวเท่าเดิม
            elif length == max_length:
                results.append(box[start:o + 1])

    return max_length, results
    

words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])
