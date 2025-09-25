class car :
    whells = 4
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start_engine(self):
        return f"Engine started {self.make} {self.model} {self.year}"
        
    def stop_engine(self):
        return  f"Engine stopped {self.make} {self.model} {self.year}"
    
my_car = car("Toyota", "Camry", 2020)
print(f"My car details: {my_car.make}, {my_car.model}, {my_car.year}")
print(my_car.start_engine())