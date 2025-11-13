#defining multiple variable at one line
b,c,d,e=234,6.4,'Great', 100+3j
#print("value is:"+b) --- not allowed in python unlike java, WE CANNOT CONCANETATE INT AND STRING, ideal was as below:
print("{} {}".format("value is:", b))


#to know the datatype of variable: NUMERIC, STRING, LIST, COMPLEX, TUPLE
print(type(b))
print(type(c))
print(type(d))

#LIST is datatype that allow mix of all datatypes such as int, float, string etc. LIST IS MUTABLE it means we can make changes in the list
values= [1,2,'Anant',3.9,5]
print(values[0]) #1
print(values[2]) #3
print(values[-1]) #5
print(values[0:3]) # it will print 1st, 2nd and 3rd values
values.insert(3,'Wagh') #adding value between the existing array
print(values)
values.append("End value") #adding value to the end
print(values)
values[2]="ANANT" #TO UPDATE THE EXISTING VALUE OF AN ARRAY
print(values)
del values[0] #deleting the first value of an array
print(values)



#TUPLE- another data type and it is IMMUTABLE
val = (1,2,3,'Anant',4,5,3.1,'Wagh',9)
print(val[1])
#val[2]=2 --- this is not possible in case of tupe as its immutable/ not changeable



#DICTIONARY data type
x={1:"f name", 2:"l name", 'c':33}

print(x[1]) #it will print the value of 1 element i.e. f name
print(x['c'])


#defining empty dictionary
dic={}

dic["fname"]="Anant"
dic["lname"]="Wagh"
dic["gender"]="male"
print(dic)
print(dic["lname"])