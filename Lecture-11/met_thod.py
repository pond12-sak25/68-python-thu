class Dog:
    species = "Canis familiaris"  # Class attribute
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
mikey = Dog("Mikey", 6)
print(mikey.description())
print(mikey.speak("Woof Woof"))