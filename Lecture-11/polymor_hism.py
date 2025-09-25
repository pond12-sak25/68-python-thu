class anime:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
class dog(anime):
    def speak(self):
        return "Woof!"
class cat(anime):
    def speak(self):
        return "Meow!"
    
def make_animal_speak(animal):
    print(animal.speak())
    
dog1 = dog()
cat1 = cat()

make_animal_speak(dog1)
make_animal_speak(cat1)    