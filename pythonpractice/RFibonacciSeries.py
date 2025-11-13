n=10
first=0
second=1


print("fibonacci series: ")

for i in range(1, n+1):
    print(first, end=" ")
    next=first+second
    first=second
    second=next