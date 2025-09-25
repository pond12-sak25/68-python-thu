class employee:
    def __init__(self):
        self.__maxearn = 50000     # Private attribute
        
    def earn(self):         # Getter method
        print("earning is :{}".format(self.__maxearn))
        
    def setmaxearn(self, earn):   # Setter method
        self.__maxearn = earn
emp1 = employee()
emp1.earn()
emp1.setmaxearn(100000)
emp1.earn()
emp1.setmaxearn(200000)
emp1.earn()