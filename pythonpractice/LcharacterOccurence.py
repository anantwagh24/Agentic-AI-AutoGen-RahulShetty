#Approach 1:

# str= input("enter your string: ")
# char='a'
# count=0
#
# for i in range (len(str)):
#     if str[i]==char:
#         count+=1
# print(f"count of char '{char}' is {count}")
#


#Approach 2:

str= input("enter your string: ")
count=0

str=str.lower()
print(str.isupper())
print(str.islower())

for ch in str:
    if ch=='a':
        count+=1
print(f"count of char is {count}")