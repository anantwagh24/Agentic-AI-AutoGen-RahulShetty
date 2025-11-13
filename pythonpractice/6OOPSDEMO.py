#CLASSES: a user defined blueprint of prototypes
#a calculator is class  and sum, multiplication, minus are methods
class Calculator:
    num = 100 # a class variable -- it is always declared in the class
    # a variable declared or called inside constructor is called a instance variable

    #functions when used in class, they called it as method--- so simple
    def getData(self):
        print("im now executing a method in class")

obj = Calculator() #syntax to create object of the class in the python
obj.getData()
print(obj.num)