score = int(input("Enter your score: "))
while score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    score = int(input("Enter your score: "))    

print(f"Your score is: {score}")