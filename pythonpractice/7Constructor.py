#Constructor is an method that gets automatically called when we create an object of a class
#self keyword is mandatory to call variable name in the method
#instance and class variable have whole new different purpose
#contructor name should be __init__

class Calculator:
    num=100 #class variable -- it is always declared inside a class
    #default constructor
    def __init__(self,a,b):
        self.firstNumber= a
        self.secondNumber= b   #here a and b are the instance variable
        str="Anant instance variable" # instance variable -- it is always declared inside a constructor
        print("im getting called automatically when an object of class is created")

    def getData(self):
        print("im executing this code now to learn constructor")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num

obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5)
obj1.getData()
print(obj1.Summation())