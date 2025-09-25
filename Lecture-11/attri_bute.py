class dog:
    species = "mammal"
    def __init__(self, name, age):
            self.name = name
            self.age = age
            
dog1 = dog("Buddy", 3)
dog2 = dog("Max", 5)

print("{} is a {} and is {} years old.".format(dog1.name, dog1.species, dog1.age))


if dog1.species == dog2.species:
    print("{} and {} are both {}s.".format(dog1.name, dog2.name, dog1.species))