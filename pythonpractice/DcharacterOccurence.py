
str=input("enter your string: ")

ch=input("enter your character: ")

count=0

for i in range(len(str)):
    if str[i]==ch:
        count+=1
print(f"occurrence of {ch} is {count} times")