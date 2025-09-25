class shape:
    def area(self):
        return NotImplementedError("Subclass must implement abstract method")
class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * (self.radius ** 2)
    
shapes = [rectangle(10, 20), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}") 