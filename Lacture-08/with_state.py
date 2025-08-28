with open ("example.txt", "r") as infile:
     lines = infile.readlines()
     #print(lines)
     for line in lines:
         print(line.strip())