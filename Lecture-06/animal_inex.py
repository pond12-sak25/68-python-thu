animals = ['cat','dog','rabbit','hamster','dog','parrot','dog']
firs_dog_index = animals.index('dog')
print(f'First dog index: {firs_dog_index}')

second_dog_index = animals.index('dog',firs_dog_index + 1)
print(f'First dog index: {second_dog_index}')
