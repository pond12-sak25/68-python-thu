input_str = input("Enter a string: ")
vowel = "aeiouAEIOU"
out_str = ""
for char in input_str:
    if char in vowel:
        out_str += "*"
    else:
        out_str += char

        print("Output string:", out_str)