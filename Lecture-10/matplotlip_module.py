import matplotlib.pyplot as plt

x= [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x, y, marker='o' , linestyle='-', color='r')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.grid(True)
plt.title('Sakchai_wonpromrach')

plt.show()