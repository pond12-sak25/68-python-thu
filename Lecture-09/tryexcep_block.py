filename = input("Enter filename: ")
try :
    
    with open(filename ,'r') as file:
        contents = file.read()
        print(contents)
        file.close()
except IOError :
    print('an error occurred trying to read the file.')
    print("Cannot open file:, '{filename}'")
    
print("End")