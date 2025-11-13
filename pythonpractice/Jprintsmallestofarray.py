a=[10,20,49,5,6,67,7,8,9,9,19]
min=a[0]

for i in range(len(a)):
    if a[i]<min:
        min=a[i]
print(f"smalles value is: {min}")