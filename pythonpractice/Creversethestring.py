#Approach 1:
#
# str=input("enter your string: ")
#
# s2=str[::-1]
# print(s2)

#Approach 2:
str=input("enter your string: ")

for i in range(len(str)-1, -1, -1):
    print(str[i], end="")