class student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        
    def sumscore(self):
        return self.score1 + self.score2 + self.score3
    
    def __str__(self):
        return "Name: {}, Score1: {}, Score2: {}, Score3: {}, Total Score: {}".format(self.name, self.score1, self.score2, self.score3, self.sumscore())
    
stu1 = student("Alice", 85, 90, 78)
print(stu1.name, stu1.sumscore())
print(stu1)