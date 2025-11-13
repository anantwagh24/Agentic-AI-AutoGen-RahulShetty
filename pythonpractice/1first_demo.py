#VVIMP -- semicolon is not required but CODE indentation is MOST IMP

print('Anant Pro - single quote')
print("Anant Pro - Double quote")

#comment for the testing

#declaring variable, no need to mention datatype like java, see below example:
a=3
print(a)

Str = "hello world"
print(Str)

#defining multiple variable at one line
b,c,d,e=234,6.4,'Great', 100+3j
#print("value is:"+b) --- not allowed in python unlike java, WE CANNOT CONCANETATE INT AND STRING, ideal is as below:
print("{} {}".format("value is:", b))

print(f"value is: {b}")
#to know the datatype of variable: NUMERIC, STRING, LIST, COMPLEX, TUPLE
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
