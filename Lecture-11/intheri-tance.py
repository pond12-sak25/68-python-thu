class Dog:
    species = "Canis familiaris"
    
    def calage(self, age):
        print('dog age is {}'.format(age*7))
class someotherbread(Dog):
    pass
        
class somebread(Dog):
        species = "bulldog"
        def calage(self, age):
            print('bulldog age is {}'.format(age*5))
            
frank = somebread()
print(frank.species)
frank.calage(5)

beans = someotherbread()
print(beans.species)
beans.calage(5)