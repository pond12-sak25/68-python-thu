from abc import ABC, abstractmethod
class Absclass(ABC):
    def print_info(self,x):
        print("You are wood:",x)
    @abstractmethod
    def task(self):
        print("You are wood")
        
class test_class(Absclass):
    def task(self):
        print("You are test class")
class example_class(Absclass):
    def task(self):
        print("You are example class")
        
test_obj = test_class()
test_obj.task()
test_obj.print(100)

exam_obj = example_class()
exam_obj.task()
exam_obj.print(200)

print("Type of test_obj:", isinstance(test_obj, Absclass))
print("Type of exam_obj:", isinstance(exam_obj, Absclass))