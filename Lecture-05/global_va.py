global_variable = "I'am a outside the function"
def my_function(): 
    print(global_variable)

my_function()
print(global_variable)