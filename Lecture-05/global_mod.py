counter = 0
def increment_counter():
    global counter
    counter = counter + 1
    
increment_counter()    
increment_counter()    
print(f"Counter incremented to: {counter}")