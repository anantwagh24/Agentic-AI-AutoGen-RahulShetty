a=[1,2,4,5,0.5,6,7,7,8,99]

min=a[0]

for i in range(len(a)):
    if a[i]<min:
        min=a[i]
print("smallest value is:",min)


# #Shortcut and easiest way:
# array=list(map(float,input("enter your input: ").split(",")))
# print("smallest value is: ", min(array))