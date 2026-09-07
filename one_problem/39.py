def remove_word(sentence: str, word_to_remove: str) -> str:
    words = sentence.split()
    filtered = [word for word in words if word != word_to_remove]
    return " ".join(filtered)

# Example
print(remove_word("Python is a popular programming language.", "popular"))
# "Python is a programming language."
