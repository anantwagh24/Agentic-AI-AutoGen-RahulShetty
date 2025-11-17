num=int(input("enter your value: "))

prime=True

if num<1:
    prime=False

else:
    for i in range(2, num):
        if num%i==0:
            prime=False
            break
if prime:
    print(f"{num} is PRIME ")
else:
        print(f"{num} is COMPOSITE ")