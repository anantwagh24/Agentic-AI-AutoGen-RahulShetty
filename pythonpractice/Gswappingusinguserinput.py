a=int(input("enter first number:"))
b=int(input("enter second number: "))
print(f"numbers before swapping: {a} and {b}")

a=a+b
b=a-b
a=a-b

print(f"numbers after swapping: {a} and {b}")