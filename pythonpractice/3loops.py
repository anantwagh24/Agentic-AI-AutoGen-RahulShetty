#if else loop
greeting="good morning"
a=4
if greeting=="good mornin" or a>10:
    print("success -  one or both conditions satisfied")
else:
    print("fail - both conditions are failing")

print("independent line - if else loop completed")


#for loop

obj=[2,3,4,5,6,7]
for i in obj:
    print(i)
   # print(i*2)

summation=0
for j in range(1,6):
    summation= summation + j
    print("{} {}".format("summation", summation))

print("******************")
for k in range(1,10,2): # loop will increment by 2 each time, similar to i+2 in java
    print(k)

print("******************")

for m in range(10):
    print(m)
