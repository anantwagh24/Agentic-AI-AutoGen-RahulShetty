#In Python, function is a group of related statements that perform a specific task.

#normal function declaration
def GreetMe():
    print("good morning")

GreetMe()

print("**********")


# function declaration with variable
def GreetMe(name):
    print("good morning: " + name)

GreetMe("Anant Wagh")

# THIS another function with Integer
def AddIntegers(a,b):
    print(a+b)

AddIntegers(4,5)

#OR THAT
def AddInteger(a,b):
    return a+b
print(AddInteger(4,5))