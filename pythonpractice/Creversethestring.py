#Approach 1:

# s1="ADANIA"
# print(f"original string is: {s1}")
#
# s2=s1[::-1]
# print(f"reversed string is: {s2}")


#Approach 2:
str=input("Enter a string: ")

for i in range(len(str)-1, -1, -1):
    print(str[i], end="")