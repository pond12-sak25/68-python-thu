score = int(input("Enter your score:"))
while score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
    print("Please enter a valid score.")
    score = int(input("Enter your score:"))
  