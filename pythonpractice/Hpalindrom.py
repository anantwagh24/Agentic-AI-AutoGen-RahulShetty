sum=0
num=int(input("Enter a number: "))
temp=num

while num>0:
    r=num%10
    sum=(sum*10)+r
    num=num//10


if sum==temp:
    print("palindrome")
else:
    print("not palindrome")
