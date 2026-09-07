def group_by_signature(words: list) -> list:
    groups = {}
    for word in words:
        # ข้ามคำที่ว่างหรือมีอักขระนอก a-z
        if not word.isalpha() or word == "":
            continue
        # ใช้ตัวพิมพ์เล็กทั้งหมด (ไม่สน case)
        key = "".join(sorted(word.lower()))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
