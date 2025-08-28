def exam_a_plus():
    with open("example_a+.txt", "a+") as file:
        file.seek(0)
        
        content = file.read()
        print("current content of the file: ")
        print(content)
        
        file.write("Appending a new line at the end.\n")
        
        file.seek(0)
        updated_content = file.read()
        print("updated content of the file: ")
        print(updated_content)

exam_a_plus()