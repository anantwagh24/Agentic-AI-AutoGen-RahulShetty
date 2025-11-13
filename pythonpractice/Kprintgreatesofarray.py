a=[1,2,3,4,56,6,0.01,7,7,8,8,99,0.1,0.2,5656]

min=a[0]

for i in range(len(a)):
    if a[i]<min:
        min=a[i]

print(f"smallest value is:{min}")