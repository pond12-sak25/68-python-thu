a = [1,2,3]
b = a

c = [1,2,3]
d = [1,2,3]

print(a is b) # True, a and b refer to the same object
print(a is c) # False, a and c refer to different objects
print(c is d) # False, c and d refer to different objects

print(a == b) # True, since  the  content of a and b are equal
print(c == d) # True, since  the  content of c and d are equal