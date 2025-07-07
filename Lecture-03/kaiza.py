inchar = input("Enter character to check:")
if inchar >= 'A' and inchar <= 'Z':
    print("Your input is uppercase lettter: " ,inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("Your input is lowercase lettter: " ,inchar)
elif inchar >= '0' and inchar <= '9':
    print("Your input is a number: " ,inchar)
else:
    print("Your input is not a letter or number:",inchar)

