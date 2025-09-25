class animal:
    def __init__(self, name,):
        self.name = name
        

    def speak(self):
        return "some sound."
    
class dog(animal):
    def speak(self):
        return f"{self.name} says Woof Woof"

class cat(animal):
    def speak(self):
        return f"{self.name} says Meow Meow"
    
dog1 = dog("Buddy")
cat1 = cat("Whiskers")

print(dog1.speak())
print(cat1.speak())